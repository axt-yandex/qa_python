import pytest
from random import randint


@pytest.fixture
def set_of_books_with_random_rating():
    number_of_books = 100
    ratings = [randint(1, 10) for _ in range(number_of_books)]
    names = [f'Книга номер {i} с рейтингом {rating}' for i, rating in enumerate(ratings)]
    return zip(names, ratings)


@pytest.fixture
def set_of_books_10x10():
    ratings = [i for i in range(1, 11)] * 10
    names = [f'Книга номер {i} с рейтингом {rating}' for i, rating in enumerate(ratings)]
    return zip(names, ratings)
