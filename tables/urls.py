from . import views
from django.urls import path


urlpatterns = [
    path('tables/', views.table, name='tables')
]