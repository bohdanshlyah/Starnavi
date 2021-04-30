from django.db import models
from User.models import CustomUser
# from django.contrib.auth import get_user_model
# User = get_user_model()

class Post(models.Model):
    title = models.CharField(blank=False, max_length=20)
    content = models.TextField(blank=True, max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_date = models.DateField(format('%Y-%M-%D'), auto_now_add=True, editable=False)
