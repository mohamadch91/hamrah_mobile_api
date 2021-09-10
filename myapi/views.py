from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product,Image
from rest_framework.permissions import IsAuthenticated
from .serializers import ImageSerializer
from rest_flex_fields.views import FlexFieldsModelViewSet
class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]    

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer    