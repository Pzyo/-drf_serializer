from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE, null=True)
    authors = models.ManyToManyField(to='Author')
    def __str__(self):
        return self.title

    def dateFormat(self):
        return '2021-8-10'

class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    def __str__(self):
        return self.name
