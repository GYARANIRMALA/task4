from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from task4_app.models import User, Group
from task4_app.serializers import UserSerializer, GroupSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
import requests
import json
import jwt, datetime
from django.contrib.auth import authenticate


class RegisterApi(viewsets.ViewSet):
    

    def create(self, request, *args, **Kwargs):
        try:
            if request.data["role"] not in [User.RoleTypes.admin,User.RoleTypes.manager,User.RoleTypes.staff]:
                return Response({"error":"Invalid role"},status=status.HTTP_400_BAD_REQUEST)
                
            try:
                group = Group.objects.get(name=request.data["group_name"])
            except Exception:
                group = Group(
                    name=request.data["group_name"]
                )
                group.save()

            # if grp info exis

                # get grp uuid and create user
            # else if 
                # create grp

                # get grp uuid and create user


            user = User(
                fullname = request.data["fullname"],
                email = request.data["email"],
                role = request.data["role"],
                group_name = group,
            )
            user.set_password(request.data["password"])
            user.save()
            return Response(
                {"message": "User created"}, status=status.HTTP_201_CREATED
            )
        except Exception as err:
            print("error RegisterApi create",err)
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **Kwargs):
        try:
            users = User.objects.filter().order_by('name')
            return Response(
                UserSerializer(users, many=True).data, status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error RegisterApi get")
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, *args, **Kwargs):
        try:
            user = User.objects.get(id=Kwargs["pk"])
            return Response(
                UserSerializer(user).data, status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error RegisterApi read")
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, *args, **Kwargs):
        try:
            user = User.objects.get(id=Kwargs["pk"])

            if "fullname" in request.data:
                user.fullname = request.data["fullname"]
            if "email" in request.data:
                user.email = request.data["email"]
            if "password" in request.data:
                user.password = request.data["password"]
            if "role" in request.data:
                user.role = request.data["role"]
            if "group_name" in request.data:
                user.group_name = Group.objects.get(group_name=request.data["group_name"])
            user.save()
            return Response(
                UserSerializer(user).data, status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error RegisterApi update",err)
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def destroy(self, request, *args, **Kwargs):
        try:
            user = User.objects.get(id=Kwargs["pk"])
            user.delete()
            return Response(
                status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error RegisterApi delete")
            return Response({"error": "This User was Deleted"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginApi(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        try:
            user = authenticate(
                email=request.data["email"], password=request.data["password"]
            )
            if not user:
                return Response(
                    {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
                )
            serializer = UserSerializer(user).data
            response = requests.post(url="http://127.0.0.1:8000/user/api/token/", data={
                "email" : request.data["email"],
                "password" :request.data["password"],
            })
            token = response.json()
            serializer["refresh"] = token["refresh"]
            serializer["access"] = token["access"]
            return Response(serializer, status=status.HTTP_200_OK)
        except Exception as err:
            print("error --->",err)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
            
    

class GroupApi(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        try:
            group = Group(
                name = request.data["name"],
            )
            group.save()
            return Response(
                GroupSerializer(group).data, status=status.HTTP_201_CREATED
            )
        except Exception as err:
            print("error GroupApi create",err)
            return Response({"error":str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            groups = Group.objects.filter()
            # groups = Group.objects.filter(name="Green_Team").order_by('name')
            return Response(
                GroupSerializer(groups,many=True).data, status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error GroupApi get")
            return Response({"error":str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            group = Group.objects.get(id=kwargs["pk"])
            return Response(
                GroupSerializer(group).data, status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error GroupApi retrieve")
            return Response({"error":str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            group = Group.objects.get(id=kwargs["pk"])

            if "name" in request.data:
                group.name = request.data["name"]
            group.save()
            return Response(
                GroupSerializer(group).data, status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error GroupApi update")
            return Response({"error":str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            group = Group.objects.get(id=kwargs["pk"])
            group.delete()
            return Response(
                {"message": "This Group was Deleted"}, status=status.HTTP_200_OK
            )
        except Exception as err:
            print("error GroupApi destroy")
            return Response({"error":str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)









# AuthUser = get_user_model()

# class LoginApi(viewsets.ViewSet):

    # def create(self, request, *args, **Kwargs):
    #     try:
    #         user = User.objects.get(
    #             email = request.data["email"],
    #             password = request.data["password"],
    #         )
    #         serializer = UserSerializer(user).data

    #         response = requests.post(url="http://127.0.0.1:8000/user/api/token/", data={
    #             "email" : "Nirmala",
    #             "password" : "1234",
    #         })
    #         token = response.json()
    #         serializer["refresh"] = token["refresh"]
    #         serializer["access"] = token["access"]
    #         return Response(
    #             serializer, status=status.HTTP_200_OK
    #         )
    #     except Exception as err:
    #         print("error --->",err)
    #         return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

    # def create(self, request, *args, **kwargs):
    #     try:
    #         auth_user = AuthUser(
    #                 username=request.data["email"],
    #                 is_superuser=True,
    #                 is_staff=True,
    #                 is_active=True
    #         )
    #         auth_user.set_password("12345")
    #         auth_user.save()
    #         return Response(status=status.HTTP_200_OK)
    #     except Exception as err:
    #         print("err --->",err)
    #         return Response({"err":str(err)})

    



