from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user=user,
            username=user.username
        )
    else:
        profile = Profile.objects.get(user=user)
        profile.email = user.email
        profile.name = user.first_name + ' ' + user.last_name
        profile.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
