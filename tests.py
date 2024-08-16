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

    @pytest.mark.parametrize('dictionary', [{'Книга 1': 'Жанр 1', 'Книга 2': 'Жанр 2', 'Книга 3': 'Жанр 3'},
                                            {'Книга 1': '', 'Книга 2': 'Жанр 2', 'Книга 3': ''}])
    def test_get_books_genre_dict_consist_three_elem_return_this_dict_consist_three_elem(self, dictionary):
        collector = BooksCollector()
        collector.books_genre = dictionary
        assert collector.get_books_genre() == dictionary

    @pytest.mark.parametrize('name', ['К', 'Кн', 'КнигаКнигаКнигаКнига', 'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКниг',
                                      'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига'])
    # len(name) == 1, 2, 20, 39, 40
    def test_add_new_book_name_len_within_range_one_book_in_dict(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_books_genre() == {name: ''}

    @pytest.mark.parametrize('name', ['', 'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаК',
                                      'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига'])
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

    def test_set_book_genre_add_existing_genre_to_existing_book_one_book_with_genre_in_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Ужасы')
        assert collector.get_books_genre() == {'Война и мир': 'Ужасы'}

    def test_set_book_genre_add_non_existing_genre_to_existing_book_one_book_without_genre_in_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Роман')
        assert collector.get_books_genre() == {'Война и мир': ''}

    def test_set_book_genre_add_existing_genre_to_non_existing_book_empty_dict(self):
        collector = BooksCollector()
        collector.set_book_genre('Война и мир', 'Ужасы')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_add_non_existing_genre_to_non_existing_book_empty_dict(self):
        collector = BooksCollector()
        collector.set_book_genre('Война и мир', 'Роман')
        assert len(collector.get_books_genre()) == 0

    def test_get_book_genre_book_with_non_existing_genre_in_the_dict_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Роман')
        assert collector.get_book_genre('Война и мир') == ''

    def test_get_book_genre_book_with_existing_genre_in_the_dict_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Ужасы')
        assert collector.get_book_genre('Война и мир') == 'Ужасы'

    @pytest.fixture()
    def create_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Ужасы')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Тихий Дон')
        return collector

    def test_get_books_with_specific_genre_two_books_with_same_genre_list_with_two_names(self, create_book_genre):
        assert create_book_genre.get_books_with_specific_genre('Ужасы') == ['Война и мир', 'Сияние']

    def test_get_books_with_specific_genre_book_without_genre_empty_list(self, create_book_genre):
        assert create_book_genre.get_books_with_specific_genre('') == []

    def test_get_books_for_children_book_genre_consist_two_books_not_for_children_and_book_without_genre_empty_list(self, create_book_genre):
        assert create_book_genre.get_books_for_children() == []

    def test_get_books_for_children_book_genre_consist_one_book_for_children_list_with_one_name(self, create_book_genre):
        create_book_genre.add_new_book('Курочка ряба')
        create_book_genre.set_book_genre('Курочка ряба', 'Мультфильмы')
        assert create_book_genre.get_books_for_children() == ['Курочка ряба']

    def test_get_list_of_favorites_books_list_consist_two_books_return_this_list(self):
        collector = BooksCollector()
        collector.favorites = ['Книга 1', 'Книга 2']
        assert collector.get_list_of_favorites_books() == ['Книга 1', 'Книга 2']

    def test_add_book_in_favorites_add_two_different_books_two_books_in_list_favorites(self, create_book_genre):
        create_book_genre.add_book_in_favorites('Война и мир')
        create_book_genre.add_book_in_favorites('Тихий Дон')
        assert create_book_genre.get_list_of_favorites_books() == ['Война и мир', 'Тихий Дон']

    def test_add_book_in_favorites_add_non_existing_book_list_of_favorites_not_consist_this_name(self, create_book_genre):
        create_book_genre.add_book_in_favorites('Война и мир')
        create_book_genre.add_book_in_favorites('Тихий Дон')
        create_book_genre.add_book_in_favorites('Возвращение джедая')
        assert create_book_genre.get_list_of_favorites_books() == ['Война и мир', 'Тихий Дон']

    def test_add_book_in_favorites_add_already_added_book_list_of_favorites_consist_this_book_in_one_copy(self, create_book_genre):
        create_book_genre.add_book_in_favorites('Война и мир')
        create_book_genre.add_book_in_favorites('Тихий Дон')
        create_book_genre.add_book_in_favorites('Тихий Дон')
        assert create_book_genre.get_list_of_favorites_books() == ['Война и мир', 'Тихий Дон']

    def test_delete_book_from_favorites_delete_one_book_in_the_list_of_two_books_one_book_in_the_list(self, create_book_genre):
        create_book_genre.add_book_in_favorites('Война и мир')
        create_book_genre.add_book_in_favorites('Тихий Дон')
        create_book_genre.delete_book_from_favorites('Тихий Дон')
        assert create_book_genre.get_list_of_favorites_books() == ['Война и мир']

    def test_delete_book_from_favorites_delete_non_existing_book_in_the_list_of_two_books_two_books_in_the_list(self, create_book_genre):
        create_book_genre.add_book_in_favorites('Война и мир')
        create_book_genre.add_book_in_favorites('Тихий Дон')
        create_book_genre.delete_book_from_favorites('Возвращения джедая')
        assert create_book_genre.get_list_of_favorites_books() == ['Война и мир', 'Тихий Дон']