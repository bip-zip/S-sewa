from django.db import models
from user_auth.models import User
# customize many to many field django

class Medicine(models.Model):
    name = models.CharField(max_length=200, null=False)
    desc = models.TextField(null=True)
    dose = models.CharField(max_length=100, null=False)
    price =  models.IntegerField(null=False)

    def __str__(self) -> str:
        return super().__str__(self.name, '-' ,self.dose)
    
    
class MedicationSchedule(models.Model):
    #  many to many field --- search it out
     created_date = models.DateTimeField(auto_now_add=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='institution')

     def __str__(self) -> str:
         return super().__str__(self.user.username)

