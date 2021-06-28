from django.contrib import admin
from .models import Doctors, Hospital, Sikk, User
admin.site.register(Doctors)
admin.site.register(Hospital)
admin.site.register(Sikk)
admin.site.register(User)