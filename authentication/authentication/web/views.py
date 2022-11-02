from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponse
from django.views import generic as views
from django.contrib.auth.models import User

from authentication.web.decorators import allow_groups


# Require `login` in function-based views
@login_required(login_url='/login')
def show_profile(request):
    return HttpResponse(f'Your are {request.user.username}')


# Require `login` in class-based views
class ProfileView(auth_mixins.LoginRequiredMixin, views.View):
    def get(self, request):
        return HttpResponse(f'Your are {request.user.username}')


# @allow_groups
@allow_groups(groups=['Users statistics'])
def index(request):
    print(
        authenticate(username='doncho', password='1123QwER'),
        authenticate(username='minkov', password='D0nch0!%123'),
        authenticate(username='minkov', password='D0nch03'),
        authenticate(username='donchominkov', password='d0n40minK00V'),
    )
    # new_user = User.objects.create_user(
    #     username='donchominkov',
    #     password='d0n40minK00V',
    #     first_name='Doncho',
    #     last_name='Minkov',
    # )
    print(request.user)
    user_message = '' if request.user.is_authenticated else 'not '
    return HttpResponse(f'The user is {user_message}authenticated')


def permissions_debug(request):
    usernames = {
        'doncho',  # superuser
        'minkov',  # user with Group...
        'donchominkov',
        # 'Pesho'
    }

    users = User.objects.filter(username__in=usernames)

    permissions_to_check = (
        'auth.add_user',
        'auth.change_user',
        'auth.delete_user',
        'auth.view_user',
    )

    for user in users:
        print('-' * 30)
        print(f'User={user}')
        # User must have all the permissions from `permissions_to_check`
        # print(f'Has {permissions_to_check}:')
        print(f'{permissions_to_check}: {user.has_perms(permissions_to_check)}')

        # User must have any permission from `permissions_to_check`
        for perm in permissions_to_check:
            print(f'{perm}: {user.has_perm(perm)}')

        # Don't do this, it's wrong
        print(user.user_permissions.all())
        print('-' * 30)

    return HttpResponse('It works')


def create_user_and_login(request):
    print(request.user)
    user = User.objects.create_user(
        username='Pesho',
        password='User.objects.create_',
    )

    # Handles the following:
    # - creates the session
    # - attaches `user` to request
    login(request, user)
    print(request.user)
    return HttpResponse('It works')


'''
Ways to create users:
1. `python manage.py createsuperuser`
2. From admin by a superuser
3. With code: 
    - `User.objects.create_user()`
    - `User.objects.create_superuser()`

'''

'''
minkov
D0nch0!%123
'''
