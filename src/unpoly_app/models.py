from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.


class Author(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(100)]
    )

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse("author_edit", kwargs={"pk": self.pk})

    def num_books(self):
        return self.books.count()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publication_date = models.DateField()

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse("book_edit", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
