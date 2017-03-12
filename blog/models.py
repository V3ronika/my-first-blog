from django.db import models
from django.utils import timezone #utils is a model with useful shortcuts

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200) #limited length for title
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save() #predefined function in django

    def __str__(self):
        return self.title #output = titulok postu alebo co si tam dam
