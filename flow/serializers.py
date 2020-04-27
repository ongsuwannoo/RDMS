from rest_framework import serializers

from .models import Flow
from camp.models import Camp, MC, Department
from locations.models import Location

class locationSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    desc = serializers.CharField()
    logo = serializers.CharField()

class MCSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    typeOfMC = serializers.CharField()
    desc = serializers.CharField()

class DepartmentSerializer(serializers.Serializer):
    name = serializers.CharField()
    typeOfDepartment = serializers.CharField()
    desc = serializers.CharField()

class CampSerializer(serializers.Serializer):
    head = serializers.CharField()
    name = serializers.CharField()
    desc = serializers.CharField()
    logo = serializers.CharField()

class FlowSerializer(serializers.Serializer):
    time_start = serializers.CharField()
    time_end = serializers.CharField()
    activity = serializers.CharField()
    sub_time = serializers.CharField()
    desc = serializers.CharField()

    camp = CampSerializer()
    department = DepartmentSerializer()
    mc = MCSerializer()
    location = serializers.CharField()

    note = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `ToDoItem` instance, given the validated data.
        """
        return Staff.objects.create(**validated_data)