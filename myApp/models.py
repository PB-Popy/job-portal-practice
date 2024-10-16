from django.db import models

from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),
        ('jobseeker','Jobseeker')
    ]

    usertype=models.CharField(choices=USER,max_length=100)
    profile_pic=models.ImageField(upload_to='Media/profile_pic',null=True)

    def __str__(self) -> str:
        return self.username 
    
class jobModel(models.Model):
    Employment_type=[
        ('full_time','Full_TIME'),
        ('part_time','Part_TIME')
    ]

    user=models.ForeignKey(Custom_user,max_length=100,null=True,blank=True,on_delete=models.CASCADE)
    job_title=models.CharField(max_length=100,null=True,blank=True)
    company_name=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    salary=models.PositiveIntegerField(null=True,blank=True)
    employment_type=models.CharField(choices=Employment_type,max_length=100,null=True,blank=True)
    posted_date=models.DateTimeField(auto_now_add=True)
    application_deadline=models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.job_title} at {self.company_name}"
