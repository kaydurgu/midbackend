from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from women.models import Women, Category
from women.serializers import WomenSerializer, CaregorySerializer

class CaregoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class =  CaregorySerializer
    def post(self, request, *args, **kwargs):
        serializer = CaregorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'category': serializer.data})

class CategoryAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = CaregorySerializer
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
class WomenAPIView(APIView):
    def get(self,request):
        lst = Women.objects.all()
        return Response({'posts': WomenSerializer(lst, many=True).data})
    def post(self,request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})
    def put (self,request, *args ,**kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})
        try:
            instance = Women.objects.get(pk = pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'post': serializer.data})