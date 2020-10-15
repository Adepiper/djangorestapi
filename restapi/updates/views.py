from django.shortcuts import render
from .models import Update
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from restapi.mixims import JsonresponseMixib

# Create your views here.


def detail_view(request):

    data = {
        'count': 1000,
        'content': 'how are you'
    }

    return JsonResponse(data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'how are you'
        }

        return JsonResponse(data)


class JsonCBV2(JsonresponseMixib, View):
    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'how are you'
        }

        return self.render_to_json_response(data)


class SerialiizedDetailView(JsonresponseMixib, View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = obj.serialize()
        return HttpResponse(data, content_type='application/json')


class SerialiizedListView(JsonresponseMixib, View):
    def get(self, request, *args, **kwargs):
        data = Update.objects.all().serialize()
        return HttpResponse(data, content_type='application/json')
