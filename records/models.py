from django.db import models
from django.template.defaultfilters import date
from user_auth.models import User

class HealthRecord(models.Model):
    STATUS = (
    ('ongoing', 'On Going'),
    ('discharged', 'Discharged'),
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    documents = models.FileField(null=False, upload_to='healthrecords/')
    prescription = models.TextField(null=True)
    status = models.CharField(max_length=50, choices=STATUS )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medical')

    def __str__(self):
        return (self.user.username + ' - '+ str(self.created_by.first_name)+ ' - ' + str(self.status))


