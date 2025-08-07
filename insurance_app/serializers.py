from rest_framework import serializers
from .models import InsurancePlan, UserPolicy, Claim, User

class InsurancePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePlan
        fields = '__all__'

class UserPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPolicy
        fields = '__all__'

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')

