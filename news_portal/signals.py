from dotenv import load_dotenv
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .tasks import send_mail_for_subscribers
from .models import Post

load_dotenv()


@receiver(m2m_changed, sender=Post.post_category.through)
def send_mails(sender, instance, action, **kwargs):
    if action == 'post_add':
        send_mail_for_subscribers.delay(instance.id)



