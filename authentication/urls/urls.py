from django.urls import path, include


urlpatterns = [
    path('auth/', include('authentication.urls.authentication_urls')),
    path('user/', include('authentication.urls.user_urls')),
]