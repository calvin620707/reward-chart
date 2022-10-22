from django.shortcuts import render

from .models import Chart
from datetime import datetime


def index(request):
    default_chart = Chart.objects.first()
    context = {"chart": default_chart, "now": datetime.now().isoformat()}
    return render(request, "index.html", context)
