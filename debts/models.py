from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

SEMESTER_CHOICES = (
    (1, 'semester1'),
    (2, 'semester2')
)


class Debt(models.Model):
    year = models.DateField()
    semester = models.SmallIntegerField(choices=SEMESTER_CHOICES, default=1)
    inscription_payment = models.DecimalField(max_digits=15,
                                              decimal_places=2, default=0.0)
    library_debts = models.DecimalField(max_digits=15,
                                        decimal_places=2,  default=0.0)
    laboratory_debts = models.DecimalField(max_digits=15,
                                           decimal_places=2, default=0.0)
    username = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('id:detail', kwargs={'id': self.id})
