from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model

class Company(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('company_list')

class Article(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    description = models.CharField(max_length=300)
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newspaper_list_view')

class Coment(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    comment = models.CharField(max_length=400 , null=True)
    date = models.DateTimeField(auto_now_add=True ,  null=True)

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('newspaper_list_view')
    

    

