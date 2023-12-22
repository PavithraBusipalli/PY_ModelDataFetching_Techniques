from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length
from app.models import Student, Course, AccessRecord
from django.db.models import Q
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
    
# Lookups : used for performing comparison and some other operations
    # lt, lte, gt, gte, startswith, endswith, contains
    obj=Course.objects.filter(cid__lt=3)
    obj=Course.objects.filter(cid__lte=4)
    obj=Course.objects.filter(cid__gt=6)
    obj=Course.objects.filter(cid__gte=4)
    obj=Course.objects.filter(cname__startswith='d') # Irrespective of case it will match 
    obj=Course.objects.filter(c_details__endswith='org')
    obj=Course.objects.filter(c_details__contains='p') # Search for entire means start,end and middle also

# UPDATE Model - update() or update_or_create()
    #obj=Course.objects.filter(cname='Java').update(cid=10)
    #obj=Course.objects.filter(cid=6).update(cname='Django')
    #obj=Course.objects.filter(cid=6).update(c_details='http://django.com')
    #obj=Course.objects.filter(cname='Django').update(cid=100) # Even primary will get updated if you're dealing with the parent table
    #obj=Course.objects.filter(cname='AWS').update(cid=100) - Unique constraint fail
    OBJ=Course.objects.get(cid=100)
    #obj=Course.objects.update_or_create(cname='Django',c_details='http://django/com',defaults={'cid':100})
    obj=Course.objects.all()
    d={'obj':obj}
    return render(request,'display.html',d)

def display_student(request):
    obj=Student.objects.all()
    #obj=Student.all()
    # Filter with 'and' and 'or' conditions
    obj=Student.objects.filter(std_name='Pavi',std_courst='offline') # , works like and at here
    obj=Student.objects.filter(Q(std_name='Lucky') & Q(std_courst='offline'))
    obj=Student.objects.filter(Q(c_id=3) | Q(c_id=4) | Q(c_id=5)) # or cond repsn
    obj=Student.objects.filter(Q(std_id=3) & Q(std_name__endswith='y') & Q(c_id=3))
    obj=Student.objects.filter()
    obj=Student.objects.filter(std_id=4).update(std_courst='online')
    obj=Student.objects.filter(std_id=1).update(std_courst='online')
    OBJ=Course.objects.get(cid=1)
    #obj=Student.objects.update_or_create(std_courst='online',defaults={'c_id':OBJ}) ---> Multiple objects can not be handled by get_or_create
    obj=Student.objects.get_or_create(std_id=6,defaults={'c_id':OBJ,'std_name':'Pavi'})
    obj=Student.objects.filter(std_id=6).update(std_courst='offline')
    obj=Student.objects.filter(std_name='Supra').update(c_id=3)
    obj=Student.objects.all()
    d={'obj':obj}
    return render(request,'display_stdnt.html',d)

def display_accessRecord(request):
    obj=AccessRecord.objects.all()
    obj=AccessRecord.objects.filter(access_date__year='2023')
    obj=AccessRecord.objects.filter(access_date__month='12')
    obj=AccessRecord.objects.filter(std_name__in=(1,2))  # std_name ---> pk values of Student Table
    d={'obj':obj}
    return render(request,'display_arec.html',d)





