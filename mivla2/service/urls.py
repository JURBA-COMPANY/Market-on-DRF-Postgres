from django.urls import path, include
from rest_framework import routers


from services.views import *

app_name = 'services'
router = routers.SimpleRouter()
router.register(r'sofa', SofaViewSet)
router.register(r'stol', StolViewSet)
router.register(r'wardrobe', WardrobeViewSet)
router.register(r'furniture', FurnitureViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', shop, name='catalog'),
    path('api/v1/', include(router.urls)),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
]
