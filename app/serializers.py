from rest_framework import serializers
from app.models import DroneCategory, Drone, Pilot, Competion

class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedModelSerializer(
        many=True,
        read_only=True,
        view_name = 'drone-detail')
    
    class Meta:
        model = DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            'drones' )

class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), 
                                                  sluge_field='name')
