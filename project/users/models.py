from django.db import models

# Create your models here.
class Post(models.Model):
    user_name=models.CharField(max_length=200,null=False)
    post_title=models.CharField(max_length=200)
    post_content=models.TextField(default='totorial content')
    date_published=models.DateField(blank=True,null=True)
    user_profilr_link=models.URLField(blank=True,null=True)
