from student.models import Student
from employees.models import Employee
from .serializers import StudentSerializer
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from django.shortcuts import render, get_object_or_404
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer
from employees.filters import EmployeeFilter

@api_view(['GET','POST'])
def studentView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)      #  The client sends data in JSON format → Serializer receives it → Converts it into a Python object → Validates it → Saves it into the database if valid.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try: 
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter

# class EmployeeViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset, many = True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors)
 
#     def retrieve(self, request, pk = None):
#         employee = get_object_or_404(Employee, pk = pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status = status.HTTP_200_OK)
    


    
'''   
class Employees(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpadateDestroyView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
'''
# class EmployeeDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'


    
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)

# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk)


# class Employees(APIView):
#     def get(self, request):
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many = True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    

# class EmployeeDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except  Employee.DoesNotExist :
#             return Http404
        
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serialiser = EmployeeSerializer(employee)
#         return Response(serialiser.data, status = status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serialiser = EmployeeSerializer(employee, data=request.data)
#         if serialiser.is_valid:
#             serialiser.save()
#             return Response(serialiser.data(), status = status.HTTP_200_OK)
#         return Response(serialiser.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)


#-------------------------------------------------------------------------------------------------------------------------------------

class BlogsView(generics.ListCreateAPIView):
    queryset =  Blog.objects.all()
    serializer_class = BlogSerializer

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field ='pk'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field='pk'

