from django.shortcuts import render

def schedule(request):
  return render(request, 'schedule.html')

def instructors(request):
  return render(request, 'instructors.html')

def index(request):
  return render(request, 'index.html')

def generateSchedule(request):
  return render(request, 'generate-schedule.html')

def forgetPassword(request):
  return render(request, 'forget-password.html')

def login(request):
  return render(request, 'login.html')
