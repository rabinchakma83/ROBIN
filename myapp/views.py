
from django.shortcuts import render,redirect

from .models import student,CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required

# Create your views here.
def home(request):

    name = "robin"
    students = student.objects.all()
    return render(request, 'index.html', {'dict_name': name, 'students': students})


def addstudent(request):

    students = student.objects.all()

    if request.method =="POST":
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        cgpa = request.POST.get('cgpa')

        new_student = student(
            name = name,
            roll = roll,
            department = department,
            semester = semester,
            cgpa = cgpa,

        )
        new_student.save()


    return render(request, "addstudent.html",{"students":students})

def studentIdCall(request, id ):

    students = student.objects.get(id =id)

    
    return render(request, 'update_student.html',{"students": students})

def updateStudent (request):
     
    if request.method =="POST":
            name = request.POST.get('name')
            roll = request.POST.get('roll')
            department = request.POST.get('department')
            semester = request.POST.get('semester')
            cgpa = request.POST.get('cgpa')
            id = request.POST.get('id')

    
            new_student = student(
                name = name,
                roll = roll,
                department = department,
                semester = semester,
                cgpa = cgpa,
                id = id,
    
            )
            new_student.save()
            return redirect('home')
    
def studentDelete(request, id):

    students = student.objects.get(id = id)
    students.delete()
    return redirect('home')

def signup(request):
    context = {

    }
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_pass')

        if password == confirm_pass:
            user = CustomUser(username=username)
            user.set_password(password)
            user.save()
            return redirect('signin')
        else:
            context ={

            'error' : "Passwords does not match"
            }
            return render(request, 'signup.html', context)

    return render(request, 'signup.html', context)

def signin(request):
    context = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        # user = CustomUser.objects.get(username=username)
        # if user.check_password(password):
        #     login(request, user)
        #     return redirect('home')
        else:
            context = {
                'error': "Passwords does not match"
            }

    return render(request, 'signin.html', context)
def user_logout(request):
    logout(request)
    return redirect('signin')
    
def update_password(request):
    context ={

    }
    if request.method == "POST":
        username = request.POST.get('username')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user = CustomUser.objects.get(username = username)
        if user.check_password(old_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                return redirect('signin')
            else:
                context = {'error': "New passwords do not match"}
        else:
            context = {'error': "Old password is incorrect"}

    return render(request, 'updatepassword.html', context)


