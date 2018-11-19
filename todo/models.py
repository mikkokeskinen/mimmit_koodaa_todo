from django.db import models


class TodoCategory(models.Model):
    name = models.CharField(max_length=255)


class Todo(models.Model):
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(TodoCategory, related_name='todos', null=True, blank=True, on_delete=models.CASCADE)
