from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import pdb

from TestApp1.models import Employee

# Create your views here.
def welcome_page(request):
	return HttpResponse("Hello User, Welcome to the app....")


def load_fb(request):
	return HttpResponseRedirect('https://facebook.com')


def load_admin(request):
	return HttpResponseRedirect('/welcome/')


def load_html_page(request):
	return render(request, "simple.html", {'user_names': ['test1', 'test2']})


def load_add_emp(request):
	return render(request, "create_emp.html")


def show_emp(request):
	# Connect to DB and get all the records from Employee table
	objs = Employee.objects.all()
	return render(request, 'show_emp.html', {'employee': objs})


def add_emp(request):
	# Here we can access the form data
	# We can use request parameter to access the form data.
	# request is nothing but WSGI OBJECT, Which can hold form data, Session, User's data.
	# pdb.set_trace()
	form_data = request.GET
	obj = Employee(emp_name=form_data['e_name'], 
		emp_age=form_data['e_age'], 
		emp_salary=form_data['e_salary'], emp_location=form_data['e_loc']
		)
	obj.save()

	return HttpResponseRedirect('/show_emp/')