from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Post, Category
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import datetime
from django.conf import settings
from django.urls import reverse


# Сигнал для добавления пользователя в группу common при регистрации
@receiver(post_save, sender=User)
def add_user_to_common_group(sender, instance, created, **kwargs):
    if created:
        common_group = Group.objects.get_or_create(name='common')[0]
        instance.groups.add(common_group)


# Сигнал для отправки приветственного письма
@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created and instance.email:
        subject = 'Добро пожаловать в наш новостной портал!'
        html_message = render_to_string('emails/welcome_email.html', {
            'username': instance.username,
            'site_url': settings.SITE_URL
        })
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            html_message=html_message,
            fail_silently=False,
        )


# Сигнал для отправки уведомлений о новых статьях
@receiver(post_save, sender=Post)
def send_new_post_notification(sender, instance, created, **kwargs):
    if created and instance.post_type == 'AR':  # Только для статей
        categories = instance.categories.all()
        for category in categories:
            subscribers = category.subscribers.all()
            post_url = settings.SITE_URL + reverse('news_detail', kwargs={'pk': instance.pk})

            for user in subscribers:
                if user.email:
                    subject = f'Новая статья в категории {category.topic}: {instance.title}'
                    html_message = render_to_string('emails/new_post_notification.html', {
                        'post': instance,
                        'username': user.username,
                        'post_url': post_url,
                        'category': category,
                    })
                    plain_message = strip_tags(html_message)

                    msg = EmailMultiAlternatives(
                        subject,
                        plain_message,
                        settings.DEFAULT_FROM_EMAIL,
                        [user.email]
                    )
                    msg.attach_alternative(html_message, "text/html")
                    msg.send()


# Функция для еженедельной рассылки
def send_weekly_newsletter():
    week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    categories = Category.objects.all()

    for category in categories:
        subscribers = category.subscribers.all()
        new_articles = Post.objects.filter(
            categories=category,
            created_at__gte=week_ago,
            post_type='AR'
        ).order_by('-created_at')

        if new_articles.exists():
            for user in subscribers:
                if user.email:
                    subject = f'Новые статьи в категории {category.topic} за неделю'
                    html_message = render_to_string('emails/weekly_newsletter.html', {
                        'articles': new_articles,
                        'username': user.username,
                        'category': category,
                        'site_url': settings.SITE_URL
                    })
                    plain_message = strip_tags(html_message)

                    msg = EmailMultiAlternatives(
                        subject,
                        plain_message,
                        settings.DEFAULT_FROM_EMAIL,
                        [user.email]
                    )
                    msg.attach_alternative(html_message, "text/html")
                    msg.send()


# Настройка планировщика
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
        send_weekly_newsletter,
        trigger=CronTrigger(day_of_week="mon", hour="8", minute="0"),  # Каждый понедельник в 8:00
        id="weekly_newsletter",
        max_instances=1,
        replace_existing=True,
    )

    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()