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
    
    LOCATIONS = (
        ('AL', 'AL'),
        ('AK', 'AK'),
        ('AZ', 'AZ'),
        ('AR', 'AR'),
        ('CA', 'CA'),
        ('CO', 'CO'),
        ('CT', 'CT'),
        ('DE', 'DE'),
        ('FL', 'FL'),
        ('GA', 'GA'),
        ('HI', 'HI'),
        ('ID', 'ID'),
        ('IL', 'IL'),
        ('IN', 'IN'),
        ('IA', 'IA'),
        ('KS', 'KS'),
        ('KY', 'KY'),
        ('LA', 'LA'),
        ('ME', 'ME'),
        ('MD', 'MD'),
        ('MA', 'MA'),
        ('MI', 'MI'),
        ('MN', 'MN'),
        ('MS', 'MS'),
        ('MO', 'MO'),
        ('MT', 'MT'),
        ('NE', 'NE'),
        ('NV', 'NV'),
        ('NH', 'NH'),
        ('NJ', 'NJ'),
        ('NM', 'NM'),
        ('NY', 'NY'),
        ('NC', 'NC'),
        ('ND', 'ND'),
        ('OH', 'OH'),
        ('OK', 'OK'),
        ('OR', 'OR'),
        ('PA', 'PA'),
        ('RI', 'RI'),
        ('SD', 'SD'),
        ('SC', 'SC'),
        ('TN', 'TN'),
        ('TX', 'TX'),
        ('UT', 'UT'),
        ('VT', 'VT'),
        ('VA', 'VA'),
        ('WA', 'WA'),
        ('WV', 'WV'),
        ('WI', 'WI'),
        ('WY', 'WY'),
        )
    location = models.CharField(max_length=100, choices = LOCATIONS, default="NYA")
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
    location = models.BooleanField(max_length=5, default="False")
    charactor = models.CharField(max_length=15, choices=CHARACTORS, default="none")













