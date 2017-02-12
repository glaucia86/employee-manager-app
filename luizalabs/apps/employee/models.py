
#
# Arquivo: employee/models.py
# Author: Glaucia Lemos
# Data: 11/02/2017
# 
# Description: Arquivo responsável por conter todas as informações inerentes ao pacote: 'employee'
# 

from django.db import models

from apps.personalInfo.models import PersonalInfo

class Employee(models.Model): 
		name = models.CharField(max_length=50)
		email = models.EmailField(max_length=30)
		departament = models.CharField(max_length=50)

		# Aqui estou fazendo o relacionando de 1 para * 
		personalInfo = models.ForeignKey(PersonalInfo, null=True, blank=True, on_delete=models.CASCADE)