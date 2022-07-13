# from cgitb import text
# from distutils.command.upload import upload
# from logging import PlaceHolder
# from pyexpat import model
from django.db import models
# from django.db.models.signals import post_save,pre_save
# from decimal import Decimal
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.db.models import Sum
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from .sendmails import *






#creating an id for registration
def customer_generate_id():
    try:
        id=Registration.objects.count()
        if id is not None:
            return f"TKI{2003+id}"
        else:
            return f"TKI{2003}"
    except Exception as e:
        print(e)


#Registration table:
class Registration(AbstractUser):
    first_name=models.CharField(max_length=60, null=True, blank=True) 
    last_name=models.CharField(max_length=60, null=True, blank=True) 
    fullname=models.CharField(max_length=60,null=True,blank=True)
    location=models.TextField(null=True,blank=True)
    gender=models.CharField(max_length=6,null=True,blank=True)
    image=models.ImageField(upload_to='image',null=True,blank=True)
    id=models.CharField(max_length=10, default=customer_generate_id,primary_key=True,editable=False)
    mobile_no=models.CharField(max_length=13)
    otp=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural='user'





#creating a id for Project_Detail
def project_detail_id():
    try:
        id=ProjectDetail.objects.count()
        if id is not None:
            return f"TKI{1003+id}"
        else:
            return f"TKI{1003}"
    except Exception as e:
        print(e)
        
   
class ProjectDetail(models.Model):
    user=models.ForeignKey(Registration,related_name='project_detail',on_delete=models.CASCADE)
    id=models.CharField(max_length=10,default=project_detail_id,primary_key=True,editable=False)
    project_detail=models.CharField(max_length=100)
    booking_amount=models.DecimalField(default=0.0,max_digits=10,decimal_places=2)
    total_project_value=models.DecimalField(default=0.0,max_digits=10,decimal_places=2) 
    project_booking_date=models.DateTimeField(null=True,blank=True)
    remaining_amount=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    # new_payment=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    
    
    def __str__(self):
        return self.project_detail
    
    def remaining_amount(self):
        return self.total_project_value-self.booking_amount
    
    # class Meta:
    #     verbose_name_plural='total_project_value'






#creating an id for payment_tracker
def payment_tracker_generate_id():
    try:
        id=PaymentTracker.objects.count()
        print("count----",id)
        if id is not None:
            return f"TKI{1001+id}"
        else:
            return f"{1001}"

    except Exception as e:
        print(e)

class PaymentTracker(models.Model):
    user = models.ForeignKey(Registration,related_name='payment_tracker',on_delete=models.CASCADE)
    id = models.CharField(max_length=10,default=payment_tracker_generate_id,primary_key=True)
    project_id=models.ForeignKey(ProjectDetail,related_name='project_details',on_delete=models.CASCADE)
    project_detail=models.ForeignKey(ProjectDetail,related_name='project',on_delete=models.CASCADE)
    # project_id = models.CharField(max_length=10,null=True,blank=True)
    # total_project_value = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    total_paid = models.DecimalField(max_digits=10,decimal_places=2)
    # total_amount_due = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    payment_mode = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='Payment Tracker'

    # def total_amount_due(self):
    #     return self.total_project_value-self.total_paid









#creating an id for project_tracker
# def project_tracker_generate_id():
#     try:
#         id=ProjectTracker.objects.count()
#         if id is not None:
#             return f"TKI{1003+id}"
#         else:
#             return f"TKI{1003}"
#     except Exception as e:
#         print(e)
        
        
        
#creating model for ProjectTracker
# class ProjectTracker(models.Model):
#     id=models.CharField(max_length=10,default=project_tracker_generate_id,primary_key=True,editable=False)
#     username=models.ForeignKey(Registration,related_name='project_tracker',on_delete=models.CASCADE)
#     client_metting=models.CharField(max_length=200)
#     planning=models.CharField(max_length=200)
#     design_ui_ux=models.FloatField(default=0.0)
#     analysis=models.FloatField(default=0.0)
#     manipulation=models.FloatField(default=0.0)
#     testing=models.FloatField(default=0.0)
#     handover=models.CharField(max_length=200)
    
    
#     def __str__(self):            
#         return self.id

