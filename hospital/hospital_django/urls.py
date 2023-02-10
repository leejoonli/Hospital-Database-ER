from django.urls import path
from . import views
#from rest_framework import DefaultRouter

urlpatterns = [
    path('procedures', views.ProcedureList.as_view(), name='procedure_list'),
    path('procedures/<int:pk>', views.ProcedureDetail.as_view(), name='procedure_detail'),
]