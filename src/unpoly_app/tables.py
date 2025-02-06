from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import format_html
from django_filters import FilterSet
from django_tables2 import Table
from django import forms
from unpoly_app.models import Author, Book
from django_filters import CharFilter


class AuthorTable(Table):

    class Meta:
        model = Author
        template_name = "tables/table.html"
        sequence = ("last_name", "first_name", "age", "num_books")
        fields = ["first_name", "last_name", "age", "num_books"]

    def render_last_name(self, record):

        return render_to_string("cotton/author_link.html", context={"author": record})


class BookFilter(FilterSet):
    title = CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        widget=forms.Select(attrs={"class": "select select-bordered w-full"}),
    )

    class Meta:
        model = Book
        fields = ["author", "title"]


class BookTable(Table):

    class Meta:
        model = Book
        template_name = "tables/table.html"
        fields = ["title", "author", "publication_date"]
        attrs = {"td": {"class": "whitespace-nowrap"}}

    def render_author(self, record):
        return format_html(
            "<a href='{}' class='link'>{}</a>".format(
                record.author.get_absolute_url(), record.author.full_name
            )
        )

    def render_title(self, record):

        return render_to_string("cotton/book_link.html", context={"book": record})
