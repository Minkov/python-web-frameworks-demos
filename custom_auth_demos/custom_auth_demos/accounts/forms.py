from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from custom_auth_demos.accounts.models import Profile

UserModel = get_user_model()


class AccountUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = '__all__'


class AccountUserCreationForm(auth_forms.UserCreationForm):
    age = forms.IntegerField()

    # Other fields of `Profile`

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
        # fields = auth_forms.UserCreationForm.Meta.fields + ("age",)

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            age=self.cleaned_data["age"],
        )

        if commit:
            profile.save()

        return user
