from django.urls import path
from . import views 

app_name = 'business'

urlpatterns = [
    path('business/', views.BusinessCreateListView.as_view(), name='business-create-list'),
    path('business/<uuid:pk>/', views.BusinessRetrieveUpdateDestroyView.as_view(), name='business-retrieve-update-destroy'),
]
