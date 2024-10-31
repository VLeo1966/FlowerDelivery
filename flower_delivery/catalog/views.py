from django.shortcuts import render, get_object_or_404
from .models import flower


def flower_list(request):
    flowers = flower.objects.all()
    return render(request, "catalog/flower_list.html", {'flowers': flowers})
