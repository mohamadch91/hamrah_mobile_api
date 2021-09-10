from rest_flex_fields import FlexFieldsModelSerializer
from .models import Product, broke, changed, color, mod,Image
from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']
class ModSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = mod
        fields = ['pk','name']
class ColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = color
        fields = ['pk','name']
class BrokeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = broke
        fields = ['pk','Battry','Mic','Speaker','Lcd','Touch','FrontCam','BackCam','other']
class ChangedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = changed
        fields = ['pk','Battry','Mic','Speaker','Lcd','Touch','FrontCam','BackCam','other']
                
                     
class ProductSerializer(serializers.ModelSerializer):
    color=ColorSerializer()
    Broken=BrokeSerializer()
    mod=ModSerializer()
    change=ChangedSerializer()
    Image=ImageSerializer
    class Meta:
        model = Product
        fields = ['pk','year','BattryHealth','image','ram','mod','color','Broken','change']
        expandable_fields = {
          'mod': (ModSerializer, {'one': True},)
        }

    def create(self, validated_data):
        print(validated_data)
        year=validated_data['year']
        ram=validated_data['ram']
        image1=validated_data['image']
        image1=validated_data['image']
        image2=Image.objects.create(name=image1['name'],image=image1['image'],image_ppoi=image1['image_ppoi'])
        BattryHealth=validated_data['BattryHealth']
        mod1=validated_data['mod']
        mod2=mod.objects.create(name=mod1['name'])
        color1=validated_data['color']
        color2=color.objects.create(name=color1['name'])
        broken1=validated_data['Broken']
        broken2=broke.objects.create(Battry=broken1['Battry'],Mic=broken1['Mic'],Speaker=broken1['Speaker'],Lcd=broken1['Lcd'],Touch=broken1['Touch'],FrontCam=broken1['FrontCam'],BackCam=broken1['BackCam'],other=broken1['other'])
        changed1=validated_data['change']
        changed2=changed.objects.create(Battry=changed1['Battry'],Mic=changed1['Mic'],Speaker=changed1['Speaker'],Lcd=changed1['Lcd'],Touch=changed1['Touch'],FrontCam=changed1['FrontCam'],BackCam=changed1['BackCam'],other=changed1['other'])
        return Product.objects.create(mod=mod2,image=image2,year=year,ram=ram,BattryHealth=BattryHealth,color=color2,Broken=broken2,change=changed2)

    def update(self, instance, validated_data): 
        instance.mod = validated_data.get('mod', instance.mod)
        instance.year = validated_data.get('year', instance.year)
        instance.ram = validated_data.get('ram', instance.ram)
        instance.image=validated_data.get('image', instance.image)
        instance.BattryHealth = validated_data.get('BattryHealth', instance.BattryHealth)
        instance.color = validated_data.get('color', instance.color)
        instance.Broken = validated_data.get('Broken', instance.Broken)
        instance.change = validated_data.get('change', instance.change)
        instance.save()
        return instance    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token        