from django.db import models

class Article(models.Model):
    DRAFT = "На модерации"
    PUBLISH = "Готоо к публикации"
    INACTIVE = "Неактивная"

    class Status(models.TextChoices):
        DRAFT = "draft", "На модерации"
        PUBLISH = "publish", "Готоо к публикации"
        INACTIVE = "inactive", "Неактивная"

    author = models.ForeignKey('users.User', related_name='article', on_delete=models.SET_NULL, null=True, default=None)

    title = models.CharField("Загаоловок новости", max_length=64, unique=True)
    description = models.CharField("Описание новости", max_length=200)
    text = models.TextField()
    status = models.CharField(max_length=8, choices=Status.choices, default=Status.DRAFT)

    pub_date = models.DateTimeField("Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
