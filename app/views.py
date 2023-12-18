from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length
from app.models import Student, Course, AccessRecord
# Create your views here.


# Insertion of Data into above models
    
def insert_course(request):
    rows=int(input('Enter No.of rows that you want to insert into Courde Model:'))
    for i in range(rows):
        cid=int(input('Nter cid:'))
        cn=input('Nter course name:')
        cd=input('Nter course details:')
        CO=Course.objects.create(cid=cid,cname=cn,c_details=cd)
        CO.save()
        
    return HttpResponse('Inserted successfully')




def insert_student(request):
    rows=int(input('Nter no.of rows that you want to insert into Student Model:'))
    for i in range(rows):
        i=int(input())
        n=input()
        c_type=input()
        cid=int(input())
        GO=Course.objects.get(cid=cid)
        SO=Student.objects.create(c_id=GO,std_id=i,std_name=n,std_courst=c_type)
        SO.save()
    return HttpResponse('Student Inserted Successfully')

def insert_accessRecord(request):
    rows=int(input('Nter no.of rows you want to insert into Access Record:'))
    for i in range(rows):
        pk=int(input())
        ass=input()
        ad=input()
        GO=Student.objects.get(pk=pk)
        AO=AccessRecord.objects.create(std_name=GO,assigned_staff=ass,access_date=ad)
        AO.save()
    return HttpResponse('Access Records inserted successfully')





def display_course(request):
    obj=Course.objects.all()
    obj=Course.objects.order_by('cname')
    obj=Course.objects.order_by('c_details')
    obj=Course.objects.order_by('-cid')
    obj=Course.objects.filter(cid=1) # keyword cid shouldn't be repeated
    obj=Course.objects.filter()# Displays all data as there is no filter condition
    obj=Course.objects.filter(cid=5)
    obj=Course.objects.filter(cid=5,cname='Python') # Work like and b/w given field names 
    #obj=Course.objects.order_by(Length()) #Length' takes exactly 1 argument (0 given)
    obj=Course.objects.order_by(Length('cname')) # Length works with only string 
    obj=Course.objects.order_by(Length('cid')) # Even it order with the numbers
    obj=Course.objects.order_by(Length('cid').desc())
    obj=Course.objects.order_by(Length('cname').asc())
    obj=Course.objects.order_by(Length('cid').desc())
    obj=Course.objects.order_by('cname','-cid') # We can order by more than one field 
    obj=Course.objects.exclude(cname='Python')
    d={'obj':obj}
    return render(request,'display.html',d)

def display_student(request):
    obj=Student.objects.all()
    d={'obj':obj}
    return render(request,'display_stdnt.html',d)

def display_accessRecord(request):
    obj=AccessRecord.objects.all()
    d={'obj':obj}
    return render(request,'display_arec.html',d)





