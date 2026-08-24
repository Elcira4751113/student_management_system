from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    def validate_age(self, value):
        if value < 15:
            raise serializers.ValidationError(
                "Student must be at least 15 years old."
            )

        return value

    class Meta:
        model = Student
        fields = "__all__"