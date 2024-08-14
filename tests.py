import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name', ['К', 'Кн', 'КнигаКнигаКнигаКнига', 'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКниг', 'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига'])
    # len(name) == 1, 2, 20, 39, 40
    def test_add_new_book_name_len_within_range_one_book_in_dict(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_books_genre() == {name:''}

    @pytest.mark.parametrize('name', ['', 'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаК', 'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига'])
    # len(name) == 0, 41, ∞
    def test_add_new_book_name_len_out_of_range_empty_dict(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_book_name_is_already_in_dictionary_one_book_in_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert collector.get_books_genre() == {'Война и мир': ''}