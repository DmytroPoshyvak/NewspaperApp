from django.shortcuts import render , redirect
from django.views.generic import TemplateView , ListView , DetailView , CreateView , UpdateView , DeleteView
from . import models
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from . import forms
from user_app.models import PersonalCustomUser

class NewspaperTemplateView(TemplateView):
    template_name = 'index.html'

class NewspapeprListView(ListView):
    template_name = 'newspaper_list_view.html'
    model = models.Article
    context_object_name = 'list'

def newspaper_detail_view(request, pk , id=999):
    a = models.Article.objects.get(id=pk)
    ccc = models.Coment.objects.filter(article = a)
    if len(ccc) > 5:
        g = 1
    else: 
        g = 2
    if request.method == 'GET':
        cc = models.Coment.objects.filter(article=a).order_by('-date')
        cc = cc[0:5]
        p = 1
        if p == 1:
            print('HI')
    else:
        p = 0
        cc = models.Coment.objects.filter(article=a).order_by('-date')
    if id != 999:
        u = PersonalCustomUser.objects.get(id=id)
        a = models.Article.objects.get(id=pk)
        c = models.Coment.objects.filter(author=u , article=a)
        if len(c) >= 2:
            t = 1
            context = {'article' : a , 't' : t , 'com' : cc, 'u' : u , 'g' : g , 'p' : p}
        else:
            if request.method != 'POST':
                form = forms.ComentForm()
            else:
                form = forms.ComentForm(data = request.POST)
                if form.is_valid():
                    new_comment = form.save(commit=False)
                    new_comment.article = a
                    new_comment.author = u
                    new_comment.save()
                    return redirect('detail_newspaper' ,pk , id)
            context = {'article' : a , 'form' : form , 'com' : cc , 'u' : u , 'come' : ccc , 'g' : g , 'p' : p }
        return render(request , 'detail_newspaper.html' , context)
    else:
        t = 2
        if t == 2:
            print('ssss')
        a = models.Article.objects.get(id=pk)
        context = {'article' : a , 't' : t , 'com' : cc , 'come' : ccc , 'g' : g, 'p' : p }
        return render(request , 'detail_newspaper.html' , context)

class NewspaperCreateView(LoginRequiredMixin , CreateView):
    model = models.Article
    fields = ['title' , 'body' , 'description'  , 'company' ]
    template_name = 'newspaper_create.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NewspaperUpdateView(LoginRequiredMixin , UpdateView):
    model = models.Article
    template_name = 'newspaper_update.html'
    fields = ['title' , 'body' , 'description' , 'author' , 'company']
    model = models.Article

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class NewspaperDeleteView(LoginRequiredMixin , DeleteView):
    template_name = 'newspaper_delete.html'
    success_url = reverse_lazy('newspaper_list_view')
    model = models.Article

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class CompanyListView(ListView):
    model = models.Company
    template_name = 'company_list.html'
    context_object_name = 'list'

class CompanyCreateView(LoginRequiredMixin , CreateView):
    model = models.Company
    fields = ['name' , 'description']
    template_name = 'company_create.html'

def coments(request , pk , id):
    u = PersonalCustomUser.objects.get(id=id)
    a = models.Article.objects.get(id=pk)
    c = models.Coment.objects.filter(author=u , article=a)
    if len(c) >= 2:
        t = 1
        context = {'a' : a , 't' : t}
    else:
        if request.method != 'POST':
            form = forms.ComentForm()
        else:
            form = forms.ComentForm(data = request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.article = a
                new_comment.author = u
                new_comment.save()
                return redirect('detail_newspaper' ,pk , id)
        context = {'a' : a , 'form' : form}
    return render(request , 'new_coment.html' , context)

def company_detail(request , pk):
    c = models.Company.objects.get(id=pk)
    cc = c.article_set.all()
    context = {'company' : c , 'cc' : cc}
    return render(request , 'company_detail.html' , context)

def about_us(request):
    return render(request , 'about_us.html')