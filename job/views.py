from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import companyAccount ,EmployeeAccount , CreatePost,EmpJobPost
from .form import companyAccountForm  ,EmployeeAccountForm



#check
def start(request):
    return render(request,"chooseLogin.html")

#Login 
def EmpLogin(request):
    user=[]
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        if user := EmployeeAccount.objects.filter(dt_emp_mobile = userid , dt_emp_password = password) :
          request.session['user_id'] = userid
          return redirect("/EmpHome")
        else:
         message = "Wrong Username or Password" 
         context = {'message': message}
         return render(request, "EmpLogin.html",context)
        
    return render(request, "EmpLogin.html")


def ComLogin(request):
    user=[]
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        if user := companyAccount.objects.filter(dt_com_mobile = userid , dt_com_password = password) :
          request.session['Com_user_id'] = userid
          return redirect("/ComHome")
        else:
         message = "Wrong Username or Password" 
         context = {'message': message}
         return render(request, "ComLogin.html",context)
               
    return render(request,"ComLogin.html",)

# Account Create 
def EmpAccount(request):
    if request.method == 'POST':
        EmpAccForm = EmployeeAccountForm(request.POST, request.FILES)
  
        if EmpAccForm.is_valid():
            EmpAccForm.save()
            return redirect ("/EmpLogin")
    else:
        EmpAccForm = EmployeeAccountForm()
   
    return render(request,"EmpAccount.html" , {'EmpAccForm' : EmpAccForm})

def ComAccount(request):
    if request.method == 'POST':
        ComAccForm = companyAccountForm(request.POST, request.FILES)
  
        if ComAccForm.is_valid():
            ComAccForm.save()
            return redirect("/ComLogin")
    else:
        ComAccForm = companyAccountForm()
    return render(request,"ComAccount.html", {'ComAccForm' : ComAccForm})


#Emp web
# Emp home
def EmpHome(request):
    user_id = request.session.get('user_id')
    DisplayPost = CreatePost.objects.all().order_by('-id')
    datapost={
        'DisplayPost': DisplayPost,
        'user_id': user_id
    }
    return render(request,"Emp/Home.html",datapost)

#Serach job
def SearchJob(request):
    post ={}
    if request.method =="POST":
        JobTitlePost = request.POST.get('JobTitle')
        DisplayPost = CreatePost.objects.filter(c_job_title = JobTitlePost)
        post = {
            'DisplayPost':DisplayPost
        }

    return render(request,"Emp/FindJob.html",post)

#check application
def ApplicationStatus(request):
    user_id = request.session.get('user_id')
    fst = 1
    rst = 2
    sst = 3
    
    fstpost = EmpJobPost.objects.filter(jp_emp_id = user_id , jp_emp_status = fst)
    rstpost = EmpJobPost.objects.filter(jp_emp_id = user_id , jp_emp_status = rst)
    sstpost = EmpJobPost.objects.filter(jp_emp_id = user_id , jp_emp_status = sst)  

    status = {
        'fstpost':fstpost,
        'rstpost':rstpost,
        'sstpost':sstpost
    }

    return render(request,"Emp/AStatus.html",status)


#Com Home
def ComHome(request):
    user_id = request.session.get('Com_user_id')
    empid =[]
    getid = EmpJobPost.objects.filter(jp_Com_id = user_id ,jp_emp_status = 3)
    for emp in getid:
        getempid = emp.jp_emp_id
        empid = EmployeeAccount.objects.filter(dt_emp_mobile = getempid)
    hireid={
        'empid':empid,
        'user_id': user_id
    }


    return render(request,"Com/Home.html",hireid)

