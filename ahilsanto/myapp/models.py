from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
	loan_no=models.CharField(max_length=10,primary_key=True)
	name=models.CharField(max_length=35)
	interest=models.IntegerField()
	date=models.DateField()
	email=models.EmailField()
class BankloanAdmin(admin.ModelAdmin):
	list_display=("loan_no","name","interest","date","email")