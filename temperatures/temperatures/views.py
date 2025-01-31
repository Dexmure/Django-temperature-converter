#from django.http import HttpResponse
from django.shortcuts import render
def home(request):
   # return HttpResponse("Azul fellawen soumatha")
    return render(request, 'homepage.html')
