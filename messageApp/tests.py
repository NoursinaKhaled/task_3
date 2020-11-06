from django.test import TestCase
from .models import Post
from django.urls  import reverse

# Create your tests here.
class PostModelTest (TestCase):
    def setUp(self):
        Post.objects.create(text = "just test")

    def test_text_context(self):
        post = Post.objects.get(id=1)
        expected_text = post.text
        self.assertEqual(expected_text,"just test")

class HomeViewTest (TestCase):
    def setUp(self):
        Post.objects.create(text = "Home page test")

    def test_view_url_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code,200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code,200)

    def test_view_url_uses_template(self):
        resp = self.client.get(reverse("home"))
        self.assertTemplateUsed(resp,"home.html") 


