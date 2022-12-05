import json
from unicodedata import category
from django.http import JsonResponse
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
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

# Create your views here.

def show_main_page(request):
    return render(
        request,
        'post/index.html'
    )

def profile_page(request):
    User = get_user_model()
    
    if request.user.is_authenticated:
        mypost=Post.objects.filter(author=request.user)
    else:
        return render(request, 'post/login.html')
    post_count = len(mypost)
    
    return render(
        request,
        'post/profile.html',
        {
            'post_count' : post_count,
            'mypost':mypost,
        }
    )



def search_result(request):
    posts, query = None, None
    # 장고 검색 기능
    if 'q' in request.GET:  
        query = request.GET.get('q')
        # posts = Post.objects.all().filter(Q(title__icontains=query))
        category1 = Category1.objects.filter(category=query)
        category2 = Category2.objects.filter(category=query)
        
        if not category1.exists(): category_num1 = 0
        else: category_num1 = category1.values_list()[0][0]
        
        if not category2.exists(): category_num2 = 0
        else: category_num2 = category2.values_list()[0][0]
        
        posts = Post.objects.all().filter(Q(title__icontains=query) | Q(category1=category_num1) | Q(category2=category_num2))
        
    return render(request,
                'post/post_list.html',
                {'query' : query,
                'posts': posts})

def show_post_detail(request, pk):
    post = Post.objects.get(pk=pk)              # 해당 포스트만 가져옴
    photo = Photo.objects.filter(postnum_id=pk) # 해당 포스트의 사진만 가져옴
    comment=Comment()
    # print(pk)
    if request.method=='POST':
        if request.user.is_authenticated:
            content=request.POST['content']
            comment.content=content
            comment.postnum=post
            comment.author=request.user
            comment.save()
        else:
            return render(request, 'post/login.html')
    
    # page
    page=request.GET.get('page')
    comment=Comment.objects.filter(postnum_id=pk).order_by('-id')  #해당 포스트의 댓글만 가져옴
    paginator=Paginator(comment,10)
    repost=paginator.get_page(page)


    return render(
        request,
        'post/post_detail.html',
        {
            'post':post,
            'photo':photo,
            'comment':comment,
            'repost':repost,
        }
    )

@csrf_exempt
def comment_delete(request,pk,comment_pk):
    post = Post.objects.get(pk=pk)              # 해당 포스트만 가져옴
    photo = Photo.objects.filter(postnum_id=pk) # 해당 포스트의 사진만 가져옴
    # comment=Comment.objects.filter(postnum_id=pk).order_by('-id')
    # page
    page=request.GET.get('page')
    comment=Comment.objects.filter(postnum_id=pk).order_by('-id')  #해당 포스트의 댓글만 가져옴
    paginator=Paginator(comment,10)
    repost=paginator.get_page(page)
    if request.method=='POST':
        # comment.id가 삭제되어야함
        del_comment=Comment.objects.get(pk=comment_pk)
        del_comment.delete()
    return render(
        request,
        'post/post_detail.html',
        {
            'post':post,
            'photo':photo,
            'comment':comment,
            'repost':repost,
        }
    )
    # return redirect('/post/'+int(post.pk))
@csrf_exempt
def post_delete(request,pk):
    post = Post.objects.get(pk=pk)              # 해당 포스트만 가져옴
    # photo = Photo.objects.filter(postnum_id=pk) # 해당 포스트의 사진만 가져옴
    if request.method=='POST':
        if request.user.is_authenticated:
            # print(post.pk)
            post.delete()
        else:
            return render(request, 'post/login.html')
    return redirect("/post")

@csrf_exempt
def post_update(request,pk):
    # 포스트의 pk를 불러오고 pk빼고 나머지를 저장
    post=Post.objects.get(pk=pk)
    if request.method=='POST':
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.category1_id=request.POST['city']
        post.category2_id=request.POST['category']
        # print(request.POST['title'])
        post.save()
        for idx, img in enumerate(request.FILES.getlist('files')):
            if idx == 0: 
                post.head_image=img
                post.save()
                photo=Photo.objects.filter(postnum_id=pk)
                photo.delete()
            else:
                photo=Photo()
                photo.postnum=post
                photo.image=img
                photo.save()
        return redirect('/')
    else:
        return render(request,'post/update.html',{'post':post})
    
    ...
@csrf_exempt
def upload(request):
    if request.method =='POST':
        title, content = request.POST.get('title',), request.POST.get('content', )
        main_category = request.POST.get('city')
        sub_category=request.POST.get('category')
    

        category_num1 = main_category
        category_num2 = sub_category
        
        post=Post()
        post.title = title
        post.content = content
        post.category1_id = category_num1
        post.category2_id = category_num2
        post.author = request.user
        
        for idx, img in enumerate(request.FILES.getlist('files')):
            if idx == 0: 
                post.head_image=img
                post.save()
            else:
                photo=Photo()
                photo.postnum=post
                photo.image=img
                photo.save()
            
        return redirect('/')
    
    else:
        return render(request, 'post/upload.html')


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
        password = request.POST['password']
        user = auth.authenticate(request, username=id, password=password)
        
        if user is not None: 
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