from django.urls import path
from accounts.views import (UserViewSet,
                            )

urlpatterns = [
        path('users/', UserViewSet.as_view({'post':'user_create'}), name='users'),
        path('user/<int:user_id>/', UserViewSet.as_view({'get':'user_detail'}), name='user-detail'),
        path('user/login/', UserViewSet.as_view({'post':'user_login'}), name='user-login'),
]