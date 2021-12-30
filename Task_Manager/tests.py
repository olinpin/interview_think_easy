from django.test import TestCase

from django.contrib.auth.models import User, UserManager
from .models import Tasks

# Create your tests here.

class TasksModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="oliverhnat")  
        user = User.objects.get(username="oliverhnat")
        Tasks.objects.create(user=user, title="Shopping list", text="Bananas", done=False)

    def test_task_max_length(self):
        task = Tasks.objects.get(id=1)
        max_length = task._meta.get_field('title').max_length
        self.assertEqual(max_length, 128)
    
    def test_object_string_output(self):
        task = Tasks.objects.get(id=1)
        expected_output = f"{task.title} - {task.text} from {task.user}, done is {task.done}"
        self.assertEqual(str(task), expected_output)


        