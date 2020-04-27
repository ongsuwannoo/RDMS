from rest_framework import serializers

from .models import Flow
from camp.models import Camp, MC, Department
from locations.models import Location

class LocationSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    desc = serializers.CharField()
    class Meta:
        model = Location
        fields = ('name','desc')

class MCSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    desc = serializers.CharField()

    class Meta:
        model = MC
        fields = ('name','desc')

class DepartmentSerializer(serializers.Serializer):
    name = serializers.CharField()
    desc = serializers.CharField()

    class Meta:
        model = Department
        fields = ('name','desc')

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
    location = LocationSerializer()

    note = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `ToDoItem` instance, given the validated data.
        """
        return Staff.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `ToDoItem` instance, given the validated data.
        """
        instance.text = validated_data.get('text', instance.text)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.complete_flag = validated_data.get('complete_flag', instance.complete_flag)
        instance.display_order = validated_data.get('display_order', instance.display_order)
        instance.save()
        return instance