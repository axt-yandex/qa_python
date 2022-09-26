from main import BooksCollector
from random import randint


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
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_same_book_twice_no_change_in_books_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        book_name = 'Гордость и предубеждение и зомби'
        # добавляем книгу и делаем копию словаря
        collector.add_new_book(book_name)
        rating_before_adding_same_book = collector.books_rating.copy()

        # добавляем ту же книгу и делаем вторую копию словаря
        collector.add_new_book(book_name)
        rating_after_adding_same_book = collector.books_rating.copy()

        # проверяем, что копии словарей идентичны
        assert rating_before_adding_same_book == rating_after_adding_same_book

    def test_set_book_rating_set_rating_non_existing_book_no_change_in_books_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги и сохраняем копию словаря
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        rating_before_changing_rating = collector.books_rating.copy()

        # пытаемся изменить рейтинг несуществующей книги и делаем вторую копию словаря
        collector.set_book_rating('Том и Джери', 5)
        rating_after_changing_rating = collector.books_rating.copy()

        # проверяем, что копии словарей идентичны
        assert rating_before_changing_rating == rating_after_changing_rating

    def test_set_book_rating_set_zero_rating_no_change_in_books_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        book_name = 'Гордость и предубеждение и зомби'
        # добавляем книгу и делаем копию словаря
        collector.add_new_book(book_name)
        rating_before_setting_zero_rating = collector.books_rating.copy()

        # пытаемся установить рейтинг = 0 и делаем вторую копию словаря
        collector.set_book_rating(book_name, 0)
        rating_after_setting_zero_rating = collector.books_rating.copy()

        # проверяем, что копии словарей идентичны
        assert rating_before_setting_zero_rating == rating_after_setting_zero_rating

    def test_get_book_rating_get_rating_receive_default_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        book_name = 'Гордость и предубеждение и зомби'
        # добавляем книгу
        collector.add_new_book(book_name)

        # проверяем что рейтинг = 1 (по умолчанию)
        assert collector.get_book_rating(book_name) == 1

    def test_get_book_rating_set_rating_7_receive_rating_7(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        book_name = 'Гордость и предубеждение и зомби'
        rating = 7
        # добавляем книгу и меняем рейтинг на 7
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rating)

        # проверяем что рейтинг = 7
        assert collector.get_book_rating(book_name) == 7

    def test_get_books_with_specific_rating_set_rating_7_receive_10_books(self, set_of_books_10x10):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем 10 наборов книг, в каждом наборе 10 книг с рейтингом от 1 до 10, итого 100 книг
        for book_name, rating in set_of_books_10x10:
            collector.add_new_book(book_name)
            collector.set_book_rating(book_name, rating)

        # проверяем что имеется 10 книг с рейтингом 7
        assert len(collector.get_books_with_specific_rating(7)) == 10

    def test_get_books_rating_add_100_books_function_return_instance_variable(self, set_of_books_with_random_rating):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем 100 книг со случайным рейтингом
        for book_name, rating in set_of_books_with_random_rating:
            collector.add_new_book(book_name)
            collector.set_book_rating(book_name, rating)

        # проверяем что функция возвращает тот же словарь, что хранится в переменной экземпляра
        assert collector.books_rating == collector.get_books_rating()

    def test_add_book_in_favorites_add_one_new_book_get_same_book_in_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        book_name_2 = 'Что делать, если ваш кот хочет вас убить'
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book(book_name_2)

        # добавляем вторую книгу в любимые
        collector.add_book_in_favorites(book_name_2)

        # проверяем, что вторая книга имеется в соответсвующей переменной экземпляра и только она
        assert book_name_2 in collector.favorites and len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_book_favorites_do_not_have_deleted_book(
            self, set_of_books_with_random_rating):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем 100 книг со случайным рейтингом
        # составляем список из названий 3 книг
        i = 0
        selected_books = []
        numbers_of_selected_books = [11, 33, 66]
        for book_name, rating in set_of_books_with_random_rating:
            collector.add_new_book(book_name)
            collector.set_book_rating(book_name, rating)

            if i in numbers_of_selected_books:
                selected_books.append(book_name)
            i += 1

        # добавить выбранные книги в любимые
        for name in selected_books:
            collector.add_book_in_favorites(name)

        # удаляем одну книгу из любимых
        deleted_book = selected_books.pop(1)
        collector.delete_book_from_favorites(deleted_book)

        # проверяем что любимые не содержать удалённую книгу и количество любимых книг = 2
        assert deleted_book not in collector.favorites and len(collector.favorites) == 2
