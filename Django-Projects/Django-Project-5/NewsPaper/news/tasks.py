from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import Post, Category
from datetime import datetime, timedelta
from django.contrib.auth.models import User


@shared_task
def send_new_post_notification(post_id):
    post = Post.objects.get(id=post_id)
    categories = post.categories.all()

    for category in categories:
        subscribers = category.subscribers.all()
        for user in subscribers:
            subject = f'Новая публикация в категории {category.topic}'
            message = render_to_string('email/new_post_notification.html', {
                'user': user,
                'post': post,
                'category': category,
            })
            send_mail(
                subject=subject,
                message='',
                html_message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )


@shared_task
def send_weekly_newsletter():
    # Новости за последнюю неделю
    week_ago = datetime.now() - timedelta(days=7)
    recent_posts = Post.objects.filter(created_at__gte=week_ago)

    if not recent_posts.exists():
        return

    # Получаем всех пользователей с подписками
    users_with_subs = User.objects.filter(subscriptions__isnull=False).distinct()

    for user in users_with_subs:
        # Категории, на которые подписан пользователь
        user_categories = user.subscriptions.all()
        # Новости в этих категориях
        posts = recent_posts.filter(categories__in=user_categories).distinct()

        if posts.exists():
            subject = 'Еженедельная подборка новостей'
            message = render_to_string('email/weekly_newsletter.html', {
                'user': user,
                'posts': posts,
                'categories': user_categories,
            })
            send_mail(
                subject=subject,
                message='',
                html_message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )