from django.db import models
from django.template.defaultfilters import date
from user_auth.models import User

class HealthRecord(models.Model):
    STATUS = (
    ('ongoing', 'On Going'),
    ('discharged', 'Discharged'),
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    documents = models.FileField(null=True, upload_to='healthrecords/')
    prescription = models.TextField(null=True)
    status = models.CharField(max_length=50, choices=STATUS )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medical')

    def __str__(self):
        return (self.user.username + ' - '+ str(self.created_by.first_name)+ ' - ' + str(self.status))

    @property
    def created(self):
        return '%s' % date(self.start_date, "F d, Y")
    
    @property
    def ended(self):
        if self.end_date == None:
            return str('On Going')
        return '%s' % date(self.end_date, "F d, Y")
