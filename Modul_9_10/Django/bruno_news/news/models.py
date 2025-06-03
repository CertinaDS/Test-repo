from django.db import models

class Article(models.Model):
    title = models.CharField("Загаоловок новости", max_length=64, unique=True)
    description = models.CharField("Описание новости", max_length=200)
    text = models.TrField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title
# Create your models here.
