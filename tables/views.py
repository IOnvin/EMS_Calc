from django.shortcuts import render


# Create your views here.

def table(request):
    return render(request, 'tables/tables.html')
