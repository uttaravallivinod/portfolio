from django.shortcuts import render,redirect
from ppage.models import Messages
from django.contrib import messages

# Create your views here.

def home(request):


    messages.info(request," vinod kumar")

    return render(request,'index.html')

def message(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        try:
            m=Messages.objects.create(name=name,email=email,message=message)
            m.save()
            messages.info(request,'Your Message Sent Succussfully')
            print('hi')
            return redirect('/')
        except:
            messages.info(request,'Your Message Sent Succussfully')

            return redirect('/')
