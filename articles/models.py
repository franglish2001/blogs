from django.db import models
from django.contrib.auth.models import User


class Articles(models.Model):
    title = models.CharField(max_length=100, blank=False,verbose_name='titre')
    sumary = models.CharField(max_length=250,blank=True,verbose_name='resumer')
    content = models.TextField(blank=False,verbose_name='contenu')
    categorie = models.ForeignKey('Categories',on_delete=models.PROTECT)
    date_pub = models.DateField(verbose_name='date de publication')
    publiche = models.BooleanField(default=False,verbose_name='publier')
    imagearticle = models.ImageField(upload_to='article_image',null=True,blank=True)
    autor = models.ForeignKey(User,on_delete=models.PROTECT)
    def __str__(self):
        return self.title
    
class Categories(models.Model):
    title = models.CharField(max_length=100,verbose_name='titre')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    article = models.ForeignKey(Articles,on_delete=models.CASCADE)
    date_comment = models.DateField(auto_now_add=True)