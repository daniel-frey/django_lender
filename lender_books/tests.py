from django.test import TestCase, RequestFactory
from .models import Book

class TestBookModel(TestCase):
    """
    """
    def setUp(self):
        """
        """
        Book.objects.create(author='Jim', title='Feed the cat', detail='the cat is hungry', status='available')
        Book.objects.create(author='Bob', title='Feed the dog', detail='the dog is hungry', status='available')
        Book.objects.create(author='Joe', title='Feed the fish', detail='the fish is hungry', status='out')


    # def setUpClass(cls):
    #     """
    #     """
    #     pass


    def test_book_titles(self):
        """
        """
        one = Book.objects.get(title='Feed the cat')
        self.assertEqual(one.title, 'Feed the cat')


    def test_book_description(self):
        """
        """
        books = Book.objects.all()
        self.assertEqual(books[2].detail, 'the fish is hungry')
        
    
    def test_book_status(self):
        """
        """
        one = Book.objects.get(title='Feed the cat')
        two = Book.objects.get(title='Feed the dog')
        self.assertEqual(one.status, 'available')
        self.assertEqual(two.status, 'available')

    
    def test_create_new_book(self):
        """
        """
        new_book = Book.objects.create(title='new', detail='')
        self.assertEqual(new_book.title, 'new')


class TestBookViews(TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.request = RequestFactory()

        self.book = Book.objects.create(title='Feed the cat', detail='the cat is hungry', status='available')
        Book.objects.create(title='Feed the dog', detail='the dog is hungry', status='available')
        Book.objects.create(title='Feed the fish', detail='the fish is hungry', status='out')


    def test_list_view_context(self):
        """
        """
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertIn(b'Feed the cat', response.content)


    def test_list_view_status(self):
        """
        """
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertEqual(200, response.status_code)


    def test_detail_view_context(self):
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, self.book.id)
        self.assertIn(b'the cat is hungry', response.content)

    
    def test_detail_view_status_code_failure(self):
        """
        """
        from .views import book_detail_view
        from django.http import Http404
        request = self.request.get('')

        with self.assertRaises(Http404):
            book_detail_view(request, '0')

    