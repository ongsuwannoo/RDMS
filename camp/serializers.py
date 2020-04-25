from rest_framework import serializers

from .models import Department


class DepartmentSerializer(serializers.Serializer):
    camp = serializers.CharField()
    name = serializers.CharField(max_length=255)
    typeOfDepartment = serializers.CharField(max_length=255)
    desc = serializers.CharField()

    def validated_name(self, value):
        return value

    def create(self, validated_data):
        """
        Create and return a new `ToDoItem` instance, given the validated data.
        """
        return Department.objects.create(
            camp = validated_data['camp'],
            name = validated_data['name'],
            typeOfDepartment = validated_data['typeOfDepartment'],
            desc = validated_data['desc']
        )

    def update(self, instance, validated_data):
        """
        Update and return an existing `ToDoItem` instance, given the validated data.
        """
        # instance.camp = validated_data['camp']
        # instance.name = validated_data['name']
        # instance.typeOfDepartment = validated_data['typeOfDepartment']
        # instance.desc = validated_data['desc']
        # instance.save()
        return instance
