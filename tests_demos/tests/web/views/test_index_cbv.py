# Creates a test database for each test
import http

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class IndexCbvTests(TestCase):

    # Completely useless test
    def test_index_fbv__when_anonymous_user__expect_not_authorized(self):
        response = self.client.get(reverse("index_cbv"))

        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, reverse("login") + "?next=" + reverse("index_cbv"))

    def test_index_fbv__when_single_user__expect_user_list_with_single_user(self):
        # Arrange
        user_data = {
            "username": "test_user",
            "password": "1123QwER",
        }

        user = UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)

        # Act
        response = self.client.get(reverse("index_cbv"))

        # Assert
        context = response.context
        user_list = context["user_list"]

        expected_user_list = [user]

        self.assertListEqual(expected_user_list, list(user_list))

    def test_index_cbv__when_three_users__expect_user_list_with_three_users(self):
        user_data = {
            "username": "atest_user",
            "password": "1123QwER",
        }

        # Arrange
        users = [
            UserModel.objects.create_user(username=f"test_user-{4 - index}", password="1123QwER")
            for index in range(1, 3)
        ]

        users.append(UserModel.objects.create_user(**user_data))

        self.client.login(**user_data)

        # Act
        response = self.client.get(reverse("index_cbv"))

        # Assert
        context = response.context
        user_list = context["user_list"]

        expected_user_list = sorted(users, key=lambda x: x.date_joined, reverse=True)

        self.assertListEqual(expected_user_list, list(user_list))
