from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from hackadoo import views

urlpatterns = [
    path('', views.home, name='home'),
    path("api/", include("articles.urls")),
    path('admin/', admin.site.urls),
    path("api/token/", views.JWTFromEmailObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
]
