# Import necessary modules from Django
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, Post

# Define a test class for Category model
class CategoryModelTest(TestCase):

    # Set up the test environment by creating a Category instance
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    # Test that the Category name attribute is as expected
    def test_category_name(self):
        self.assertEqual(str(self.category), 'Test Category')

# Define a test class for Post model
class PostModelTest(TestCase):

    # Set up the test environment by creating a User, Category, and Post instance
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')
        self.post = Post.objects.create(title='Test post', content='This is a test post', author=self.user, category=self.category)

    # Test that the Post title attribute is as expected
    def test_post_title(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        self.assertEqual(expected_title, 'Test post')

    # Test that the Post content attribute is as expected
    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_content = f'{post.content}'
        self.assertEqual(expected_content, 'This is a test post')

    # Test that the Post author attribute is as expected
    def test_post_author(self):
        post = Post.objects.get(id=1)
        expected_author = f'{post.author}'
        self.assertEqual(expected_author, 'testuser')

    # Test that the Post category attribute is as expected
    def test_post_category(self):
        post = Post.objects.get(id=1)
        expected_category = f'{post.category}'
        self.assertEqual(expected_category, 'Test Category')

    # Test that the Post views attribute is as expected
    def test_post_views(self):
        post = Post.objects.get(id=1)
        expected_views = f'{post.views}'
        self.assertEqual(expected_views, '0')

    # Test the Post list view by making a request to the blog-home URL and checking the response
    def test_post_list_view(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test post')
