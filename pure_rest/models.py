from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    pubdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=68)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
