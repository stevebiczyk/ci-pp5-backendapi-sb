from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', 'Easy'),
        ('Intermediate', 'Intermediate'),
        ('Hard', 'Hard'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(null=True, blank=True)  # in minutes
    image = models.ImageField(upload_to='images/', default='../girl_climbing_gxt5ti', blank=True)
    difficulty_level = models.CharField(choices=DIFFICULTY_LEVELS, max_length=20, null=True, blank=True)
    # categories = models.ManyToManyField(Category)
    # ratings = models.models.PositiveIntegerField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
