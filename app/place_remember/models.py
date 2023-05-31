from django.db import models
from allauth.socialaccount.models import SocialAccount


class Memory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Воспоминание")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    user_id = models.ForeignKey(SocialAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Воспоминания'
        verbose_name_plural = 'Воспоминания'
