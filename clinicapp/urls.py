from django.urls import path
from clinicapp.views import (ClientViewSet,
                             )

urlpatterns = [
    path('clients/', ClientViewSet.as_view({'get':'clientList','post':'createClient'}), name='clients'),
    path('client/detail/<int:client_id>/', ClientViewSet.as_view({'get':'clientDetail'}), name='client-detail'),
    path('client/delete/<int:client_id>/', ClientViewSet.as_view({'get':'clientDelete'}), name='client-delete'),

]