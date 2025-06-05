from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=13)
    birth_date = models.DateField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=13)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField()
    isbn = models.CharField(max_length=17, unique=True)
    pages = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.title} by {self.author.name}"
