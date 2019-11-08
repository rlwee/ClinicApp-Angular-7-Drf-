from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',
                  'date_of_birth',
                  'password')
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            date_of_birth = validated_data['date_of_birth'],
            password = validated_data['password']
        )

        return user