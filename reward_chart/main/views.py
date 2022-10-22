from django.shortcuts import render, get_object_or_404

from .models import Chart
from datetime import datetime


def _prepare_context(chart: Chart) -> dict:
    return {"chart": chart, "now": datetime.now().isoformat()}


def _render_index(request, chart):
    return render(request, "index.html", _prepare_context(chart))


def index(request):
    chart = Chart.objects.first()
    return _render_index(request, chart)


def increase_points(request, chart_id):
    chart = get_object_or_404(Chart, pk=chart_id)
    chart.points += 1
    chart.save()
    return _render_index(request, chart)


def redeem(request, chart_id):
    chart = get_object_or_404(Chart, pk=chart_id)
    chart.points -= 1
    chart.save()
    return _render_index(request, chart)
