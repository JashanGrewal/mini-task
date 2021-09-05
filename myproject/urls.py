from django.contrib import admin
from django.urls import path
from studentdata import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_api),
    path('<int:pk>', views.student_api),
]
