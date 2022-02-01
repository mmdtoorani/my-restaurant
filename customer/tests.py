from django.test import TestCase
from .models import Customer, Address


class UserTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username='username1', password='user123456', phone_number="09124568585")
        Customer.objects.create(username='username2', password='user123456', phone_number="09364568585")
        customer1 = Customer.objects.get(username='username1')
        Address.objects.create(
            customer=customer1,
            address="naziabad, mashhadi, badaligivi, plake 54, tabaghe 3"
        )

    def test_user_create(self):
        user1 = Customer.objects.get(username="username1")
        user2 = Customer.objects.get(username="username2")
        self.assertEqual(user1.username, "username1")
        self.assertEqual(user2.phone_number, '09364568585')

    def test_address_create(self):
        self.assertEqual(
            "naziabad, mashhadi, badaligivi, plake 54, tabaghe 3",
            Address.objects.get(customer__username='username1').address
        )
