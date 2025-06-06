from django.urls import path, include 
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', views.EmployeeViewset, basename = 'employee')

urlpatterns = [
    path('student/', views.studentView),
    path('student/<int:pk>/', views.studentDetailView),

    # path('employee/', views.Employees.as_view()),
    # path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
    path('', include(router.urls))
]
