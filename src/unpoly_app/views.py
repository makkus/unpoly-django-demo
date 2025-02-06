import time

from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from django_tables2 import RequestConfig

from unpoly_app.forms import BookEditForm
from unpoly_app.models import Author, Book
from unpoly_app.tables import AuthorTable, BookTable, BookFilter


# Create your views here.
def home(request):

    return render(request, "index.html")


def todo(request):
    return render(request, "todo.html")


def author_list(request):

    authors = Author.objects.all().annotate(num_books=Count("books"))

    authors_table = AuthorTable(authors, prefix="authors-")

    RequestConfig(request, paginate={"per_page": 5}).configure(authors_table)

    context = {
        "authors": authors,
        "authors_table": authors_table,
    }

    return render(request, "author_list.html", context)


def book_list(request):

    books = Book.objects.all()

    books_filtered = BookFilter(request.GET, queryset=books)
    books_table = BookTable(books_filtered.qs, prefix="books-")

    RequestConfig(request, paginate={"per_page": 5}).configure(books_table)

    context = {"books": books, "books_table": books_table, "filter": books_filtered}

    return render(request, "books_list.html", context)


def author_edit(request, pk):

    author = Author.objects.get(pk=pk)
    pass


def book_detail(request, pk):

    book = Book.objects.get(pk=pk)
    pass


def book_edit(request, pk):

    book = Book.objects.get(pk=pk)

    if request.method == "POST":
        form = BookEditForm(request.POST, instance=book)
        print("EDIT")
        if "cancel" in request.POST:
            print("CANCEL")
        elif "save" in request.POST:
            print("SAVE")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("book_detail", args=[book.pk]))

    else:
        form = BookEditForm(instance=book)

    context = {"form": form, "book": book}
    return render(request, "cotton/book_edit.html", context)


class AuthorView(DetailView):

    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        time.sleep(2)

        books = Book.objects.filter(author=self.object)
        books_table = BookTable(books, prefix="books-")
        RequestConfig(self.request, paginate={"per_page": 5}).configure(books_table)
        context["books_table"] = books_table
        return context


class BookDetailView(DetailView):

    model = Book
