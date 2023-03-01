from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User, Group

@receiver(signals.post_save,sender=User)
def add_to_default(sender, instance, created,**kwargs):
    if created:
        default_group = Group.objects.get(name='default')
        instance.groups.add(default_group)