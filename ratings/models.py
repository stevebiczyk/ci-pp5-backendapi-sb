from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe


# class Like(models.Model):
#     """
#     Like model, related to 'owner' and 'post'.
#     'owner' is a User instance and 'post' is a Post instance.
#     'unique_together' makes sure a user can't like the same post twice.
#     """
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(
#         Post, related_name='likes', on_delete=models.CASCADE
#     )
#     created_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ratings'
        )
    stars = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.user.username} - {self.recipe.title}'

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'recipe']

    def __str__(self):
        return f'{self.owner} {self.recipe.title}'
