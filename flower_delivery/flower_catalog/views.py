from django.shortcuts import render


def flower_list(request):
    return render(request, 'flower_catalog/flower_list.html')
