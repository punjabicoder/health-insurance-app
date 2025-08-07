from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InsurancePlanViewSet, UserPolicyViewSet, ClaimViewSet, CurrentUSerView, get_current_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('plans', InsurancePlanViewSet)
router.register('policies', UserPolicyViewSet)
router.register('claims', ClaimViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('me/', get_current_user),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
