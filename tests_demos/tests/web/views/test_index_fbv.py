# Creates a test database for each test
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class IndexFbvTests(TestCase):
    def test_index_fbv__what_can_be_tested(self):
        response = self.client.get(reverse("index_fbv"))
        context = response.context
        self.assertEqual("users.html", context.template_name)
        self.assertEqual(200, response.status_code)






    def test_index_fbv__when_no_users__expect_empty_user_list(self):
        response = self.client.get(reverse("index_fbv"))

        context = response.context
        user_list = context["user_list"]

        expected_user_list = []

        self.assertListEqual(expected_user_list, list(user_list))

    def test_index_fbv__when_single_user__expect_user_list_with_single_user(self):
        # Arrange
        user = UserModel.objects.create_user(username="test_user", password="1123QwER")

        # Act
        response = self.client.get(reverse("index_fbv"))

        # Assert
        context = response.context
        user_list = context["user_list"]

        expected_user_list = [user]

        self.assertListEqual(expected_user_list, list(user_list))

    def test_index_fbv__when_three_users__expect_user_list_with_three_users(self):
        # Arrange
        users = [
            UserModel.objects.create_user(username=f"test_user-{index}", password="1123QwER")
            for index in range(1, 4)
        ]

        # Act
        response = self.client.get(reverse("index_fbv"))

        # Assert
        context = response.context
        user_list = context["user_list"]

        expected_user_list = users

        self.assertListEqual(expected_user_list, list(user_list))