#     class Meta:
#         verbose_name_plural='Project Tracker'
        
        
#     def calculate_percentage(self):
#         count = 0
#         sum = 0
#         try:
#             sum = sum + self.planning
#             count = count + 1
#         except:
#             sum = sum
#             count = count

#         try:
#             sum = sum + self.design_ui_ux
#             count = count + 1
#         except:
#             sum = sum
#             count = count

#         try:
#             sum = sum + self.analysis
#             count = count + 1
#         except:
#             sum = sum
#             count = count

#         try:
#             sum = sum + self.manipulation
#             count = count + 1
#         except:
#             sum = sum
#             count = count
        
#         try:
#             sum = sum + self.testing
#             count = count + 1
#         except:
#             sum = sum
#             count = count

#         p= sum/count
#         return p/100

#     def get_planning(self):
#         return self.planning/100
    
    
      
#     def get_design_ui_ux(self):
#         return self.design_ui_ux/100




#     def get_analysis(self):
#         return self.analysis
    



#     def get_manipulation(self):
#         return self.manipulation

#     def get_testing(self):
#         return self.testing

                                



# creating an id for project_tracker:
def project_tracker_generate_id():
    try:
        id=ProjectTracker.objects.count()
        if id is not None:
            return f"TKI{1003+id}"
        else:
            return f"TKI{1003}"
    except Exception as e:
        print(e)

     
#creating model for ProjectTracker:
class ProjectTracker(models.Model):
    id=models.CharField(max_length=10,default=project_tracker_generate_id,primary_key=True)
    user=models.ForeignKey(Registration,related_name='project_tracker',on_delete=models.CASCADE)
    # project_id=models.ForeignKey(ProjectDetail,related_name='project_tacker',on_delete=models.CASCADE)
    client_meeting=models.CharField(max_length=250,blank=True,null=True)
    planning=models.CharField(max_length=250,blank=True,null=True)
    requirements=models.CharField(max_length=250,blank=True,null=True)
    design_ui_ux=models.CharField(max_length=250,blank=True,null=True)
    framework=models.CharField(max_length=250,blank=True,null=True)
    approval=models.CharField(max_length=250,blank=True,null=True)
    development=models.CharField(max_length=250,blank=True,null=True)
    testing=models.CharField(max_length=250,blank=True,null=True)
    release=models.CharField(max_length=250,blank=True,null=True)
    handover=models.CharField(max_length=250,blank=True,null=True)

    
    def __str__(self):
        return str (self.user + " - " + self.id)

    
    





   

#creating a id TeamName
def team_name_id():
    try:
        id=TeamName.objects.count()
        if id is not None:
            return f"TKI{1003+id}"
        else:
            return f"TKI{1003}"
    except Exception as e:
        print(e)
 


class TeamName(models.Model):
    id=models.CharField(max_length=10,default=team_name_id,primary_key=True,editable=False)
    designation=models.CharField(max_length=80,blank=True, null=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    profile_image=models.ImageField(upload_to='profile_image/',blank=True,null=True)
    email=models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return str (self.name + " - " + self.email)


class TeamAssign(models.Model):
    user=models.ForeignKey(Registration,related_name='Teama',on_delete=models.CASCADE,null=True, blank=True)
    project=models.ForeignKey(ProjectDetail,related_name='Teamsa',on_delete=models.CASCADE, null=True, blank=True)
    team= models.ManyToManyField(TeamName, related_name="team_lista",blank=True,)

    def __str__(self):
        return str (self.user.username)

    



# class TeamAssign(models.Model):
#     user=models.ForeignKey(Registration,related_name='Teamassign',on_delete=models.CASCADE,null=True, blank=True)
#     designation=models.CharField(max_length=250)

#     def __str__(self):
#         return str (self.user.username)

    





