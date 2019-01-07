from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from .models import Case, Profile, Passwords
from .encryption import encrypt
# Create your views here.
def is_valid(request):
    u=request['username_input']
    p=request['password_input']
    m=request['number_input']
    if u != None and p!= None and m!= None:
        return True
    return False
        
def register(request):
    print(request.method)
    if request.method=='POST':
        print(request.POST)
        form = RegisterForm(request.POST)
        print(form)
        if is_valid(request.POST):
            #Save input in database
            print(request)
            case = Case()
            case.username = request.POST['username_input']
            case.password = request.POST['password_input']
            x,y = encrypt(case.password)
            case.password = x
            case.phone_number = request.POST['number_input']
            profile = Profile()
            profile.save()
            case.place = profile
            case.save()
            context = {}
            return render(request, 'account/login.html', context)
        else:
            blank_form = RegisterForm()
            context = {'form': blank_form}
            return render(request, 'account/register.html', context)
    else:   #if get method, create a blank form.
        blank_form = RegisterForm()
        context = {'form': blank_form}
        return render(request, 'account/register.html', context)


def login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #Save input in database
            inpusername = form.cleaned_data.get("inpusername")
            inppassword = form.cleaned_data.get("inppassword")
            CaseObjList = Case.objects.all()
            ReqObj = None
            for obj in CaseObjList:
                if obj.username==inpusername and obj.password==inppassword:
                    ReqObj = obj
                    break
            if ReqObj==None:
                blank_form = LoginForm()
                context = {'form': blank_form}
                return render(request, 'account/login.html', context)
            #
            #
            #Collect all data of ReqObj and send it to template.
            #
            #
            context = {}
            return render(request, 'account/profile.html', context)
        else:
            blank_form = LoginForm()
            context = {'form': blank_form}
            return render(request, 'account/login.html', context)
    else:   #if get method, create a blank form.
        blank_form = LoginForm()
        context = {'form': blank_form}
        return render(request, 'account/login.html', context)
