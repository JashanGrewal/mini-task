from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from .mypaginations import MyPageNumberPagination

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id1 = pk
        if id1 is not None:
            try:
                studt = Student.objects.get(id=id1)
            except Student.DoesNotExist:
                studt = None
            serializer = StudentSerializer(studt)
            return Response(serializer.data)

        paginator = MyPageNumberPagination()
        studt = Student.objects.all()
        result_page = paginator.paginate_queryset(studt, request)
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id2 = pk
        studt1 = Student.objects.get(pk=id2)
        serializer = StudentSerializer(studt1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id2 = pk
        studt2 = Student.objects.get(pk=id2)
        serializer = StudentSerializer(studt2, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id3 = pk
        studt3 = Student.objects.get(pk=id3)
        studt3.delete()
        return Response({'msg':'Data Deleted'})
