from django.shortcuts import render, get_object_or_404, redirect

from .models import Chart
from datetime import datetime

POINT_PER_PAGE = 8


def _prepare_context(chart: Chart, page=0) -> dict:
    display_point_number = chart.points - ((page) * 8)

    display_points = []

    for i in range(POINT_PER_PAGE):
        if i < display_point_number:
            display_points.append({"show_point": True})
        else:
            display_points.append({"show_point": False})

    return {
        "chart": chart,
        "now": datetime.now().isoformat(),
        "display_points": display_points,
    }


def _render_index(request, chart):
    return render(request, "index.html", _prepare_context(chart))


def index(request):
    chart = Chart.objects.first()
    return _render_index(request, chart)


def increase_points(request, chart_id):
    chart = get_object_or_404(Chart, pk=chart_id)
    chart.points += 1
    chart.save()
    return redirect("index")


def redeem(request, chart_id):
    chart = get_object_or_404(Chart, pk=chart_id)
    chart.points -= 1
    chart.save()
    return redirect("index")
