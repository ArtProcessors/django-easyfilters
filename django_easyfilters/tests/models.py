from django.db import models


BINDING_CHOICES = [
    ('H', 'Hardback'),
    ('P', 'Paperback'),
    ('C', 'Cloth'),
]

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Book(models.Model):
    name = models.CharField(max_length=100)
    binding = models.CharField(max_length=2, choices=BINDING_CHOICES)
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_published = models.DateField()
    edition = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

