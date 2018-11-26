from django.test import TestCase
from rest_framework.test import APIClient

from todo.models import Todo


class TodoTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(id=1, text="Tee jotain", completed=False)

    def test_create_new_todo(self):
        client = APIClient()
        response = client.post('/v1/todo/', {
            'text': 'new idea'
        }, format='json')

        self.assertEqual(response.status_code, 201)  # Created

        self.assertEqual(Todo.objects.count(), 2)

    def test_patch_todo(self):
        client = APIClient()
        response = client.patch('/v1/todo/1/', {
            'text': 'Muuta'
        }, format='json')

        self.assertEqual(response.status_code, 200)

        todo = Todo.objects.get(pk=1)

        self.assertEqual(todo.text, "Muuta")
