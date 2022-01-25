from rest_framework.test import APITestCase

class UsersTest(APITestCase):
    def setUp(self) -> None:
        self.host = 'http://127.0.0.1:8000'
 
    def test_register(self):
        response = self.client.post(
            f'{self.host}/api/v1/core/register/',
            {
                "email": "test_user@email.com",
                "password":"contra232"
            }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["email"],"test_user@email.com")