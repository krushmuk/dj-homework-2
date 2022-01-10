from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile))
        paginator = Paginator(reader, 10)
        page = int(request.GET.get('page', 1))
        bus_stations = paginator.get_page(page)


    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
         'bus_stations': bus_stations,
         'page': bus_stations,
    }
    return render(request, 'stations/index.html', context)