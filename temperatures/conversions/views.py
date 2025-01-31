from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Historic
from django.utils.timezone import get_current_timezone
from datetime import datetime

 
# Create your views here.
def create (request):
    if request.method == 'GET':
        return redirect ("convert")
    elif request.method == 'POST':
        username = request.POST.get("username")
    
    user = User(username=username.lower())
    user.save()
    
    return render(request,"create.html",
                  {
                      'username': username.capitalize(),
                  },
                  )
    
    



def convert (request):
    users=User.objects.all()
    return render (request, "convert.html", {"users":users})

    
def results (request):
        if request.method == 'GET':
            return redirect ("convert")
  
        if request.method == 'POST':
            username = request.POST.get("usernames").lower()

            conv= request.POST.get("conv")
            temp = float(request.POST.get("temp"))
            
            if not temp or not conv:
                return HttpResponse("Erreur : Tous les champs doivent être remplis.")

            try:
                temp= float(temp)
            except ValueError:
                return HttpResponse("Erreur : La température doit être un nombre valide.")

            if conv == "celsius":
                conv_temp = (temp* 9/5) + 32
                conv = "°C"
                result = f"{conv_temp:.2f} °F"
                initial_conv = "°C"
                final_conv = "°F"
            elif conv == "fahrenheit":
                conv_temp = (temp- 32) * 5/9
                conv = "°F"
                result = f"{conv_temp:.2f} °C"
                initial_conv = "°C"
                final_conv = "°F"
            else:
                return HttpResponse("Erreur : échelle inconnue.")
            
            user = User.objects.filter(username=username).first()
            if not user:
                return HttpResponse("Erreur : Utilisateur introuvable.")
            historique= Historic(
                user=user,
                val_initial= temp,
                val_final = conv_temp,
                time=datetime.now(tz=get_current_timezone()), 
                initial_conv=initial_conv.replace("°", ""),  # Convertit "°C" en "C"
                final_conv=final_conv.replace("°", ""),      # Convertit "°F" en "F"
            )
            historique.save()
            

            return render(request, "results.html", {
                "username":username,
                "temp": f"{temp:.2f}",
                "conv": conv,
                "result": result,
            },)
            
def historique(request, username):
    user = User.objects.filter(username=username).first()
    histories= user.historic_set.all()
    return render(request, 'historique.html',
    {
        "username":username,
        'histories': histories 
    },
    )

            
            
          
