from django.urls import path, include

from . import views

urlpatterns = [
    path('details', views.detail_view),
    path('cbv/jsoncb1', views.JsonCBV.as_view()),
    path('cbv/jsoncb2', views.JsonCBV2.as_view()),
    path('serialize/detailview', views.SerialiizedDetailView.as_view()),
    path('serialize/listview', views.SerialiizedListView.as_view()),
    path("", include("updates.api.urls")),
]
