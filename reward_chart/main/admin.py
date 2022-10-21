from django.contrib import admin

from .models import Chart, User

admin.site.register(User)
admin.site.register(Chart)
