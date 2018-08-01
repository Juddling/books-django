from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=128)
    abstract = models.CharField(max_length=128, blank=True, null=True)
    author_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'