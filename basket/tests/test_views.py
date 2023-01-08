from django.test import  TestCase
from django.urls import reverse


class BasketPageTest(TestCase):
    def test_basket_page(self):
        url = reverse('basket_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Добро пожаловать в этот чудесный магазин")


class BasketTest(TestCase):
    def test_basket_exists_at_desiret_location(self):
        response = self.client.get('/basket_detail/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket_detail.html')

