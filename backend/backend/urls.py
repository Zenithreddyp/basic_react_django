"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 🔽 Django’s built-in admin and routing imports
from django.contrib import admin
from django.urls import path,include

# 🔽 Import your custom registration view from your app (e.g. api/views.py)
from api.views import CreateUserView

# 🔽 Import JWT views from DRF SimpleJWT for login and token refresh
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [

    # ✅ Admin panel (Django default)
    path('admin/', admin.site.urls),

    # ✅ Register a new user using your custom CreateUserView
    # POST request to: http://localhost:8000/api/user/register/
    path("api/user/register/", CreateUserView.as_view(), name="register"),

    # ✅ Get JWT tokens (access + refresh) using username & password
    # POST request to: http://localhost:8000/api/token/
    # Payload: { "username": "john", "password": "test123" }
    # Returns: { "access": "...", "refresh": "..." }
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),

    # ✅ Refresh access token using the refresh token
    # POST request to: http://localhost:8000/api/token/refresh/
    # Payload: { "refresh": "your-refresh-token" }
    # Returns: { "access": "new-access-token" }
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),

    # ✅ DRF's default login/logout views for the browsable API (optional)
    # Useful when you're testing the API via the browser (not needed in production)
    path("api-auth/", include("rest_framework.urls")),

    path("api/",include("api.urls"))

]
