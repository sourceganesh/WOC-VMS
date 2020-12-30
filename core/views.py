from django.shortcuts import render
from rest_framework import views
from core.models import VehicleLogs
from core.serializers import VehicleLogsSerializer
from rest_framework import authentication, permissions
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from vehiclemanagement import settings


# Create your views here.
def index(request):
    return render(request,'core/index.html')

class LogVehicle(views.APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def logging(self, request, format=None):
        pass

def webcam_index(request):
    return render(request,'core/admin_view.html')

@csrf_exempt
def save_image(request):
	if request.method == 'POST':
		# save it somewhere
		f = open(settings.MEDIA_ROOT + '/vehicle_image/someimage.jpg', 'wb')
		f.write(request.body)
		f.close()
		# return the URL
		# return HttpResponse('')
	else:
		return HttpResponse('no data')