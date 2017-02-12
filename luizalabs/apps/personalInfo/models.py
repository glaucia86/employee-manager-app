#
# Arquivo: personalInfo/models.py
# Author: Glaucia Lemos
# Data: 11/02/2017
# 
# Description: Arquivo responsável por conter todas as informações inerentes ao pacote: 'personalInfo'
# 

from django.db import models

class PersonalInfo(models.Model): 
		gender = models.CharField(max_length=10)
		age = models.IntegerField()
		birthday = models.DateField()
		phone = models.CharField(max_length=12)
		address = models.TextField()

		
	