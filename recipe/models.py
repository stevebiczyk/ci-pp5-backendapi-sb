from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', 'Easy'),
        ('Intermediate', 'Intermediate'),
        ('Hard', 'Hard'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='recipes')
    cooking_time = models.IntegerField(null=True, blank=True)  # in minutes
    servings = models.IntegerField(null=True, blank=True)
    difficulty_level = models.CharField(choices=DIFFICULTY_LEVELS, max_length=20, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
