from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Chart
from datetime import datetime

POINT_PER_PAGE = 6
REDEEM_OPTIONS = (2, 4, 6, 8)


def _prepare_context(chart: Chart) -> dict:
    display_points = []
    point_slots = max(POINT_PER_PAGE, chart.points)
    point_slots += point_slots % 2

    for i in range(point_slots):
        if i < chart.points:
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
    try:
        chart = Chart.objects.first()
    except Chart.DoesNotExist:
        return HttpResponse("Create a Chart first.")

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


def redeem_center(request, chart_id):
    chart = get_object_or_404(Chart, pk=chart_id)
    return render(
        request, "redeem_center.html", {"chart": chart, "options": REDEEM_OPTIONS}
    )
