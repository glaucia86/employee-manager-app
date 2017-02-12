#
# Arquivo: employee/models.py
# Author: Glaucia Lemos
# Data: 11/02/2017
# 
# Description: Arquivo responsável por conter todas as informações inerentes ao pacote: 'employee'
# 

from django.db import models

# Importando o pacote para poder fazer o relacionamento de 1 para 1
from apps.personalInformation.models import PersonalInformation


class Employee(models.Model): 
		employee_id = models.CharField(max_length=10, primary_key=True)
		name = models.CharField(max_length=50)
		email = models.EmailField(max_length=30)
		departament = models.CharField(max_length=50)
		# Aqui realizando o relacionamento de 1 para 1:
		personalInformation = models.OneToOneField(PersonalInformation, null=True, blank=True, on_delete=models.CASCADE)
