from rest_framework import serializers
from core.models import VehicleLogs

class VehicleLogsSerializer(serializers.ModelSerializer):

    class Meta:
        model   = VehicleLogs
        fields  = ('entry_time', 'exit_time', 'vehicle')