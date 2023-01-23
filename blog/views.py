from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator


# Create your views here.
from blog.models import Post, Category, Copyuser


def home(request):
    #load post from database
    post=Post.objects.order_by('-add_date')
    # print (post)
    cats = Category.objects.all()
    # cats=cats.order_by('-add_date')
    posts = post.order_by('add_date')



    p=Paginator(post,3)
    pageno=request.GET.get('page')
    pfinal=p.get_page(pageno)

    data={
        'post':pfinal,
        'cats':cats,
        'posts':posts
    }
    return render(request,'home.html',data)

def post(request,url):
    post = Post.objects.get(url=url)
    cats=Category.objects.all()

    return render(request, 'posts.html',{'post': post, 'cats': cats})

def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    cats = Category.objects.all()
    return render(request, "category.html", {'cat': cat, 'posts': posts,'cats':cats,})

# def log(request):
#     if request.POST == 'GET':
#         pass
#
#     if request.POST == 'POST':
#         pass

def signin(request):
    if request.method == 'GET':
        return render(request, "signin1.html", {})

    if request.method == 'POST':
        pd = request.POST
        fn = pd.get('first_name')
        ln = pd.get('last_name')
        em = pd.get('cemail')
        pn = pd.get('cphone')
        ps = pd.get('passwd')
        ps1= pd.get('passwd1')
        # adr = pd.get('addr')
        # pin = pd.get('pin')

        value = {
            'first_name': fn,
            'last_name': ln,
            'cmail': em,
            'phone': pn
        }

        er_massege = None

        if len(fn) < 1:
            er_massege = "First Name is required"
        elif len(ln) < 1:
            er_massege = "Last name is rquired"
        elif len(em) < 1:
            er_massege = "email is required"
        elif len(pn) < 10:
            er_massege = "Phone number is required 10 digits"
        elif (ps!=ps1):
            er_massege = "password is not match"

        # elif len(adr) < 1:
        #     er_massege = "Address is required"
        # elif len(pin) < 1:
        #     er_massege = "PIN Code is required"

        user = User.objects.all()
        for x in user:
            if x.username == em:
                er_massege = 'Email address Already Registered..'

        if not er_massege:
            # note :-> here first_neame = em and em = fn
            myuser = User.objects.create_user(em, fn, ps)
            myuser.last_name = ln
            myuser.phone = pn
            myuser.save()
            c = Copyuser(first_name=fn, last_name=ln, email=em, phone=pn)
            c.save()
            er_massege = "Account created successfully please login"
            return render(request, 'signup.html', {'succ': er_massege})
        data1 = {
            'error': er_massege,
            'values': value
        }
        return render(request, 'signup.html', data1)


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login1.html')

    if request.method == 'POST':
        em = request.POST.get('cemail')
        ps = request.POST.get('passwd')
        # ps = str(ps)
        # if (em == 'rahul1@gmail.com' and ps == '999'):
        #     print('====Analysis Start======')
        #     # print(d)
        #     print('=====Analysis End=======')
        #     return render(request, 'analysis.html')

        er_massege = None
        user = False
        user = check_user(em)
        if user:
            eml = User.objects.get(username=em)
            if eml.username == em and (check_password(ps, eml.password)):
                user = authenticate(username=eml, password=ps)
                login(request, user)
                return redirect('home')
            else:
                er_massege = "invalid password"
                return render(request, 'login1.html', {'error': er_massege})
        else:
            er_massege = "invalid email"
            return render(request, 'login1.html', {'error': er_massege})

def check_user(em):
    try:
        User.objects.get(username = em)
        return True
    except:
        return False

def userlogout(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request,'about.html',{})
def courses(request):
    return render(request,'courses.html',{})