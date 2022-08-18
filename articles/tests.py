from django.test import TestCase
from django.utils.text import slugify

from .models import Article

class ArticleTesCase(TestCase):

    def setUp(self):
        self.number_of_articles = 5
        for i in range(0, 5):
            Article.objects.create(
                title='Hello World', content='somtehing else'
            )

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertTrue(qs.count(), 1)
    
    def test_hello_world_slug(self):
        obj = Article.objects.all().order_by('id').first()
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug, 'hello-world')


