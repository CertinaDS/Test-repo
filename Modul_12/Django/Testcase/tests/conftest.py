import pytest
from datetime import date
from django_tests.models import Author


@pytest.fixture
def sample_author():
    return Author.objects.create(
        name="J.K. Rowling",
        birth_date=date(1965, 7, 31),
        bio="British author best known for the Harry Potter series."
    )

