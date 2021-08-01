from django.db import models
from django.utils.translation import ugettext_lazy as _

from dateutil.relativedelta import relativedelta


class Driver(models.Model):
    first_name = models.CharField(_('first name'), max_length=128, blank=True)
    last_name = models.CharField(_('last name'), max_length=128, blank=True)

    @property
    def full_name(self):
        names = (self.first_name, self.last_name)
        return ' '.join(names)

    birthday = models.DateTimeField(_('birthday'))

    @property
    def age(self):
        return relativedelta(datetime.today(), self.birthday).years

    picture = models.ImageField(upload_to='drivers')

    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    favorites = models.IntegerField(_('favorites'), default=0)

    def favorite(self):
        self.favorites += 1

    nationality = models.CharField(_('nationality'), max_length=128, blank=True)

    is_active = models.BooleanField(_('is active'), default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'


class Team(models.Model):
    name = models.CharField(_('name'), max_length=128, default='Free Agent')
    logo = models.ImageField(upload_to='teams')

    def drivers(self):
        return Driver.objects.filter(team=self)

    def __str__(self):
        return name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
