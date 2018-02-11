from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()


    def __str__(self):
        return "Пользователь:  %s" % (self.email)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'A lot of Subscribers'
