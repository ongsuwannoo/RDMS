from rest_framework import serializers

from .models import Staff
from personal.models import Personal
from camp.models import Camp, MC, Department

class MCSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    typeOfMC = serializers.CharField()
    desc = serializers.CharField()
    class Meta:
        model = MC
        fields = ('name', 'typeOfMC', 'desc')

class DepartmentSerializer(serializers.Serializer):
    name = serializers.CharField()
    typeOfDepartment = serializers.CharField()
    desc = serializers.CharField()

class CampSerializer(serializers.Serializer):
    head = serializers.CharField()
    name = serializers.CharField()
    desc = serializers.CharField()
    logo = serializers.CharField()

class PersonalSerializer(serializers.Serializer):
    sid = serializers.CharField()

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    nick_name = serializers.CharField()
    
    sex = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()

    blood_type = serializers.CharField()
    birthday = serializers.CharField()
    religion = serializers.CharField()
    food_allergy = serializers.CharField()
    congenital_disease = serializers.CharField()
    shirt_size = serializers.CharField()
    
    profile_pic = serializers.CharField()

class StaffSerializer(serializers.Serializer):
    camp = CampSerializer()
    personal = PersonalSerializer()
    position = serializers.CharField()
    group = serializers.CharField()
    department = DepartmentSerializer()
    mc = MCSerializer()
    postscript = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `ToDoItem` instance, given the validated data.
        """
        return Staff.objects.create(**validated_data)