def CreateJobPost(request):
    user_id = request.session.get('Com_user_id')
    Company_id = companyAccount.objects.filter(dt_com_mobile = user_id) 
    for i in Company_id:
      c_company_id =  i.dt_com_mobile
      c_com_name =   i.dt_com_name
      c_job_com_logo = i.dt_com_logo.url
    
    latest_post = CreatePost.objects.latest('id') 
    c_Post_id_get = latest_post.id 
    c_Post_id = int(c_Post_id_get) + 1
    
    if request.method=='POST':
        c_job_title = request.POST.get('c_job_title')
        c_joblpg = request.POST.get('c_joblpg')
        c_job_state = request.POST.get('c_job_state')
        c_job_pincode = request.POST.get('c_job_pincode')
        c_job_deteils = request.POST.get('c_job_deteils')
        c_job_recruitment = request.POST.get('c_job_recruitment')

        post = CreatePost(c_Post_id  = c_Post_id ,c_company_id = c_company_id, c_com_name = c_com_name, c_job_title = c_job_title, c_job_com_logo = c_job_com_logo , c_joblpg = c_joblpg , c_job_state = c_job_state, c_job_pincode = c_job_pincode, c_job_deteils = c_job_deteils, c_job_recruitment = c_job_recruitment )
        post.save()
        
    DisplayPost = CreatePost.objects.filter(c_company_id = user_id)
    datainfo = {
        'Company_id':Company_id,
        'DisplayPost': DisplayPost,
       

      }
    return render(request,"Com/CreatePost.html" , datainfo)


def Emphiring(request):
    post={}
    fst = 1
    user_id = request.session.get('Com_user_id')
    userajp = EmpJobPost.objects.filter(jp_Com_id=user_id ,jp_emp_status =fst)
    
    for emp in userajp:
        post_id = emp.jp_Post_id
        usereap = EmpJobPost.objects.filter(jp_Com_id=user_id, jp_Post_id=post_id  )
        post={
              'userajp':userajp,
              'usereap':usereap
         }

    return render(request,"Com/EmpHiring.html",post)

def EmpSelect(request,id):
    empapid = EmpJobPost.objects.filter(id=id)
    for getemp in empapid:
        empgetid = getemp.jp_emp_id 
    empd =  EmployeeAccount.objects.filter(dt_emp_mobile=empgetid)
    data = {
        'empapid':empapid,
        'empd':empd,
    }
    return render(request,"Com/EmpSelect.html",data)




#database process
def deletepost(request,id ):
    djobpost = CreatePost.objects.get(id=id)
    djobpost.delete()
    return redirect('/CreateJobPost')

def EmpApplyJob(request,id):
    applyPost = CreatePost.objects.filter(id=id)
    user_id = request.session.get('user_id')
    for job in applyPost:
        jp_Post_id = job.id
        jp_Com_id  = job.c_company_id
        jp_com_name  = job.c_com_name
        jp_job_title = job.c_job_title 
        jp_job_com_logo = job.c_job_com_logo
        jp_joblpg = job.c_joblpg 
        jp_job_state = job.c_job_state
        jp_job_pincode = job.c_job_pincode
        jp_job_deteils = job.c_job_deteils
        jp_job_recruitment = job.c_job_recruitment

    userap = EmployeeAccount.objects.filter(dt_emp_mobile = user_id)
    for user_info in userap:
        jp_emp_id = user_info.dt_emp_mobile
        jp_emp_Dp = user_info.dt_emp_Dp.url
        jp_emp_name = user_info.dt_emp_name
        jp_emp_info = user_info.dt_emp_detelis
    
    jp_emp_status = 1

    Post = EmpJobPost(jp_Post_id = jp_Post_id, jp_Com_id = jp_Com_id, jp_com_name = jp_com_name , jp_job_title = jp_job_title, jp_job_com_logo = jp_job_com_logo, jp_joblpg = jp_joblpg, jp_job_state = jp_job_state, jp_job_pincode = jp_job_pincode, jp_job_deteils = jp_job_deteils,jp_job_recruitment = jp_job_recruitment, jp_emp_Dp =jp_emp_Dp ,jp_emp_id = jp_emp_id, jp_emp_name = jp_emp_name, jp_emp_info = jp_emp_info, jp_emp_status = jp_emp_status )
    Post.save()

    return redirect('/EmpHome')


def EmpHire(request,id):
    hire = 3
    emphid = EmpJobPost.objects.get(id=id)
    emphid.jp_emp_status = hire
    emphid.save()
    return redirect('/Emphiring')


def EmpReject(request,id):
    reject = 2
    emprid = EmpJobPost.objects.get(id=id)
    emprid.jp_emp_status = reject
    emprid.save()
    return redirect('/Emphiring')
