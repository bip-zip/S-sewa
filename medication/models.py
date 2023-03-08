from django.db import models
from user_auth.models import User
# customize many to many field django

class Medicine(models.Model):
    name = models.CharField(max_length=200, null=False)
    desc = models.TextField(null=True)
    dose = models.CharField(max_length=100, null=False)
    price =  models.IntegerField(null=False)

    def __str__(self):
        return ("{} - {} mmhg".format(self.name,str(self.dose)))
    
    
class MedicationSchedule(models.Model):
    #  many to many field --- search it out
    medicine = models.ManyToManyField(Medicine, related_name='medicine', through='MedicineMedicationSchedule')
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='institution')

    def __str__(self):
        return self.user.username
    
    @property
    def allmedicines(self):
        return MedicineMedicationSchedule.objects.filter(medicationSchedule = self.id)


class MedicineMedicationSchedule(models.Model):
    TIME_CHOICES = (
    ('morning', 'Morning'),
    ('morning&evening', 'Morning & Evening'),
     ('morning&afternoon&evening','Morning, Afternoon & Evening'),
    )
    medicationSchedule = models.ForeignKey(MedicationSchedule, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    desc = models.CharField(max_length=2000, null=True)
    timesaday= models.CharField(null=False, max_length=50, choices=TIME_CHOICES)
    emptyStomach = models.BooleanField(default=False) 

    def __str__(self):
        return (self.medicationSchedule.user.username)

