from django.urls import path
from django.contrib import admin
from core.views import test, TestAPIView, CheckListsAPIView, CheckListAPIView, CheckListItemCreateAPIView, CheckListItemAPIView


urlpatterns = [
    # path('',test),
    path('class/',TestAPIView.as_view()),
    path('api/checklists/',CheckListsAPIView.as_view()),
    path('api/checklist/<int:pk>/',CheckListAPIView.as_view()),
    path('api/checklistitem/create/',CheckListItemCreateAPIView.as_view()),
    path('api/checklistitem/<int:pk>/',CheckListItemAPIView.as_view()),
    
]
