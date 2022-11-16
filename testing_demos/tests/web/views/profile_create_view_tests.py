from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

from testing_demos.web.models import Profile
from tests.common.base_test_case import BaseTestCase

UserModel = get_user_model()


class ProfileCreateViewTests(BaseTestCase):
    def test_create_profile__when_user_is_loggedin__expect_to_create_profile(self):
        profile_data = {
            'name': 'Doncho',
            'age': 19,
            'egn': 1234567890,
        }
        credentials = {
            'username': 'doncho',
            'password': 'doncho123',
        }

        self.create_and_login_user(**credentials)

        response = self.client.post(
            reverse('create profile'),
            data=profile_data,
        )

        created_profile = Profile.objects.filter(**profile_data) \
            .get()

        self.assertIsNotNone(created_profile)
        self.assertEqual(302, response.status_code)

    def test_create_profile__when_anonymous_user__expect_to_redirect_to_login(self):
        profile_data = {
            'name': 'Doncho',
            'age': 19,
            'egn': 1234567890,
        }

        response = self.client.post(
            reverse('create profile'),
            data=profile_data,
        )
        self.assertEqual(302, response.status_code)
        expected_redirect_url = f'{settings.LOGIN_URL}?next={reverse("create profile")}'
        self.assertEqual(expected_redirect_url, response.headers.get('Location'))
