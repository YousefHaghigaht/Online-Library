from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    age = models.PositiveSmallIntegerField()
    national_code = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    name = models.CharField(max_length=200)
    publication_year = models.PositiveSmallIntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')

    def __str__(self):
        return self.name


