from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Admin,Course,Student,Faculty,FacultyCourseMapping


# Create your views here.
def adminhome(request):
    auname = request.session["auname"]
    return render(request,"adminhome.html",{"adminuname":auname})


def logout(request):
    return render(request,"login.html")

def checkadminlogin(request):
    adminuname = request.POST["uname"]
    adminpwd = request.POST["pwd"]

    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)

    if flag:
        print("login sucess")
        request.session["auname"] = adminuname  # creating session vo
        return render(request,"adminhome.html", {"adminuname":adminuname})
    else:
        msg="Login Failed"
        return render(request,"login.html",{"message":msg})
        #return HttpResponse("Login failure")

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

def viewstudents(request):
    students = Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request,"viewstudents.html",{"studentdata":students,"count":count,"adminuname":auname})

def viewcourses(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request,"viewcourses.html",{"coursedata":courses,"count":count,"adminuname":auname})

def viewfaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})

def adminstudent(request):
    auname=request.session["auname"]
    return render(request,"adminstudent.html",{"adminuname":auname})

def adminfaculty(request):
    auname = request.session["auname"]
    return render(request,"adminfaculty.html",{"adminuname":auname})

def admincourse(request):
    auname = request.session["auname"]
    return render(request,"admincourse.html",{"adminuname":auname})

def addcourse(request):
    auname = request.session["auname"]
    return render(request,"addcourse.html",{"adminuname":auname})

def updatecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"updatecourse.html",{"adminuname":auname,"courses":courses,"count":count})

def courseupdation(request,cid):
    auname = request.session["auname"]
    return render(request,"courseupdation.html",{"cid":cid,"adminuname":auname})

def courseupdated(request):
    auname = request.session["auname"]
    cid=request.POST["cid"]
    courseid=int(cid)
    ctitle = request.POST["ctitle"]
    ltps = request.POST["ltps"]
    credits = request.POST["credits"]

    Course.objects.filter(id=courseid).update(coursetitle=ctitle,ltps=ltps,credits=credits)
    msg = "Course Updated Successfully"

    return render(request,"courseupdation.html",{"msg":msg,"adminuname":auname,"cid":cid})


def insertcourse(request):
    auname = request.session["auname"]
    if request.method=="POST":
        dept=request.POST["dept"]
        program=request.POST["program"]
        ay=request.POST["ay"]
        sem=request.POST["sem"]
        year=request.POST["year"]
        ccode=request.POST["ccode"]
        ctitle=request.POST["ctitle"]
        ltps = request.POST["ltps"]
        credits = request.POST["credits"]

        course = Course(department=dept,program=program,academicyear=ay,semester=sem,year=year,coursecode=ccode,coursetitle=ctitle,ltps=ltps,credits=credits)

        Course.save(course)

        message = "Course Added Succesfully"

        return render(request,"addcourse.html",{"msg":message,"adminuname":auname})


def deletecourse(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request,"deletecourse.html",{"coursedata":courses,"count":count,"adminuname":auname})

def coursedeletion(request,cid):

    Course.objects.filter(id=cid).delete()

    #return HttpResponse("Course Deleted Succesfully")

    return  redirect("deletecourse")

def addfaculty(request):
    auname = request.session["auname"]
    return render(request,"addfaculty.html",{"adminuname":auname})

def insertfaculty(request):
    auname = request.session["auname"]
    if request.method=="POST":
        facid=request.POST["facid"]
        fullname=request.POST["fullname"]
        gender=request.POST["gender"]
        dept=request.POST["dept"]
        qua=request.POST["qua"]
        degn=request.POST["degn"]
        pwd=request.POST["pwd"]
        email = request.POST["email"]
        contact = request.POST["contact"]

        faculty = Faculty(facultyid=facid,fullname=fullname,gender=gender,department=dept,qualification=qua,designation=degn,password=pwd,email=email,contact=contact)

        Faculty.save(faculty)

        message = "Faculty Added Succesfully"

        return render(request,"addfaculty.html",{"msg":message,"adminuname":auname})

def deletefaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request,"deletefaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})

def facultydeletion(request,fid):

    Faculty.objects.filter(id=fid).delete()

    #return HttpResponse("Faculty Deleted Succesfully")

    return  redirect("deletefaculty")

def addstudent(request):
    auname = request.session["auname"]
    return render(request, "addstudent.html", {"adminuname": auname})

def insertstudent(request):
    auname = request.session["auname"]
    if request.method=="POST":
        stuid=request.POST["stuid"]
        fullname=request.POST["fullname"]
        gender=request.POST["gender"]
        dept=request.POST["dept"]
        program=request.POST["program"]
        sem=request.POST["sem"]
        year = request.POST["year"]
        pwd=request.POST["pwd"]
        email = request.POST["email"]
        contact = request.POST["contact"]

        student = Student(studentid=stuid,fullname=fullname,gender=gender,department=dept,program=program,semester=sem,year=year,password=pwd,email=email,contact=contact)

        Student.save(student)

        message = "Student Added Succesfully"

        return render(request,"addstudent.html",{"msg":message,"adminuname":auname})





def deletestudent(request):
    student = Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request,"deletestudent.html",{"studentdata":student,"count":count,"adminuname":auname})

def studentdeletion(request,sid):

    Student.objects.filter(id=sid).delete()

    #return HttpResponse("Student Deleted Succesfully")

    return  redirect("deletestudent")





def facultycoursemapping(request):
    fmcourses=FacultyCourseMapping.objects.all()
    auname = request.session["auname"]
    return render(request,"facultycoursemapping.html",{"adminuname":auname,"fmcourses":fmcourses})


def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request,"adminchangepwd.html",{"adminuname":auname})

def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(auname,opwd,npwd)
    flag = Admin.objects.filter(Q(username=auname) & Q(password=opwd))

    if flag:

        print("Old Pwd is Correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("updated..")
        msg="Password Updated Successfully"
    else:
        print("Old Pwd is Invalid")
        msg="Old Password is Incorrect"
    return render(request,"adminchangepwd.html",{"adminuname":auname,"message":msg})

