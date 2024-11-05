from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render


def index(request):
    current_time = timezone.now()
    return HttpResponse(f"Текущая дата и время: {current_time}")


def multiplication_table(request):
    mt = [[i * j for j in range(1, 11)] for i in range(1, 11)]
    return render(request, 'multiplication_table.html')


