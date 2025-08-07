from django.shortcuts import render
from rest_framework import viewsets, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InsurancePlan, UserPolicy, Claim
from .serializers import InsurancePlanSerializer, UserPolicySerializer, ClaimSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        })
    else:
        return Response({
            "id": None,
            "username": "Anonumous",
            "email": None,
            "role": "guest"
        })
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class CurrentUSerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class InsurancePlanViewSet(viewsets.ModelViewSet):
    queryset = InsurancePlan.objects.all()
    serializer_class = InsurancePlanSerializer
    permission_classes = [IsAuthenticated]

class UserPolicyViewSet(viewsets.ModelViewSet):
    queryset = UserPolicy.objects.all()
    serializer_class = UserPolicySerializer
    permission_classes = [IsAuthenticated]

class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [IsAuthenticated]





# Create your views here.
