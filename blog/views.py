from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def home(request):
    if request.method=='POST':
        srch = request.POST['srh']

        if srch:
            match = Enroll.objects.filter(Q(name__icontains=srch)|
                                           Q(enno__icontains=srch)
                                            )
            if match:
                return render(request,'blog/home.html',{'sr':match})
            else:
                messages.error(request,'No Result Found')
        else:
            return HttpResponseRedirect('/home/')

    return render(request,'blog/home.html')




def index(request):
    obj = Enroll.objects.all()
    return render(request,'blog/index.html',{'obj':obj})

def student(request):
    if request.method == 'POST':
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studentform/')
    else:
        form = student_form()
    return render(request,'blog/student.html',{'form':form})



