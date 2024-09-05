from django.shortcuts import render,redirect
from . models import regtb2


def index(request):
    return render(request,"home.html")

def add(request):
    if request.method=='POST':
        name1=request.POST.get('nm')
        date1=request.POST.get('da')
        obj=regtb2.objects.create(taskname=name1,taskdate=date1)
        obj.save()
        if obj:
            return render(request,"home.html")
        else:
            return render(request,"add.html")  
    else:
        return render(request,"add.html")  

def view(request):
    obj=regtb2.objects.all()
    return render(request,"view.html",{'data':obj})  


def edit(request):
    id_value= request.GET.get('idn')
    obj=regtb2.objects.filter(id=id_value)
    return render(request,"edit.html",{'data':obj})

def update(request):
    if request.method=='POST':
        name1=request.POST.get('nm')
        date1=request.POST.get('da')
        idno=request.POST.get('idno')
        obj=regtb2.objects.get(id=idno)
        obj.taskname=name1
        obj.taskdate=date1        
        obj.save()
        return redirect('/view')

def delete(request):
    id_value= request.GET.get('idn')       
    obj=regtb2.objects.filter(id=id_value)
    obj.delete()
    return redirect('/view')