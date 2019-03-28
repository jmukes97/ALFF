from django.db import models

# Create your models here.
class user(models.Model):
    criteria = models.ForeignKey('SearchCriteria',on_delete=models.PROTECT, null=True)
    email = models.CharField(max_length=30, primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.CharField(max_length=30)
    DEVICES = (
    ('ps4', 'Playstation'),
    ('xb1', 'Xbox'),
    ('pc', 'PC'),
    ('none', 'NONE')
    )
    device = models.CharField(max_length=4, choices=DEVICES, default="none")
    hasMic = models.BooleanField(default=False)
    CHARACTORS = (
    ('Bangalore', 'Bangalore'),
    ('Gibraltar', 'Gibraltar'),
    ('Mirage', 'Mirage'),
    ('Lifeline', 'Lifeline'),
    ('Bloodhound', 'Bloodhound'),
    ('Caustic', 'Caustic'),
    ('Octane', 'Octane'),
    ('Pathfinder', 'Pathfinder'),
    ('Wraith', 'Wraith'),
    ('none', 'NYA'),
    )
    
    location = models.CharField(max_length=100, default="NYA")
    charactor = models.CharField(max_length=15, choices=CHARACTORS, default="none")

class SearchCriteria(models.Model):
    age = models.CharField(max_length=30, default="20")
    DEVICES = (
    ('ps4', 'Playstation'),
    ('xb1', 'Xbox'),
    ('pc', 'PC'),
    ('none', 'NONE')
    )
    device = models.CharField(max_length=4, choices=DEVICES, default="none")
    hasMic = models.BooleanField(default=False)
    CHARACTORS = (
    ('Bangalore', 'Bangalore'),
    ('Gibraltar', 'Gibraltar'),
    ('Mirage', 'Mirage'),
    ('Lifeline', 'Lifeline'),
    ('Bloodhound', 'Bloodhound'),
    ('Caustic', 'Caustic'),
    ('Octane', 'Octane'),
    ('Pathfinder', 'Pathfinder'),
    ('Wraith', 'Wraith'),
    ('none', 'NYA'),
    )
    location = models.CharField(max_length=100, default="NYA")
    charactor = models.CharField(max_length=15, choices=CHARACTORS, default="none")













