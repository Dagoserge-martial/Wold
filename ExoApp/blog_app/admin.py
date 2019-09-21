# vim: set fileencoding=utf-8 :
from django.contrib import admin
from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register
from django.utils.safestring import mark_safe

from . import models

@register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user_id',
        'nom',
        'date_add',
        'date_update',
        'statut',
    )
    list_filter = (
        'user_id',
        'date_add',
        'date_update',
        'statut',
        'id',
        'user_id',
        'nom',
        'date_add',
        'date_update',
        'statut',
    )

@register(models.Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'affiche_image',
        'id',
        'categorie_id',
        'auteur',
        'titre',
        'article_acueil',
        'statut',
        'image_cat',
        'image_detail',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'categorie_id',
        'auteur',
        'date_add',
        'date_upd',
        'statut',
        'id',
        'categorie_id',
        'auteur',
        'titre',
        'date_add',
        'date_upd',
        'statut',
        'image_cat',
        'image_detail',
    )
    def affiche_image(self, obj):
        return mark_safe('<img src = " {url} " width = " 100px " heigth = " 50px " />'.format(url= obj.image_cat.url))

    raw_id_fields = ('tag_id',)

@register(models.Commentaire)
class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'contenue',
        'date_add',
        'date_upd',
        'statut',
        'article_id',
    )
    list_filter = (
        'user',
        'date_add',
        'date_upd',
        'statut',
        'article_id',
        'id',
        'user',
        'contenue',
        'date_add',
        'date_upd',
        'statut',
        'article_id',
    )

@register(models.Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom')
    list_filter = ('id', 'nom')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Tag, TagAdmin)
