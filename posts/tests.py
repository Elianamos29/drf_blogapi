from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "testuser",
            email = "testuser@gmail.com",
            password = "secret",
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = "dope title",
            body = "The body",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "dope title")
        self.assertEqual(self.post.body, "The body")
        self.assertEqual(str(self.post), "dope title")
