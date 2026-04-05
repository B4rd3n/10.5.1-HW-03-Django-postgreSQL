from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os
from dotenv import load_dotenv
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import timedelta

from .models import Post, Subscriber


load_dotenv()


@shared_task
def weakly_send():
    today = timezone.now()
    frequency = 7
    first_day = today - timedelta(days=frequency)
    posts_list = Post.objects.filter(creation_time__range=[first_day, today])
    if not posts_list.exists():
        return

    for user in User.objects.all():
        print(user)
        user_categories = Subscriber.objects.filter(user_sub=user).values_list('category', flat=True)
        posts_for_user = posts_list.filter(post_category__in=user_categories).distinct().order_by('-creation_time')

        if posts_for_user.exists():
            html_content = render_to_string(
                'weekly_mail.html',
                {
                    'post_list': posts_for_user,
                    'user': user,
                }
            )

            msg = EmailMultiAlternatives(
                subject=f'Привет',
                body='Test django',
                from_email=os.getenv('EMAIL_HOST_USER'),
                to=[user.email],
            )
            msg.attach_alternative(html_content, "text/html")

            try:
                msg.send()
                print(f"Отправлено пользователю: {user.email}")
            except Exception as e:
                print(f"Ошибка при отправке {user.email}: {e}")


@shared_task
def send_mail_for_subscribers(instance_id):
    try:
        instance = Post.objects.get(pk=instance_id)
    except Post.DoesNotExist:
        return

    if not instance.is_notified:
        categories = instance.post_category.all()

        if not categories.exists():
            return

        subscribers = User.objects.filter(
            subscribed_categories__in=categories
        ).distinct()

        for user in subscribers:
            if not user.email:
                continue

            html_content = render_to_string(
                'post_created.html',
                {
                    'post': instance,
                    'user': user,
                }
            )

            msg = EmailMultiAlternatives(
                subject=f'Новая статья: {instance.title}',
                body=instance.preview(),
                from_email=os.getenv('EMAIL_HOST_USER'),
                to=[user.email],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        # Обновляем флаг уведомления
        instance.is_notified = True
        instance.save(update_fields=['is_notified'])