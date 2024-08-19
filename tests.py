import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('dictionary', [{'Книга 1': 'Жанр 1', 'Книга 2': 'Жанр 2', 'Книга 3': 'Жанр 3'},
                                            {'Книга 1': '', 'Книга 2': 'Жанр 2', 'Книга 3': ''}])
    def test_get_books_genre_return_this_dict(self, dictionary):
        collector = BooksCollector()
        collector.books_genre = dictionary
        assert collector.get_books_genre() == dictionary

    @pytest.mark.parametrize('name', ['К', 'Кн', 'КнигаКнигаКнигаКнига', 'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКниг',
                                      'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига'])
    def test_add_new_book_name_len_within_range(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_books_genre() == {name: ''}

    @pytest.mark.parametrize('name', ['', 'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаК',
                                      'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига'])
    def test_add_new_book_name_len_out_of_range(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_book_is_already_in_dictionary(self, create_book_genre_one_book):
        create_book_genre_one_book.add_new_book('Война и мир')
        assert create_book_genre_one_book.get_books_genre() == {'Война и мир': ''}

    def test_set_book_genre_add_existing_genre_to_existing_book(self, create_book_genre_one_book):
        create_book_genre_one_book.set_book_genre('Война и мир', 'Ужасы')
        assert create_book_genre_one_book.get_books_genre() == {'Война и мир': 'Ужасы'}

    def test_set_book_genre_add_non_existing_genre_to_existing_book(self, create_book_genre_one_book):
        create_book_genre_one_book.set_book_genre('Война и мир', 'Роман')
        assert create_book_genre_one_book.get_books_genre() == {'Война и мир': ''}

    def test_set_book_genre_add_existing_genre_to_non_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Война и мир', 'Ужасы')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_add_non_existing_genre_to_non_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Война и мир', 'Роман')
        assert len(collector.get_books_genre()) == 0

    def test_get_book_genre_book_with_non_existing_genre_in_the_dict(self, create_book_genre_one_book):
        create_book_genre_one_book.set_book_genre('Война и мир', 'Роман')
        assert create_book_genre_one_book.get_book_genre('Война и мир') == ''

    def test_get_book_genre_book_with_existing_genre_in_the_dict(self, create_book_genre_one_book):
        create_book_genre_one_book.set_book_genre('Война и мир', 'Ужасы')
        assert create_book_genre_one_book.get_book_genre('Война и мир') == 'Ужасы'

    def test_get_books_with_specific_genre_check_two_books_with_same_genre(self, create_book_genre_three_books):
        assert create_book_genre_three_books.get_books_with_specific_genre('Ужасы') == ['Война и мир', 'Сияние']

    def test_get_books_with_specific_genre_check_book_without_genre(self, create_book_genre_three_books):
        assert create_book_genre_three_books.get_books_with_specific_genre('') == []

    def test_get_books_for_children_check_two_books_not_for_children_and_book_without_genre(self, create_book_genre_three_books):
        assert create_book_genre_three_books.get_books_for_children() == []

    def test_get_books_for_children_check_one_book_for_children(self, create_book_genre_three_books):
        create_book_genre_three_books.add_new_book('Курочка ряба')
        create_book_genre_three_books.set_book_genre('Курочка ряба', 'Мультфильмы')
        assert create_book_genre_three_books.get_books_for_children() == ['Курочка ряба']

    def test_get_list_of_favorites_books_list_consist_two_books(self):
        collector = BooksCollector()
        collector.favorites = ['Книга 1', 'Книга 2']
        assert collector.get_list_of_favorites_books() == ['Книга 1', 'Книга 2']

    def test_add_book_in_favorites_add_two_different_books(self, create_book_genre_three_books):
        create_book_genre_three_books.add_book_in_favorites('Война и мир')
        create_book_genre_three_books.add_book_in_favorites('Тихий Дон')
        assert create_book_genre_three_books.get_list_of_favorites_books() == ['Война и мир', 'Тихий Дон']

    def test_add_book_in_favorites_add_non_existing_book(self, create_book_genre_three_books):
        create_book_genre_three_books.add_book_in_favorites('Война и мир')
        create_book_genre_three_books.add_book_in_favorites('Тихий Дон')
        create_book_genre_three_books.add_book_in_favorites('Возвращение джедая')
        assert create_book_genre_three_books.get_list_of_favorites_books() == ['Война и мир', 'Тихий Дон']

    def test_add_book_in_favorites_add_already_added_book(self, create_book_genre_three_books):
        create_book_genre_three_books.add_book_in_favorites('Война и мир')
        create_book_genre_three_books.add_book_in_favorites('Тихий Дон')
        create_book_genre_three_books.add_book_in_favorites('Тихий Дон')
        assert create_book_genre_three_books.get_list_of_favorites_books() == ['Война и мир', 'Тихий Дон']

    def test_delete_book_from_favorites_delete_one_book_in_the_list(self, create_book_genre_three_books):
        create_book_genre_three_books.add_book_in_favorites('Война и мир')
        create_book_genre_three_books.add_book_in_favorites('Тихий Дон')
        create_book_genre_three_books.delete_book_from_favorites('Тихий Дон')
        assert create_book_genre_three_books.get_list_of_favorites_books() == ['Война и мир']

    def test_delete_book_from_favorites_delete_non_existing_book(self, create_book_genre_three_books):
        create_book_genre_three_books.add_book_in_favorites('Война и мир')
        create_book_genre_three_books.add_book_in_favorites('Тихий Дон')
        create_book_genre_three_books.delete_book_from_favorites('Возвращения джедая')
        assert create_book_genre_three_books.get_list_of_favorites_books() == ['Война и мир', 'Тихий Дон']