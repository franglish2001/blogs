import pytest
from django.contrib.auth.models import User
from django.utils import timezone

from articles.models import Articles
from articles.models import Categories


@pytest.fixture
def user():
    user = User.objects.create_user(
        username='fode', email='fode@gmail.com', password='12345')
    return user


@pytest.fixture
def category(user):
    return Categories.objects.create(title='categorie 1', user=user)


@pytest.fixture
def article(user, category):
    return Articles.objects.create(
        title='Test Article',
        sumary='Test Summary',
        content='Test Content',
        categorie=category,
        date_pub=timezone.now(),
        publiche=True,
        autor=user,
    )
