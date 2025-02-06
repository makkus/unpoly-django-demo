from django.urls import path

from src.unpoly_app import views
from unpoly_app.views import AuthorView, BookDetailView

urlpatterns = [
    path("", views.home, name="home"),
    path("todo/", views.todo, name="todo"),
    path("authors/", views.author_list, name="author_list"),
    path("authors/<int:pk>/", AuthorView.as_view(), name="author_detail"),
    path("books/", views.book_list, name="book_list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("books/<int:pk>/edit/", views.book_edit, name="book_edit"),
]
