from django.urls import path
from authentication.views.user_views import CreateUserView, CreateAdminView, ListUsersView, ListUserbyEmailView


urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('register/admin/', CreateAdminView.as_view(), name='register_admin'),
    path('list/', ListUsersView.as_view(), name='list_users'),    
    path('list/email/', ListUserbyEmailView.as_view(), name='list_user_by_email'),
]
