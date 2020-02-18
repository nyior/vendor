from rest_framewrok import serializers

from users.models import CustomUser

class CustomUserSerializer(serializers.model):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_picture', 'phone_number', 'residence_hall', 'bio']