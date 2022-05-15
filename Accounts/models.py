from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    image = models.ImageField(default='def.png',
                              upload_to='Profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


@ receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_save_useu_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
