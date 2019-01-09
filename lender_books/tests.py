from django.test import TestCase, RequestFactory
from .models import Book
from django.contrib.auth.models import User


class TestBookModel(TestCase):
    """
    """
    def setUp(self):
        """Test the setup function, create books, and a user account.
        """
        user = User.objects.create_user('scott', 'im@yourhouse.com', 'mypassw0rd')

        Book.objects.create(author='Jim', title='Feed the cat', detail='the cat is hungry', status='available', user=user)
        Book.objects.create(author='Bob', title='Feed the dog', detail='the dog is hungry', status='available', user=user)
        Book.objects.create(author='Joe', title='Feed the fish', detail='the fish is hungry', status='out', user=user)

    def test_book_titles(self):
        """Test that the book title matches the input title
        """
        one = Book.objects.get(title='Feed the cat')
        self.assertEqual(one.title, 'Feed the cat')

    def test_book_description(self):
        """Test that the book detail matches that which was given
        """
        books = Book.objects.all()
        self.assertEqual(books[2].detail, 'the fish is hungry')

    def test_book_status(self):
        """Test that the books have correct status
        """
        one = Book.objects.get(title='Feed the cat')
        two = Book.objects.get(title='Feed the dog')
        self.assertEqual(one.status, 'available')
        self.assertEqual(two.status, 'available')

    def test_create_new_book(self):
        """Test to create a new book with only a title
        """
        new_book = Book.objects.create(title='new', detail='')
        self.assertEqual(new_book.title, 'new')


class TestBookViews(TestCase):
    """Test the book views page
    """
    def setUp(self):
        self.request = RequestFactory()
        """Test the setup of the books view page including new books and user
        """
        user = User.objects.create_user('scott', 'im@yourhouse.com', 'mypassw0rd')

        self.book = Book.objects.create(title='Feed the cat', detail='the cat is hungry', status='available', user=user)
        Book.objects.create(title='Feed the dog', detail='the dog is hungry', status='available', user=user)
        Book.objects.create(title='Feed the fish', detail='the fish is hungry', status='out', user=user)

    def test_list_view_context(self):
        """Test that the list view shows the correct context
        """
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertIn(b'Feed the cat', response.content)

    def test_list_view_status(self):
        """Test that the status is correct for the assigned book
        """
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertEqual(200, response.status_code)

    def test_detail_view_context(self):
        """Test that the book detail view is correct
        """
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, self.book.id)
        self.assertIn(b'the cat is hungry', response.content)

    def test_detail_view_status_code_failure(self):
        """Test that the status code of 404 is received
        """
        from .views import book_detail_view
        from django.http import Http404
        request = self.request.get('')
        with self.assertRaises(Http404):
            book_detail_view(request, '0')
