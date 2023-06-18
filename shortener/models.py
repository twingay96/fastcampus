from django.db import models
# from django.contrib.auth.models import User as U
from django.contrib.auth.models import AbstractUser

class PayPlan(models.Model):
    name= models.CharField(max_length=20)
    price= models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)    # 매번 업데이트 되는 시간
    create_at = models.DateTimeField(auto_now_add=True) # 처음생성된 시간

class Users(AbstractUser):
    pay_plan = models.ForeignKey(PayPlan,on_delete=models.DO_NOTHING, null= True)   # default 는 null 허용

class UserDetail(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)
