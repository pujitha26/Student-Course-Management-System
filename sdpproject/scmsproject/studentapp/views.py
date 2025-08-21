from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student,Course

from facultyapp.models import CourseContent


# Create your views here.
def studenthome(request):
    sid = request.session["sid"]
    return render(request,"studenthome.html",{"sid":sid})

def checkstudentlogin(request):
    sid = request.POST["sid"]
    pwd = request.POST["pwd"]

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=pwd))
    print(flag)

    if flag:
        print("login success")
        request.session["sid"] = sid  # creating session vo
        return render(request,"studenthome.html", {"sid":sid})
    else:
        msg="Login Failed"
        return render(request,"studentlogin.html",{"message":msg})
        #return HttpResponse("Login failure")



def studentchangepwd(request):
    sid = request.session["sid"]
    return render(request,"studentchangepwd.html",{"sid":sid})

def studentupdatepwd(request):
    sid = request.session["sid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(sid,opwd,npwd)
    flag = Student.objects.filter(Q(studentid=sid) & Q(password=opwd))

    if flag:

        print("Old Pwd is Correct")
        Student.objects.filter(studentid=sid).update(password=npwd)
        print("updated..")
        msg="Password Updated Successfully"
    else:
        print("Old Pwd is Invalid")
        msg="Old Password is Incorrect"
    return render(request,"studentchangepwd.html",{"sid":sid,"message":msg})

def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})

def studentcoursecontent(request):
    sid = request.session["sid"]
    content = CourseContent.objects.all()
    return render(request,"studentcoursecontent.html",{"sid":sid,"coursecontent":content})


def displaystudentcourses(request):

    sid = request.session["sid"]

    ay = request.POST["ay"]
    sem = request.POST["sem"]

    courses = Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))

    return render(request,"displaystudentcourses.html",{"courses":courses,"sid":sid})