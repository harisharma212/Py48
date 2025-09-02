from django.db import models

# Create your models here.

class Employee(models.Model):
	emp_name = models.CharField(max_length=150)
	emp_age = models.IntegerField()
	emp_location = models.CharField(max_length=150)
	emp_salary = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.emp_name

