from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Signup_form,Login_form
import subprocess
from oameni.models import Profesor 

#dummy placeholder
def main_page(request):
    if 'utilizator_id' in request.session:
        context = {}
        return render(request,"index.html",context)
    return redirect('login')

#logout quick function , testing only 

def logout_user(request):
    request.session.flush()  # scoate sessiunea mea
    return redirect('login')


# SIGNUP /CREATE 
# USER DONT TOUCH!!!!!!!!!!
# WORK JUST FINE 
def create_user(nume_prof,prenume_prof,email_prof,coordonator_status_nou,parola_nou):
    
    if not nume_prof or not prenume_prof or not email_prof or not parola_nou:
        raise ValueError("Toate câmpurile sunt obligatorii!")
    
    prof_nou = Profesor(nume = nume_prof,
                        prenume = prenume_prof,
                        email = email_prof,
                        coordonator_status = coordonator_status_nou,
                        parola = parola_nou)
    prof_nou.save()


def send_password (request):
    email_scriptpath = "/home/out/proggramer_stuff/webstite_projects/lrdv_2025/lrdv_back/automatic_pass_sender/email_sender.py"
    parola_scriptpath  = "/home/out/proggramer_stuff/webstite_projects/lrdv_2025/lrdv_back/automatic_pass_sender/password_maker.py"
    nume = prenume = email = coordonator_status = None
    parola =   subprocess.run(#da run lascript de creare email si trimitere
                    ["python3", parola_scriptpath],
                    check=True,
                    capture_output=True,
                    text=True
            ).stdout.strip()
    
    context = {}

    if request.method =="POST":
        form = Signup_form(request.POST)
        if form.is_valid() :

            nume = form.cleaned_data["nume"]#ia datele de la email de pe pag
            prenume = form.cleaned_data["prenume"]
            email = form.cleaned_data["email"]
            coordonator_status = form.cleaned_data["coordonator_status"]

            subprocess.run(#da run lascript de creare email si trimitere
                    ["python3", email_scriptpath, email,parola],
                    check=True,
                    capture_output=True,
                    text=True
            
            )
            create_user(nume,prenume,email,coordonator_status,parola)
            
    else:
        form = Signup_form()
            
    context['form'] = form

    

    return render(request,"register/signup.html",context)

#PROFESOR LOGIN
#merge good
def login_user(request):
    context = {}
    
    if request.method == "POST":

        form = Login_form(request.POST)
        
        if form.is_valid():

            email = form.cleaned_data['email'] #get email form db
            password = form.cleaned_data['parola'] #get password form db

            try:
                utilizator = Profesor.objects.get(email=email) #scaneaza utilizator in functie de mail
                if utilizator.parola == password: #verifica parola

                    request.session['utilizator_id'] = utilizator.id #face session ca sa verifice daca avem user
                    return redirect ("index") #mookup,to change la pagina principala
                else:

                    form.add_error(None, "parola gresita")
            except Profesor.DoesNotExist:
                form.add_error(None, 'utilizator nu exista')
    else:
        form = Login_form()

    context['form'] = form

    return render(request, "register/login.html", context)
    