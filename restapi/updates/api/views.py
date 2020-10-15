from updates.models import Update as UpdateModel
import json
from django.views.generic import View
from django.http import HttpResponse
from .mixins import CSRFExemptMixin
from restapi.mixims import HttpResponseMixin
from updates.forms import UpdateModelForm
from .utils import is_json


class UpdateModelDetailsApi(HttpResponseMixin, CSRFExemptMixin, View):

    def get_object(self, id=None):
        try:
            obj = UpdateModel.objects.get(id=id)
        except UpdateModel.DoesNotExist:
            obj = None

        return obj

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({
                'message': 'That content doest exist'
            })
            return self.render_to_response(error_data, status=404)
        return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        data = {}
        return self.render_to_response(data)

    def put(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({
                'message': 'Update not found'
            })
            return self.render_to_response(error_data, status=404)
        if is_json(request.body) == False:
            json_data = json.dumps({
                'message': 'Value must me in json format'
            })
            return self.render_to_response(json_data, status=400)

        passed_data = json.loads(request.body)
        data = json.loads(obj.serialize())
        for key, value in passed_data.items():
            data[key] = value
        print(data)
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            data = json.dumps(data)
            json_data = json.dumps({
                'message': 'Saved successfully'
            })
            return self.render_to_response(json_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        json_data = json.dumps({
            'message': 'bad request'
        })
        return self.render_to_response(json_data, status=400)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({
                'message': 'That content doest exist'
            })
            return self.render_to_response(error_data, status=404)

        return self.render_to_response(obj, status=200)


class UpdateModelListApi(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True
    querset = None

    def get_queryset(self):
        qs = UpdateModel.objects.all()
        self.querset = qs
        return qs

    def get_object(self, id=None):
        if id is None:
            return None
        obj = self.get_queryset().filter(id=id)
        if obj.count() == 1:
            return obj.first()
        return None

    def get(self, request, *args, **kwargs):
        passed_data = json.loads(request.body)
        passed_data_id = passed_data.get('id', None)
        if passed_data_id is not None:
            obj = self.get_object(id=passed_data_id)
            if obj is None:
                error_data = json.dumps({
                    'message': 'That content doest exist'
                })
                return self.render_to_response(error_data, status=404)
            data = obj.serialize()
            return self.render_to_response(data)
        else:
            obj = self.get_queryset()
            data = obj.serialize()
            return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        if is_json(request.body) == False:
            json_data = json.dumps({
                'message': 'Value must me in json format'
            })
            return self.render_to_response(json_data, status=400)

        requested_data = json.loads(request.body)
        form = UpdateModelForm(requested_data)
        if form.is_valid():
            obj = form.save(commit=True)
            data = obj.serialize()
            return self.render_to_response(data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = json.dumps({
            'message': 'unknown data'
        })
        return self.render_to_response(data, status=400)

    def put(self, request, *args, **kwargs):
        passed_data = json.loads(request.body)
        if is_json(request.body) == False:
            json_data = json.dumps({
                'message': 'Value must me in json format'
            })
            return self.render_to_response(json_data, status=400)
        passed_data_id = passed_data.get('id', None)
        obj = self.get_object(passed_data_id)
        if obj is None:
            error_data = json.dumps({
                'message': 'Update not found'
            })
            return self.render_to_response(error_data, status=404)
        data = json.loads(obj.serialize())
        for key, value in passed_data.items():
            data[key] = value
        print(data)
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            data = json.dumps(data)
            json_data = json.dumps({
                'message': 'Saved successfully'
            })
            return self.render_to_response(json_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        json_data = json.dumps({
            'message': 'bad request'
        })
        return self.render_to_response(json_data, status=400)

    def delete(self, request, *args, **kwargs):
        passed_data = json.loads(request.body)
        passed_data_id = passed_data.get('id', None)
        if passed_data_id is not None:
            obj = self.get_object(passed_data_id)
            if obj is None:
                error_data = json.dumps({
                    'message': "The object you are trying to delete doesn't exist"
                })
                return self.render_to_response(error_data, status=400)
            obj.delete()
            success_data = json.dumps({
                'message':  'Update has been successfully deleted'
            })
            return self.render_to_response(success_data, status=200)
        error_data = json.dumps({
            'message': "bad request"
        })
        return self.render_to_response(error_data, status=400)
