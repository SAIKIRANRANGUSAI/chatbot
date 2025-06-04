from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service_type = models.CharField(max_length=100)
    requirements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SupportTicket(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    project_id = models.CharField(max_length=50)
    issue = models.TextField()
    browser = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.project_id}"
