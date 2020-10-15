from django.urls import path

from .views import UpdateModelDetailsApi, UpdateModelListApi

urlpatterns = [
    path('api/serialize/listview', UpdateModelListApi.as_view()),
    path('api/serialize/listview/<int:id>', UpdateModelDetailsApi.as_view())
]
