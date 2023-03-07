from django.urls import path
from . import views

urlpatterns = [
    path('dashboards/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('dashboards/data', views.pivot_data, name='pivot_data'),
    # path('hel/', views.hel, name='pivot_data'),
]