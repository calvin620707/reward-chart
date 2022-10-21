from django.contrib import admin

from .models import Chart, User


@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ("child", "points")
    pass


admin.site.register(User)
