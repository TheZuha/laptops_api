from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, LaptopViewSet, FeedbackViewSet, RegisterView, LoginView, RefreshTokenView, LogoutView

router = DefaultRouter()
router.register('brands', BrandViewSet, basename='brand')
router.register('laptops', LaptopViewSet, basename='laptop')
router.register('feedbacks', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
