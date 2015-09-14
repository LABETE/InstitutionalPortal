from django.db import models


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(type='s')


class TeacherManager(models.Manager):
    def get_queryset(self):
        return super(TeacherManager, self).get_queryset().filter(type='t')


class AdministratorManager(models.Manager):
    def get_queryset(self):
        return super(
            AdministratorManager, self).get_queryset().filter(type='a')


class TeacherAdministratorManager(models.Manager):
    def get_queryset(self):
        return super(
            TeacherAdministratorManager, self).get_queryset().filter(type='b')
