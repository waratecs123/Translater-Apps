from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Advert
from django.views.generic import CreateView, ListView
from django.core.mail import send_mail
from .models import Response
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.db.models import Q
from .forms import *
from django.views.generic import FormView
from django.core.mail import send_mass_mail
from .forms import NewsletterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.core.mail import send_mail, send_mass_mail
from django.views.generic import (
    ListView, CreateView, DetailView,
    UpdateView, DeleteView, FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django import forms
from django.db.models import Q
from django.utils import timezone
from .models import Advert, Response, Newsletter, Subscription
from .forms import ResponseFilterForm, NewsletterForm



class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return render(request, 'auth/register.html', {'error': 'Email уже занят!'})

        user = User.objects.create_user(username=username, email=email, password=password)
        code = str(random.randint(100000, 999999))
        request.session['verification_code'] = code
        request.session['email'] = email

        send_mail(
            'Код подтверждения',
            f'Ваш код: {code}',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return redirect('confirm_email')


class ConfirmEmailView(View):
    def get(self, request):
        return render(request, 'auth/confirm_email.html')

    def post(self, request):
        user_code = request.POST.get('code')
        saved_code = request.session.get('verification_code')

        if user_code == saved_code:
            email = request.session.get('email')
            user = User.objects.get(email=email)
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return render(request, 'auth/confirm_email.html', {'error': 'Неверный код!'})


class AdvertListView(ListView):
    model = Advert
    template_name = 'adverts/list.html'
    context_object_name = 'adverts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class AdvertCreateView(LoginRequiredMixin, CreateView):
    model = Advert
    fields = ['title', 'content', 'category', 'image', 'video_url']
    template_name = 'adverts/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'adverts/detail.html'


class AdvertUpdateView(LoginRequiredMixin, UpdateView):
    model = Advert
    fields = ['title', 'content', 'category']
    template_name = 'adverts/edit.html'


class AdvertDeleteView(LoginRequiredMixin, DeleteView):
    model = Advert
    success_url = '/'
    template_name = 'adverts/delete.html'


class ResponseAcceptView(LoginRequiredMixin, View):
    def post(self, request, pk):
        response = get_object_or_404(Response, pk=pk, advert__author=request.user)
        response.is_accepted = True
        response.save()

        send_mail(
            'Ваш отклик принят!',
            f'Ваш отклик на объявление "{response.advert.title}" был принят.',
            'from@example.com',
            [response.author.email],
        )
        return redirect('response_list')

class ResponseDeleteView(LoginRequiredMixin, DeleteView):
    model = Response
    template_name = 'responses/delete.html'
    success_url = reverse_lazy('response_list')

    def get_queryset(self):
        return super().get_queryset().filter(advert__author=self.request.user)


class ResponseCreateView(LoginRequiredMixin, CreateView):
    model = Response
    fields = ['text']
    template_name = 'responses/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.advert = Advert.objects.get(pk=self.kwargs['pk'])


        send_mail(
            'Новый отклик!',
            f'На ваше объявление "{form.instance.advert.title}" оставили отклик.',
            'from@example.com',
            [form.instance.advert.author.email],
        )
        return super().form_valid(form)


class UserResponsesView(LoginRequiredMixin, FormMixin, ListView):
    model = Response
    template_name = 'responses/list.html'
    context_object_name = 'responses'
    form_class = ResponseFilterForm

    def get_queryset(self):
        queryset = Response.objects.filter(advert__author=self.request.user)


        advert_id = self.request.GET.get('advert_id')
        if advert_id:
            queryset = queryset.filter(advert_id=advert_id)


        status = self.request.GET.get('status')
        if status == 'accepted':
            queryset = queryset.filter(is_accepted=True)
        elif status == 'rejected':
            queryset = queryset.filter(is_accepted=False)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adverts'] = Advert.objects.filter(author=self.request.user)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class NewsletterCreateView(LoginRequiredMixin, FormView):
    template_name = 'newsletter/create.html'
    form_class = NewsletterForm
    success_url = reverse_lazy('advert_list')

    def form_valid(self, form):
        newsletter = form.save(commit=False)
        newsletter.save()


        subscribers = Subscription.objects.filter(is_active=True).select_related('user')
        emails = [subscriber.user.email for subscriber in subscribers]
        subject = newsletter.title
        message = newsletter.content
        from_email = 'from@example.com'

        email_messages = [(subject, message, from_email, [email]) for email in emails]
        send_mass_mail(email_messages)

        newsletter.sent_at = timezone.now()
        newsletter.save()

        return super().form_valid(form)


class SubscriptionView(LoginRequiredMixin, View):
    def post(self, request):
        subscription, created = Subscription.objects.get_or_create(
            user=request.user,
            defaults={'is_active': True}
        )

        if not created:
            subscription.is_active = not subscription.is_active
            subscription.save()

        return redirect('advert_list')