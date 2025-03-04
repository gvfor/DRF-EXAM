from django.urls import path
from meals import views

urlpatterns = [
    path('users/',views.UsercreateView.as_view()),
    path('meals/',views.MealListCreateView.as_view()),
    path('meals/<int:pk>/',views.MealRetriveUpdateDestroyView.as_view()),
    path('meals/',views.GetmealsView.as_view()),
    path('summary/',views.Mealsummaryview.as_view())
   
   
]