from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Author

@receiver(post_save, sender=Author)
def notify_new_author(sender, instance, created, **kwargs):
    if created:
        print(f"[Notificação] Novo autor cadastrado: {instance.name}")
