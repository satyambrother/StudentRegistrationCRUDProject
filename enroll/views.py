from django.shortcuts import render
from enroll.forms import StudentRegistration
from .models import Users
from django.http import HttpResponseRedirect

# Create your views here.

#This Function Show all Record and New Item 
def add_show(request):
    if request.method == 'POST':
       fm=StudentRegistration(request.POST)
       if fm.is_valid():
          nm=fm.cleaned_data['name']
          em=fm.cleaned_data['email']
          ps=fm.cleaned_data['password']
          reg=Users(name=nm,email=em,password=ps)
          reg.save()
          fm=StudentRegistration() 
          
    else:
         fm=StudentRegistration() 
    stud=Users.objects.all()  
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

# This Function will  delete
def delete_data(request,id):
    if request.method == 'POST':
       pi=Users.objects.get(pk=id)
       pi.delete() 
       return HttpResponseRedirect('/')

# This Function Update and Delete
def update_data(request,id):
    if request.method == 'POST':
       pi=Users.objects.get(pk=id)
       fm=StudentRegistration(request.POST,instance=pi)
       if fm.is_valid():
          fm.save()
    else:
        pi=Users.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)      

    return render(request,'enroll/updatestudent.html',{'form':fm})



