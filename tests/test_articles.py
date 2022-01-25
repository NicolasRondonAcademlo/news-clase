import email
from multiprocessing.spawn import old_main_modules
from django.http import response
from rest_framework.test import APITestCase
from core.models import CustomUser
from django.contrib.auth.hashers import make_password
from articles.models import Article

class TestArticles(APITestCase):

    def setUp(self) -> None:
        self.host = 'http://127.0.0.1:8000'
        self.user = CustomUser.objects.create(
            email='testemail@example.com',
            password =make_password('contra2434')
        )
        response= self.client.post(f'{self.host}/api/token/',
        {
            'email':'testemail@example.com',
            'password': 'contra2434'
        }
        )
        self.auth = f'Bearer {response.data["access"]}'  
        self.user_two = CustomUser.objects.create(
            email='testemail2@example.com',
            password =make_password('contra2434')
        )
        response= self.client.post(f'{self.host}/api/token/',
        {
            'email':'testemail2@example.com',
            'password': 'contra2434'
        }
        )
        self.auth_two = f'Bearer {response.data["access"]}'  
        
        self.article = Article.objects.create(
            title="Gran Articulo",
            body="Esto es el articulo",
            auhtor=CustomUser.objects.get(id=self.user.id)
        )


    def test_add_article(self):
        response = self.client.post(
            f'{self.host}/api/v1/articles/',
            {
                "title": "Articulo desde un test",
                "body": "mucho texto",
                "auhtor": self.user.id
            }
        )
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "Articulo desde un test")

    def test_only_owner_can_edit(self):
        response = self.client.put(
            f'{self.host}/api/v1/articles/{self.article.id}/',
                {
                "title": "Articulo edidato",
                "body": "mucho texto",
                "auhtor": self.user.id
            },
            HTTP_AUTHORIZATION=self.auth_two
        )
        print(response)
        self.assertEqual(response.status_code,403)