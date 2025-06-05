import factory
from factory.django import DjangoModelFactory
from django_tests.models import Book, Author
from faker import Faker

fake = Faker()

class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.LazyAttribute(lambda x: fake.name()[:13])  # Генерируем имя и обрезаем до 13 символов
    birth_date = factory.Faker('date_of_birth', minimum_age=25, maximum_age=80)
    bio = factory.Faker('text', max_nb_chars=200)

class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    author = factory.SubFactory(AuthorFactory)
    publish_date = factory.Faker('date_between', start_date='-30y', end_date='today')
    isbn = factory.LazyAttribute(lambda x: fake.isbn13().replace("-", ""))  # Удаляем дефисы (останется 13 цифр)
    pages = factory.Faker('random_int', min=50, max=1000)
    rating = factory.Faker('pydecimal', left_digits=1, right_digits=1, positive=True, min_value=1, max_value=5)