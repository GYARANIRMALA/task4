from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from task4_app.models import User
from products_app.models import Product
from products_app.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from datetime import timedelta

class ProductApi(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        try:
            if request.data["product_inventory_count"] < 0 :
                return Response({"error": "product_inventory_count should not be Negitive"}, status=status.HTTP_400_BAD_REQUEST)
            
            product = Product(
                product_name = request.data["product_name"],
                product_description = request.data["product_description"],
                product_inventory_count = request.data["product_inventory_count"],
                created_by = self.request.user,
                # active = request.data["active"],
            )
            product.save()
            return Response(
                ProductSerializer(product).data, status=status.HTTP_201_CREATED
            )
        except Exception as err:
            print("error ProductApi create")
            return Response({"error":str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            products = Product.objects.filter(active=True,created_by=self.request.user)
            # products = Product.objects.filter(active="True")
            # products = Product.objects.filter(created_by=self.request.user)
            return Response(
                ProductSerializer(products, many=True).data, status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error ProductApi get")
            return Response({"error":str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs["pk"])
            return Response(
                ProductSerializer(product).data, status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error ProductApi retrieve")
            return Response({"error":str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs["pk"],active=True)
            if product.created_by != request.user:
                return Response({"error":"You do not have permission to update product"}, status=status.HTTP_400_BAD_REQUEST)

            if "product_name" in request.data:
                product.product_name = request.data["product_name"]
            if "product_description" in request.data:
                product.product_description = request.data["product_description"]
            if "product_inventory_count" in request.data:
                if request.data["product_inventory_count"] < 0 :
                    return Response({"error": "product_inventory_count should not be Negitive"}, status=status.HTTP_400_BAD_REQUEST)
            product.save()
            return Response(
                ProductSerializer(product).data, status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error ProductApi update")
            return Response({"error":str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

## Soft Deletion ##
    def destroy(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(active=True,id=kwargs["pk"])
            if product.created_by != request.user:
                return Response({"error":"You do not have permission to delete product"}, status=status.HTTP_400_BAD_REQUEST)
            product.active = False
            product.save()
            return Response(
                {"error" : "This Product was Deleted"}, status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error ProductApi destroy",err)
            return Response({"error" : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


























# # Regular Deletion # #
    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         product = Product.objects.get(id=kwargs["pk"])
    #         product.delete()
    #         return Response(
    #             status=status.HTTP_200_OK
    #         )
    #     except Exception as err:
    #         print("error ProductApi delete")
    #         return Response({"error":"This product was Deleted"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

