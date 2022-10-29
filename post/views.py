import json

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth
from numpy import product
from .models import *
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.

def show_main_page(request):
    return render(
        request,
        'post/index.html'
    )

def profile_page(request):
    User = get_user_model()
    
    return render(
        request,
        'post/profile.html'
    )


def search_result(request):
    posts, query = None, None
    print(request.GET)
    # 장고 검색 기능
    if 'q' in request.GET:  
        query = request.GET.get('q')
        posts = Post.objects.all().filter(title__icontains=query)
        print(query, posts)
    return render(request,
                'post/post_list.html',
                {'query' : query,
                'posts': posts})

def show_post_detail(request, pk):
    post = Post.objects.get(pk=pk)              # 해당 포스트만 가져옴
    photo = Photo.objects.filter(postnum_id=pk) # 해당 포스트의 사진만 가져옴
    return render(
        request,
        'post/post_detail.html',
        {
            'post':post,
            'photo':photo,
        }
    )
    
# Create your views here.
def register(request):   
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        nickname = request.POST['nickname']
        
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                username=id, password=password
            )
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'post/register.html')
    return render(request, 'post/register.html')
        
        

def login(request):    
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == "POST":
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        id = request.POST['id']
        password = make_password(request.POST['password'])
        user = User.objects.get(username=id)
        print(user)
        
        print(user.password, password)
        print(check_password(user.password, password))
        
        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        if user is not None and check_password(user.password, make_password(password)):
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'post/login.html', {'error':'not user'})
    else:
        return render(request, 'post/login.html')

# 로그 아웃
def logout(request):
    auth.logout(request)
    return redirect('/')


''' mysql version
@csrf_exempt   
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, user_name=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'main')
        else:
            return redirect('/'), {'error': 'username or password is incorrect'}
    else:
        return render(request, 'post/login.html')

@csrf_exempt
def register(request):
    print(request.method)
    if request == "POST":
        id = request.POST['user_name']
        passwd = request.POST['user_password']
        nickname = request.POST['user_nickname']
        
        if User.objects.filter(id=id).exists():
            return render(request, 'post/index.html')
        else:
            user = User.objects.create(id=id, passwd=make_password(passwd), nickname=nickname)
            user.save()
            return redirect('main')
    else: return render(request, 'post/register.html')

@csrf_exempt
def loginCheck(request):
    template_name = 'login.html'
    request.session['loginOk'] = False
    inputId == ''
    inputPassword == ''
    
    try:
        data = request.POST
        inputId = data['username']
        inputPassword = data['password']

    except (KeyError):
        context = {
            "uid": "empty",
            "upass": "empty",
        }
        return render(request, template_name, context)
    else:
        if User.objects.filter(username=inputId).exists():
            getUser = User.objects.get(username=inputId)
            if getUser.password == inputPassword:
                request.session['loginOk'] = True
                context = {
                    "result": "로그인 성공"
                }
            else:
                request.session['loginOk'] = False
                context = {
                    "result": "비밀번호가 틀렸습니다"
                }
        else:
            request.session['loginOk'] = False
            context = {
                "result": "존재하지 않는 id입니다"
            }
        return HttpResponse(json.dumps(context), content_type="application/json")
'''