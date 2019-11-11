from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from api.scripts.views import RunnerPython, StaticFiles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/scripts/', RunnerPython.as_view()),
    path('api/v1/files/', StaticFiles.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
