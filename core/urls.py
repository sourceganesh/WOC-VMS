from django.urls import path,include
from core import views
from core.views import LogVehicle


app_name = 'core'
urlpatterns = [
    path('', views.index, name="index"),
    path('create', LogVehicle.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework'))
]