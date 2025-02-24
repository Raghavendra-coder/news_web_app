from django.test import TestCase, Client
from unittest.mock import patch

class GetLatestNewsAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    @patch("news_web_app.views.get_latest_news")
    def test_get_latest_news(self, mock_get_news):
        mock_get_news.return_value = [{"title": "Sample News", "content": "News Content"}]

        response = self.client.get("/news/get_latest_news/?country=us&language=en")
        self.assertTrue(response.json()["success"])
        self.assertEqual(len(response.json()["data"]), 1)


