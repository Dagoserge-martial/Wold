from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
# Create your models here.


class Categorie (models.Model):
    user_id =  models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'categorie_user',)
    nom = models.CharField ( max_length = 255 )
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )

    def __str__(self):
        return self.nom

class Article (models.Model):
    categorie_id = models.ForeignKey(Categorie, on_delete = models.CASCADE, related_name = 'categorie_post',)
    tag_id = models.ManyToManyField('Tag')
    description = models.TextField(null=True)
    article_acueil = models.BooleanField ( default = False )
    content = HTMLField('Content')
    auteur = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'article_user',)
    titre = models.CharField ( max_length = 255 )
    date_add = models.DateTimeField ( auto_now_add = True )
    date_upd = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )
    image_cat = models.ImageField( blank = True, upload_to = 'post' )
    image_detail = models.ImageField( blank = True, upload_to = 'post' )

class Commentaire (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'Commentair_user',)
    contenue = models.CharField(max_length=225)
    date_add = models.DateTimeField ( auto_now_add = True )
    date_upd = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )
    article_id = models.ForeignKey(Article, on_delete = models.CASCADE, related_name = 'article',)

class Tag (models.Model):
    nom = models.CharField ( max_length = 255 )

#python manage.py admin_generator blog_app >> blog_app/admin.py
