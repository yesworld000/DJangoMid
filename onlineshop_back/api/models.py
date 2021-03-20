from django.db import models
import sqlite3



class BookJournalBase(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    price = models.FloatField(default=0)
    created_at = models.DateField


class Book(models.Model):
    num_pages = models.FloatField(default=0)
    genre = models.CharField(max_length=200)
    book = models.ForeignKey(BookJournalBase, null=True, on_delete=models.CASCADE)

class Journal(models.Model):
    type_ = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200, default='no pubisher')
    journal = models.ForeignKey(BookJournalBase, null=True, on_delete=models.CASCADE)