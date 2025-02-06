from crispy_forms.helper import FormHelper
from crispy_tailwind.layout import Submit
from django.forms import ModelForm

from unpoly_app.models import Book


class BookEditForm(ModelForm):

    class Meta:
        model = Book
        fields = ["title", "author", "publication_date"]
