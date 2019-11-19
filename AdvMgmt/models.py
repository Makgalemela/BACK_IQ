from django.db import models

# Advertisement Attributes

class Adv(models.Model):
    adTitle = models.CharField(max_length=250, verbose_name='Ad. Title')
    adDescription = models.TextField(verbose_name='Description')
    adMedia = models.FileField(upload_to='adfiles/%Y/',verbose_name='Media')
    timesPlayed = models.PositiveIntegerField(default=0, verbose_name='Times Played')
    nStoreLocator = models.CharField(max_length=300, verbose_name='Location')
    clientName = models.CharField(max_length=250, verbose_name='Name of Client')

    class Meta:
        verbose_name = "Advert"
        verbose_name_plural = "Advertisements"
    def __str__(self):
        return self.adTitle + " " + self.clientName