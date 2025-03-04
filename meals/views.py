from django.shortcuts import render,get_object_or_404
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.response import Response
from meals.models import Meal
from meals.serializers import UserSerializer,MealSerializer
from rest_framework import authentication,permissions



# Create your views here.
class UsercreateView(CreateAPIView):

    serializer_class=UserSerializer

class MealListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=MealSerializer

    queryset=Meal.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class MealRetriveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=MealSerializer

    queryset=Meal.objects.all()