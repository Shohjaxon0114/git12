from django.shortcuts import render
from rest_framework.views import APIView
from .models import NoutbooksModel, CustomerModel
from .serializers import NoutbooksModelSerializers, CustomerModelSerializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers

# Create your views here.
class AllNoutbooksView(APIView):
    def get(self,request,*args,**kwargs):
        all_noutbooks = NoutbooksModel.objects.all()
        serializer = NoutbooksModelSerializers(all_noutbooks,many=True)
        return Response(serializer.data,status=200)


class DetailNoutbooksView(APIView):
    def get(self,request,*args,**kwargs):
        noutbook = get_object_or_404(NoutbooksModel,id=kwargs['id'])
        serializer = NoutbooksModelSerializers(noutbook)
        return Response(serializer.data,status=200)

class UpdateNoutbooksView(APIView):
    def patch(self,request,*args,**kwargs):
        noutbook = get_object_or_404(NoutbooksModel,id=kwargs['id'])
        serializer1 = NoutbooksModelSerializers(noutbook,data=request.data,partial=True)
        if serializer1.is_valid():
            serializer1.save()
            return Response("Success update!")
        return Response(serializer1.errors)

class CreatedNoutbookView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = NoutbooksModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Success created!",status=201)
        return Response(serializer.errors)

class DeletedNoutbookView(APIView):
    def delete(self,request,*args,**kwargs):
        noutbook = get_object_or_404(NoutbooksModel,id=kwargs['id'])
        noutbook.delete()
        return Response({"msg" : "Success deleted"})

class GetByApiView(APIView):
    def get(self,request):
        price = request.query_params.get('price',False)
        ram = request.query_params.get('ram',False)
        model = request.query_params.get('model',False)
        all_noutbooks = NoutbooksModel.objects.filter(model=model,price=price,ram=ram)
        serializer = NoutbooksModelSerializers(all_noutbooks,many=True)
        return Response(serializer.data)

class GetCustomer(APIView):
    def get(self,request):
        all_customer = CustomerModel.objects.all()
        serializer = CustomerModelSerializers(all_customer,many=True)
        return Response(serializer.data,status=200)
