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
    path('', include(router.urls)),
    
    path('blog/', views.BlogsView.as_view()),
    path('comment/', views.CommentsView.as_view()),

    path('blog/<int:pk>', views.BlogDetailView.as_view()),
    path('comment/<int:pk>', views.CommentDetailView.as_view())


]
