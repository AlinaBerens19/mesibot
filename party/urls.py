from django.urls import path
from . import views


urlpatterns = [
    path('', views.getAllRoutes, name='routes'),
    # path('parties/create/', views.createParty, name='createParty'),
    # path('parties/<str:pk>/update/', views.updateParty, name='updateParty'),
    # path('parties/<str:pk>/delete/', views.deleteParty, name='deleteParty'),
    # path('parties/<str:pk>/', views.getParty, name='getParty'),
    # path('parties/', views.getParties, name='getParties'),
    path('parties/', views.PartyList.as_view(), name='parties'),
    path('parties/<int:pk>/', views.PartyDetail.as_view(), name='party'),

]

