from django.test import TestCase

from testing_demos.web.forms import ProfileCreateForm


class ProfileCreateFormTests(TestCase):
    def test_profile_create_form_disabled_fields__when_all__expect_all_to_be_disabled(self):
        form = ProfileCreateForm()
        disabled_fields = {
            name: field.widget.attrs[ProfileCreateForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            ProfileCreateForm.disabled_attr_name,
            disabled_fields['name'],
        )
        self.assertEqual(
            ProfileCreateForm.disabled_attr_name,
            disabled_fields['age'],
        )
        self.assertEqual(
            ProfileCreateForm.disabled_attr_name,
            disabled_fields['egn'],
        )

    def test_profile_create_form_disabled_fields__when_name_is_disabled__expect_name_to_be_disabled(self):
        # monkey patching
        ProfileCreateForm.disabled_fields = ('name',)
        form = ProfileCreateForm()
        disabled_fields = {
            name: field.widget.attrs[ProfileCreateForm.disabled_attr_name]
            for name, field in form.fields.items()
            if ProfileCreateForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            ProfileCreateForm.disabled_attr_name,
            disabled_fields['name'],
        )
        self.assertEqual(1, len(disabled_fields))
