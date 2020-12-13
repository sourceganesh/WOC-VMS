from django.shortcuts import render
from rest_framework import views
from core.models import VehicleLogs
from core.serializers import VehicleLogsSerializer
from rest_framework import authentication, permissions


# Create your views here.
def index(request):
    return render(request,'core/index.html')

class LogVehicle(views.APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def logging(self, request, format=None):
        pass