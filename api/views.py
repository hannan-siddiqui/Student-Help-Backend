from .models import *
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response





class StudentView(APIView):
  
    def get(self, request):
        student = Student.objects.all()
        studentSerObj = StudentSerializer(student, many=True)
        return Response(studentSerObj.data)
    
    def post(self,request):
        serializeobj=StudentSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)


# update datails 

class DetailsUpdate(APIView):
    def post(self,request,pk):
        try:
            detailObj=Student.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")

        serializeobj=StudentSerializer(detailObj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)
    


# dalete datails

class DetailsDelete(APIView):
    def post(self,pk):
        try:
            detailObj=Student.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        detailObj.delete()
        return Response(200)
    
