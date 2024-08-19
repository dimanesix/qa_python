import pytest

from main import BooksCollector

@pytest.fixture()
def create_book_genre_one_book():
    collector = BooksCollector()
    collector.add_new_book('Война и мир')
    return collector
@pytest.fixture()
def create_book_genre_three_books():
    collector = BooksCollector()
    collector.add_new_book('Война и мир')
    collector.set_book_genre('Война и мир', 'Ужасы')
    collector.add_new_book('Сияние')
    collector.set_book_genre('Сияние', 'Ужасы')
    collector.add_new_book('Тихий Дон')
    return collector
