from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()


def index(requrest):

    users = User.objects.all()

    context = {
        'users': users,
    }

    # username = user.username
    # img_profile = user.img_profile
    # nickname = U

    return render(requrest, 'index.html', context)
