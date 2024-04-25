"""
URL configuration for todobackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# In urls.py (project-level)

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from todos.views import CustomUserCreateView
from todos.views import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    # API authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # User registration endpoint
    path('api/register/', CustomUserCreateView.as_view(), name='user_register'),
    # User login/logout endpoints
    path('api/login/', login, name='user_login'),
    path('api/logout/', logout, name='user_logout'),
    # Include app-level URLs
    path('api/', include('todos.urls')),  # Replace 'your_app.urls' with the actual module path to your app's URL configuration
    # Other URL patterns for your project...
]


