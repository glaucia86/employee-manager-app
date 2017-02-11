#
# Arquivo: employee/models.py
# Author: Glaucia Lemos
# Data: 11/02/2017
# 
# Description: Arquivo responsável por conter todas as informações inerentes ao pacote: 'employee'
# 

from django.db import models

# Create your models here.

class Employee(models.Model): 
		employee_id = models.CharField(max_length=10, primary_key=True)
		name = models.CharField(max_length=50)
		email = models.EmailField(max_length=30)
		departament = models.CharField(max_length=50)
