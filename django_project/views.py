import json
from django.shortcuts import render
from django.conf import settings
# Create your views here.
def about(request):
	return render(request, "about.html", {})
def schedule(request):
	return render(request, "schedule.html", {})
def index(request):
	return render(request, "index.html", {})

def team(request):
	return render(request, "secretariat.html", {})

def registrationform(request):
	return render(request, "form.html")

def reg(request):
	return render(request, "registration.html", {})

def ga(request):
	return render(request, "ga.html", {})

def sa(request):
	return render(request, "sa.html", {})

def crisis(request):
	return render(request, "crisis.html", {})

def travel(request):
	return render(request, "travel.html")

def staff(request):
	return render(request, "staff.html", {})

def contact(request):
	return render(request, "contact.html", {})

def faq(request):
	return render(request, "faq.html", {})
# def sponsors(request):
# 	return render(request, "sponsors.html", {})

def committees(request):
	return render(request, "committees.html", {})

def comingsoon(request):
	return render(request, "coming-soon.html", {})

def positionpaperReceived(request):
	return render(request, "positionpaperReceived.html", {})
# def thankyou(request):
# 	return render(request, "thankyou.html", {})

# def faq(request):
# 	return render(request, "faq/index.html", {})
