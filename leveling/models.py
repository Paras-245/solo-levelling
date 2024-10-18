from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=255, default='E')
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    goal = models.CharField(max_length=100)
    goal_progress = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    day = models.IntegerField(default=1)
    mana = models.IntegerField(default=100)

    def __str__(self):
        return self.user.username
    
class Quest(models.Model):
    title = models.CharField(max_length=200)
    objective = models.TextField()
    tasks = models.JSONField()  # Store tasks as a list of strings
    day = models.IntegerField()  # Store the day number for the quest
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title

class UserQuest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    completed_tasks = models.JSONField(default=list)  # Store completed tasks as a list of strings

    def is_completed(self):
        return set(self.completed_tasks) == set(self.quest.tasks)