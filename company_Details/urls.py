from django.contrib import admin
from django.urls import path
from .views import companyAPIView,contactAPIView,company_detail,company_list,contact_list,contact_detail


urlpatterns = [
    path('company/', companyAPIView.as_view()),
    path('detail/<int:pk>/',company_detail),
    path('contact/', contactAPIView.as_view()),
    path('details/<int:pk>/',contact_detail),

]