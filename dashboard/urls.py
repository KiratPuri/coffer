from django.contrib import admin
from dashboard import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r"^filterd_data/$", views.chart_data.as_view()),
    re_path(r"^filters/$", views.filters.as_view())
]