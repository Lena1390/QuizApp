from django.contrib import admin
from proxymodelapp.models import *


admin.site.register(UserAccount)


class Teacher:
    pass


admin.register(Teacher)


class Student:
    pass


admin.register(Student)
