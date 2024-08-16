# qa_python

<h3>В проект добавлены следующие проверки</h3>
1) **test_add_new_book_add_two_books** <p>
   <u>Описание:</u> тест, который проверяет добавление двух книг в словарь _books_genre_ <br></br>
2) **test_get_books_genre_dict_consist_three_elem_return_this_dict_consist_three_elem** <p>
   <u>Описание:</u> тест, который проверяет корректное получение словаря с книгами _books_genre_ <br></br>
3) **test_add_new_book_name_len_within_range_one_book_in_dict** <p>
    <u>Описание:</u> тест, который проверяет добавление книги с корректной длиной названия <br></br>
4) **test_add_new_book_name_len_out_of_range_empty_dict** <p>
    <u>Описание:</u> тест, который проверяет добавление книги с некорректной длиной названия <br></br>
5) **test_add_new_book_book_name_is_already_in_dictionary_one_book_in_dict** <p>
    <u>Описание:</u> тест, который проверяет добавление уже находящейся в словаре _books_genre_ книги <br></br>
6) **test_set_book_genre_add_existing_genre_to_existing_book_one_book_with_genre_in_dict** <p>
    <u>Описание:</u> тест, который проверяет добавление известного жанра к существующей книги в словаре _books_genre_ <br></br>
7) **test_set_book_genre_add_non_existing_genre_to_existing_book_one_book_without_genre_in_dict** <p>
    <u>Описание:</u> тест, который проверяет невозможность установления к существующей в словаре _books_genre_ книги неизвестного жанра <br></br>
8) **test_set_book_genre_add_existing_genre_to_non_existing_book_empty_dict** <p>
    <u>Описание:</u> тест, который проверяет невозможность установления к несуществующей в словаре _books_genre_ книги известного жанра <br></br>
9) **test_set_book_genre_add_non_existing_genre_to_non_existing_book_empty_dict** <p>
    <u>Описание:</u> тест, который проверяет невозможность установления к существующей в словаре _books_genre_ книги неизвестного жанра <br></br>
10) **test_get_book_genre_book_with_non_existing_genre_in_the_dict_empty_genre** <p>
    <u>Описание:</u> тест, который проверяет получение жанра книги, для книги с неизвестным жанром <br></br>
11) **test_get_book_genre_book_with_existing_genre_in_the_dict_existing_genre** <p>
    <u>Описание:</u> тест, который проверяет получение жанра книги, для книги с известным жанром <br></br>
12) **test_get_books_with_specific_genre_two_books_with_same_genre_list_with_two_names** <p>
    <u>Описание:</u> тест, который проверяет получение списка книг одинакового жанра <br></br>
13) **test_get_books_with_specific_genre_book_without_genre_empty_list** <p>
    <u>Описание:</u> тест, который проверяет невозможность получения списка книг, для которых отсутствует жанр <br></br>
14) **test_get_books_for_children_book_genre_consist_two_books_not_for_children_and_book_without_genre_empty_list** <p>
    <u>Описание:</u> тест, который проверяет полчение списка книг для детей в случае, если в словаре находятся только книги для взрослых или книги с отсутствующим жанром <br></br>
15) **test_get_books_for_children_book_genre_consist_one_book_for_children_list_with_one_name** <p>
    <u>Описание:</u> тест, который проверяет полчение списка книг для детей в случае, если в словаре содержится одна книга подходящего жанра <br></br>
16) **test_get_list_of_favorites_books_list_consist_two_books_return_this_list** <p>
    <u>Описание:</u> тест, который проверяет корректное получение списка любимых книг <br></br>
17) **test_add_book_in_favorites_add_two_different_books_two_books_in_list_favorites** <p>
    <u>Описание:</u> тест, который проверяет добавление двух имеющихся в словаре _books_genre_ книг в список любимых книг <br></br>
18) **test_add_book_in_favorites_add_non_existing_book_list_of_favorites_not_consist_this_name** <p>
    <u>Описание:</u> тест, который проверяет невозможность добавления отсутствующей в словаре _books_genre_ книги в список любимых книг <br></br>
19) **test_add_book_in_favorites_add_already_added_book_list_of_favorites_consist_this_book_in_one_copy** <p>
    <u>Описание:</u> тест, который проверяет невозможность добавления уже добавленной книги в список любимых книг <br></br>
20) **test_delete_book_from_favorites_delete_one_book_in_the_list_of_two_books_one_book_in_the_list** <p>
    <u>Описание:</u> тест, который проверяет удаление из списка любимых книг существующей книги <br></br>
21) **test_delete_book_from_favorites_delete_non_existing_book_in_the_list_of_two_books_two_books_in_the_list** <p>
    <u>Описание:</u> тест, который проверяет невозможность удаления несуществующей книги из списка любимых книг <br></br>