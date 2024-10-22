# Ex02 Django ORM Web Application
## Date: 22.10.24

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](Bankloan.png)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

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

admin.py

from django.contrib import admin
from .models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)

```

## OUTPUT

Include the screenshot of your admin page.
![alt text](<bankloan screenshot.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
