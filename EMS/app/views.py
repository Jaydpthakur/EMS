from django.shortcuts import render, redirect
from .models import UserData, AdminDataBase, EnquiryDataBase
# Create your views here.
def home(req):
    return render(req,'index.html')

def usignup(req):
    return render(req,'usignup.html')

def udata(req):
    if req.method=='POST':
        nm=req.POST.get('name')
        em=req.POST.get('email')
        mb=req.POST.get('mobile')
        ps=req.POST.get('password')
        cps=req.POST.get('cpassword')
        
        data=UserData(name=nm, email=em, mobile=mb, password=ps, cpassword=cps)
        user=UserData.objects.filter(email=em)
        if user:
            msg= "User already exist"
            return render(req,'usignup.html',{'msg':msg})
        else:
            if ps == cps:
                data.save()
                msg = "User register Successfully"
                return render(req,'index.html',{'msg':msg})
            else:
                msg = "Password and Confirm Password Doesnot Match"
                return render(req,"usignup.html",{'msg':msg})
        
def asignup(req):
    return render(req,'asignup.html')

def adata(request):
    if request.method=='POST':
        fname=request.POST["name"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        contact=request.POST["mobile"]
        password=request.POST["password"]
        cpassword=request.POST["cpassword"]
        
        #First we check user is already exist or not
        user=AdminDataBase.objects.filter(Email=email)
        if user:
            msg= "Admin already exist"
            return render(request,'asignup.html',{'msg':msg})
        else:
            if password == cpassword:
                newuser = AdminDataBase.objects.create(Firstname=fname,Lastname=lname,Email=email
                                    ,Contact=contact,Password=password)
                msg = "Admin register Successfully"
                # data = {
                #     'msg':"User register Successfully"
                # }
                return render(request,'index.html',{'msg':msg})
                # return render(request,'home.html',data)
            else:
                msg = "Password and Confirm Password Doesnot Match"
                return render(request,"asignup.html",{'msg':msg})


        
def ulogin(req):
    return render(req,'ulogin.html')

def udatabase(request):
    if request.method=='POST':
        em=request.POST['email']
        ps=request.POST['password']
        # newuser=UserData.objects.filter(email=em,password=ps)
        try:
            newuser=UserData.objects.get(email=em)
            if newuser:       
                if newuser.password==ps:
                    request.session['Email']=newuser.email
                    request.session['Password']=newuser.password
                    return render(request,'userpage.html')
                else:
                    msg="Incorrect Password!"
                    return render(request,'ulogin.html',{'msg':msg})
        except:
            msg="User does not exist!"
            return render(request,'ulogin.html',{'msg':msg})
   

def alogin(req):
    return render(req,'alogin.html')

def adatabase(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        # newuser=AdminDataBase.objects.filter(Email=email,Password=password)
        
        try:
            newuser=AdminDataBase.objects.get(Email=email)

            if newuser:       
                if newuser.Password==password:
                    request.session['Firstname']=newuser.Firstname
                    request.session['Lastname']=newuser.Lastname
                    request.session['Email']=newuser.Email
                    request.session['Password']=newuser.Password
                    return render(request,'admpage.html')
                else:
                    msg="Incorrect Password!"
                    return render(request,'alogin.html',{'msg':msg})         
        except:
            msg='Admin does not exist!'
            return render(request,'alogin.html',{'msg':msg})
              
           
        

def enquiryView(request):
    return render(request,'enquiry.html')

def insertEnquiryDataBase(request):
    if request.method=='POST':
        sname=request.POST["sname"]
        email=request.POST["email"]
        contact=request.POST["contact"]
        enquiry=request.POST["enquiry"]
        user = EnquiryDataBase.objects.create(Studentname=sname,Email=email,Contact=contact,Enquiry=enquiry)
        msg= "Enquiry Successfully submitted!"
        return render(request,'enquiry.html',{'msg':msg})
    
#===============================(CRUD)==========================================

def showPage(request):
    all_data=EnquiryDataBase.objects.all()
    return render(request,'showpage.html',{'key1':all_data})

#Edit page view
def EditPage(request,pk):
    #fetching the data of perticular ID
    get_data=EnquiryDataBase.objects.get(id=pk)
    return render(request,'edit.html',{'key2':get_data})

#Update data View
def UpdateData(request,pk):
    udata=EnquiryDataBase.objects.get(id=pk)
    udata.Studentname=request.POST['studentname']
    udata.Enquiry=request.POST['enquiry']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']
    #Query for update
    udata.save()
    return redirect('showpage')

#Delete data View
def DeleteData(request,pk):
    ddata=EnquiryDataBase.objects.get(id=pk)
    #Query for delete
    ddata.delete()
    return redirect('showpage')
