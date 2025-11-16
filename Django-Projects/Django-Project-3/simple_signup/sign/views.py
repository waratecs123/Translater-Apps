from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import mail_managers
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import test, printer


# Create your views here.

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='premium')
    if not request.user.groups.filter(name='premium').exists():
        premium_group.user_set.add(user)
    return redirect('/')

class MyView(PermissionRequiredMixin, View):
    permission_required = ('<app>.<action>_<model>', '<app>.<action>_<model>')

test.delay()

class IndexView(View):
    def get(self, request):
        printer.delay(10)
        return HttpResponse('Hello!')