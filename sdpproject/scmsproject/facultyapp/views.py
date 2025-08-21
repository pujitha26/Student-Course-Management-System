from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Faculty,FacultyCourseMapping,Course


def checkfacultylogin(request):
    fid = request.POST["fid"]
    pwd = request.POST["pwd"]

    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=pwd))
    print(flag)

    if flag:
        print("login success")
        request.session["fid"] = fid  # creating session vo
        return render(request,"facultyhome.html", {"fid":fid})
    else:
        msg="Login Failed"
        return render(request,"facultylogin.html",{"message":msg})
        #return HttpResponse("Login failure")

def facultyhome(request):
    fid = request.session["fid"]
    return render(request,"facultyhome.html",{"fid":fid})

def facultycourses(request):
    fid = request.session["fid"]
    print(fid)
    courses=Course.objects.all()
    count=Course.objects.count()

    mappingcourses=FacultyCourseMapping.objects.all()
    fmcourses=[]
    for course in mappingcourses:
        #print(course.faculty)
        if(course.faculty.facultyid==int(fid)):
            fmcourses.append(course)

    print(fmcourses)
    dir(fmcourses)
    count=len(fmcourses)
    return render(request,"facultycourses.html",{"fid":fid,"fmcourses":fmcourses,"count":count})

def facultychangepwd(request):
    fid = request.session["fid"]
    return render(request,"facultychangepwd.html",{"fid":fid})

def facultyupdatepwd(request):
    fid = request.session["fid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(fid,opwd,npwd)
    flag = Faculty.objects.filter(Q(facultyid=fid) & Q(password=opwd))

    if flag:

        print("Old Pwd is Correct")
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        print("updated..")
        msg="Password Updated Successfully"
    else:
        print("Old Pwd is Invalid")
        msg="Old Password is Incorrect"
    return render(request,"facultychangepwd.html",{"fid":fid,"message":msg})