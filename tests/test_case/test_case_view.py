from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from articles.models import Articles
from articles.models import Categories
from articles.models import Comment


class TestModelArticle(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='fode', email='fode@gmail.com')
        self.user.set_password('12345')
        self.user.save()

        self.categories = Categories.objects.create(
            title='categorie 1', user=self.user)
        self.articles = Articles.objects.create(
            title='article 1',
            sumary='description',
            content='le contenu de mon article',
            categorie=self.categories,
            date_pub=timezone.now(),
            publiche=True,
            autor=self.user
        )

    def test_articles_categories(self):
        self.assertEqual(self.categories.title, 'categorie 1')
        self.assertEqual(self.articles.title, 'article 1')
        self.assertEqual(self.articles.sumary, 'description')
