# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
#from django.utils.translation import ugettext_lazy as _

from .managers import StudentManager, TeacherManager
from .managers import AdministratorManager, TeacherAdministratorManager


USER_CHOICES = (
    ('s', 'Students'),
    ('t', 'Teachers'),
    ('a', 'Admin_personal'),
    ('b', 'Teachers_and_admin_personal')
)


@python_2_unicode_compatible
class User(AbstractUser):
    type = models.CharField(max_length=1, choices=USER_CHOICES, default='s')
    credits = models.SmallIntegerField(default=0)
    semester = models.SmallIntegerField(default=0)
    # First Name and Last Name do not cover name patterns
    # around the globe.
    #name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class Student(User):
    objects = StudentManager()

    class Meta:
        proxy = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('students:detail', kwargs={'username': self.username})


class Teacher(User):
    objects = TeacherManager()

    class Meta:
        proxy = True
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('teaches:detail', kwargs={'username': self.username})


class Administrator(User):
    objects = AdministratorManager()

    class Meta:
        proxy = True
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('administrators:detail',
                       kwargs={'username': self.username})


class TeacherAdministrator(User):
    objects = TeacherAdministratorManager()

    class Meta:
        proxy = True
        verbose_name = 'TeacherAdministrator'
        verbose_name_plural = 'TeachersAdministrators'
