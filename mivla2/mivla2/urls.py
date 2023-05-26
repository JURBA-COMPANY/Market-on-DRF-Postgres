from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from services.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls'), name='index'),
    path('catalog/', include('services.urls', namespace='services'), name='get_all'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

