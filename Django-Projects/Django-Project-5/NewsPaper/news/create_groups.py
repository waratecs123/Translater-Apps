from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from news.models import Post


class Command(BaseCommand):
    help = 'Создает группы common и authors с соответствующими правами'

    def handle(self, *args, **options):
        # Создаем или получаем группы
        common_group, created = Group.objects.get_or_create(name='common')
        authors_group, created = Group.objects.get_or_create(name='authors')

        # Получаем ContentType для модели Post
        content_type = ContentType.objects.get_for_model(Post)

        # Получаем разрешения
        post_permissions = Permission.objects.filter(content_type=content_type)

        # Добавляем разрешения в группу authors
        for perm in post_permissions:
            if perm.codename in ['add_post', 'change_post', 'delete_post']:
                authors_group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Группы успешно созданы'))