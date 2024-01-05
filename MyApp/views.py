from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from .models import Upload_File
from .forms import RegistationForm,LoginForm,UploadForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "MyApp/index.html")


def signup(request):
    if request.method == "POST":
        form=RegistationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Account created Successfully!")
            return HttpResponseRedirect("/signup")
    else:   
        form=RegistationForm()
    return render(request, "MyApp/signup.html", {'form':form})


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user=authenticate(request, email=email, password=password)
        if user is None:
            messages.error(request, "Details may incorrect")
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/index')
    else:       
        form=LoginForm()
    return render(request, "MyApp/login.html",{"form":form})

class CreateUploadView(View):
    def get(self,request):
        form=UploadForm
        return render(request,"MyApp/uploads_file.html" ,{
            "form":form
        })
    
    #@login_required
    def post(self,request):
        submitted_form=UploadForm(request.POST,request.FILES)
        if submitted_form.is_valid():
            uploads=Upload_File(upload=request.FILES["upload"])
            uploads.save()
            messages.error(request, "File Uploaded Successfully")
            return redirect('/upload')
        
        return render(request,"MyApp/uploads_file.html" ,{
            "form":submitted_form
        })
    
def file_list(request):
    files=Upload_File.objects.all()
    return render(request, 'MyApp/file_list.html',{
        "files": files
    })