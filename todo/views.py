import json
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .models import Todo


@method_decorator(csrf_exempt, name='dispatch')
class TodoView(View):
    def get(self, request):
        todos = Todo.objects.all()

        result = []
        for todo in todos:
            result.append({
                "id": todo.id,
                "text": todo.text,
                "completed": todo.completed,
                "category": todo.category.id if todo.category else None,
            })

        return HttpResponse(json.dumps(result),
                            content_type="application/json")

    def post(self, request):
        request_data = json.loads(request.body)

        todo = Todo(**request_data)
        todo.save()

        data = {
            "id": todo.id,
            "text": todo.text,
            "completed": todo.completed,
            "category": todo.category.id if todo.category else None,
        }

        return HttpResponse(json.dumps(data), content_type="application/json",
                            status=201)


@method_decorator(csrf_exempt, name='dispatch')
class TodoDetailView(View):
    def get(self, request, todo_id):
        try:
            todo = Todo.objects.get(pk=todo_id)

            data = {
                "id": todo.id,
                "text": todo.text,
                "completed": todo.completed,
                "category": todo.category.id if todo.category else None,
            }

            return HttpResponse(json.dumps(data),
                                content_type="application/json")
        except Todo.DoesNotExist:
            return HttpResponse(json.dumps({"error": "Todo not found"}),
                                content_type="application/json", status=404)

    def patch(self, request, todo_id):
        request_data = json.loads(request.body)

        try:
            todo = Todo.objects.get(pk=todo_id)

            for key, val in request_data.items():
                if key == 'category':
                    key = 'category_id'

                setattr(todo, key, val)

            todo.save()

            data = {
                "id": todo.id,
                "text": todo.text,
                "completed": todo.completed,
                "category": todo.category.id if todo.category else None,
            }

            return HttpResponse(json.dumps(data),
                                content_type="application/json")
        except Todo.DoesNotExist:
            return HttpResponse(json.dumps({"error": "Todo not found"}),
                                content_type="application/json", status=404)

    def delete(self, request, todo_id):
        try:
            todo = Todo.objects.get(pk=todo_id)
            todo.delete()

            return HttpResponse(None, status=204)
        except Todo.DoesNotExist:
            return HttpResponse(json.dumps({"error": "Todo not found"}),
                                content_type="application/json", status=404)
