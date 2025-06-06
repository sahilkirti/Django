from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.studentView),
    path('student/<int:pk>/', views.studentDetailView),

    path('employee/', views.Employees.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
]
