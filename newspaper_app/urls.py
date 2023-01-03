from django.urls import path
from . import views
from user_app.models import PersonalCustomUser

urlpatterns = [
    path('' , views.NewspaperTemplateView.as_view() , name = 'index'),
    path('AllArticle/' , views.NewspapeprListView.as_view() , name = 'newspaper_list_view'),
    path('DetailArticle/<int:pk>/<int:id>/' , views.newspaper_detail_view , name = 'detail_newspaper'),
    path('CreateArcticle/' , views.NewspaperCreateView.as_view() , name = 'newspaper_create'),
    path('UpdateArticle/<int:pk>/' , views.NewspaperUpdateView.as_view() , name = 'newspaper_update'),
    path('DeleteArticle/<int:pk>/' , views.NewspaperDeleteView.as_view() ,  name = 'newspaper_delete'),
    path('CompanyList/' , views.CompanyListView.as_view() , name = 'company_list'),
    path('CompanyDetail/<int:pk>' , views.company_detail , name = 'company_detail'),
    path('CompanyCreate/' , views.CompanyCreateView.as_view() , name = 'company_create'),
    path('AddComents/<int:pk>/<int:id>/' , views.coments , name = 'comment'),
    path('About_us/' , views.about_us , name = 'about_us'),
]
