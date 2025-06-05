from django.test import TestCase
import pytest
# Create your tests here.
from django_tests.models import Author, Book
from tests.factories import BookFactory, AuthorFactory

@pytest.mark.django_db
def test_author_creation(sample_author):
    assert Author.objects.count() == 1
    assert sample_author.name == "J.K. Rowling"

@pytest.mark.django_db
def test_book_factory():
    book = BookFactory()
    assert Book.objects.count() == 1
    assert 50 <= book.pages <= 1000