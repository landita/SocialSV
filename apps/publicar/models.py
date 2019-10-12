import os;
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Publicaciones(models.Model):
    titulo          = models.CharField(max_length=100, null=False)
    descripcion     = RichTextUploadingField(external_plugin_resources=[(
        'youtube',
        '/static/scripts/ckeditor-youtube-plugin/youtube/',
        'plugin.js'
    )],)
    categoria       = models.CharField(max_length=100, null=False)
    fechaRegistro   = models.DateField(auto_now=False, auto_now_add=True, blank=True, null=True)
    estado          = models.BooleanField(null=True, default=False)
    autor           = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
