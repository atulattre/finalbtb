from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import User1


from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def cp(request):
    if request.method=='POST':
        username=request.user
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        student_id=request.POST.get('student_id')
        phone=request.POST.get('phone')
        branch=request.POST.get('branch')
        year=request.POST.get('year')
        building_name=request.POST.get('building_name')
        room_number=request.POST.get('room_number')
        room_type=request.POST.get('room_type')
        space=request.POST.get('space')
        rent=request.POST.get('rent')
        images1=request.FILES.get('images1')
        
        
        print(images1)
        
        comments=request.POST.get('comments')
        new_user=User1(username=username,firstname=firstname,lastname=lastname,student_id=student_id,phone=phone,branch=branch,year=year,building_name=building_name,room_number=room_number,room_type=room_type,space=space,rent=rent,images1=images1,comments=comments)
        new_user.username=username
        
        

        
        
        new_user.save()

        

       
        
        return render(request,'home.html')



    return render(request,'cp.html')


def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request,'login.html')

def signuppage(request):
    if request.method=='POST':
        username=request.POST.get('username')
       
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
       
        
        if password!=confirm_password:
            return HttpResponse("password and confirm password are different")
        elif password==confirm_password:
            my_user=User.objects.create_user(username,email,password)
            my_user.save()
            
            return redirect('loginpage')
    elif request.method=='GET':
        return render(request,'signup.html')
    else:
        return HttpResponse('An exception occured!Try again')
        

    return render(request,'signup.html')
def all_flat(request):
    flats=User1.objects.all()
    
    context={
        'flats':flats
    }
    
    print(context)
    return render(request,'card.html',{ 'flats':flats})
    


def contact(request,id):
    flats1=User1.objects.get(id=id)
    context={
        'flats1':flats1
    }
    print(flats1)
    return render(request,'contact.html',{'flats1':flats1})


        







