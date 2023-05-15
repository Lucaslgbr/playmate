from django.db import models

class DeployScript(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied=models.DateTimeField(auto_now_add=True)
