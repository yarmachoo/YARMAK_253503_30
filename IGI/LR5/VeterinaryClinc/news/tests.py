import datetime
from datetime import timezone

from django.test import TestCase

from news.models import Articles

class ArticleModelTest(TestCase):
    def setUp(self):
        self.article = Articles.objects.create(
            title="Тестовая статья",
            anons="Анонс тестовой статьи",
            full_text="Текст тестовой статьи",
            public_date=datetime.datetime.now()
        )

    def test_article_creation(self):
        self.assertTrue(isinstance(self.article, Articles))
        self.assertEqual(str(self.article), self.article.title)
