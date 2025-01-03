import pytest
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from articles.models import Articles
from articles.models import Categories
from articles.views import Article_detail
from articles.views import Article_view
from articles.views import Create_Article


@pytest.mark.django_db
def test_article_creation(article):
    assert article.title == 'Test Article'
    assert article.categorie.title == 'categorie 1'


@pytest.mark.django_db
def test_article_view(article, category, user):
    view = Articles.objects.create(
        title='Test Article 1',
        sumary='Test Summary',
        content='Test Content',
        categorie=category,
        date_pub=timezone.now(),
        publiche=True,
        autor=user,
    )
    assert view in Articles.objects.all()


@pytest.mark.django_db
def test_delete_view(category, user, client):
    client.force_login(user)
    delete_id = Articles.objects.create(
        title='Test delete',
        sumary='Test delete',
        content='Test Content delete',
        categorie=category,
        date_pub=timezone.now(),
        publiche=True,
        autor=user,
    )
    assert Articles.objects.filter(pk=delete_id.pk).exists(
    ), "L'article n'existe pas avant suppression"

    url = reverse('articles:delete_article', kwargs={'pk': delete_id.pk})
    response = client.post(url)

    assert response.status_code == 302, f'assertion 1 {response.status_code}'
    assert not Articles.objects.filter(id=delete_id.pk).exists(), 'assertion 2'
    assert response.url == reverse('articles:article_view')
    assert response.url == reverse('articles:article_view')
