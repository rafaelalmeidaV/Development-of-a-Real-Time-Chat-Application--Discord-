from django.urls import path
from authentication.views.user_views import CreateUserView, CreateAdminView, ListUsersView


urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('register/admin/', CreateAdminView.as_view(), name='register_admin'),
    path('list/', ListUsersView.as_view(), name='list_users'),    
]
