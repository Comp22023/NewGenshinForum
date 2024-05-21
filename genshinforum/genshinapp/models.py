from django.db import models
from ckeditor.fields import RichTextField
import datetime
from django.contrib.auth import get_user_model
# Create your models here.
class Themes(models.Model):
    id = models.BigAutoField(primary_key=True)
    themename = models.TextField()
    themecontent = RichTextField()
    themeimg = models.ImageField(upload_to='img/', blank=True, null=True)
    themeauthor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    class Meta():
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return self.themename

class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    commentcontent = RichTextField()
    comment_date = models.DateField(default=datetime.date.today, blank=True, null=True)
    commentimg = models.ImageField(upload_to='img/')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE, blank=True, null=True)