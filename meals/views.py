from django.shortcuts import render,get_object_or_404
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.response import Response
from meals.models import Meal
from meals.serializers import UserSerializer,MealSerializer
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from django.db.models import Sum




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

class GetmealsView(APIView):
     
  def get(self,request):

    date=request.GET.get('date')

    meal_type=request.GET.get('meal_type')

    meals=Meal.objects.all()

    if date:

        meals=meals.filter(date=date)
    
    if meal_type:

        meals=meals.filter(meal_type=meal_type)

    serializer=MealSerializer(meals, many=True)

    return Response(serializer.data)


class Mealsummaryview(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        total_calorie=Meal.objects.filter(owner=request.user).values("calorie").aggregate(total=Sum("calorie"))

        print(total_calorie)

        category_summary=Meal.objects.filter(owner=request.user).values("meal_type").annotate(total=Sum("meal_type"))

        context={
            "expense_total":total_calorie.get("total"),
            "category_summary":category_summary
        }

        return Response(data=context)    