from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from .models import Post
from django.contrib.auth.models import Group

# Create your views here.
#home
def Home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

#about
def About(request):
    return render(request,'blog/about.html')

#contact
def Contact(request):
    return render(request,'blog/contact.html')

#dashboard
def Dashboard(request):
 if request.user.is_authenticated:
  posts = Post.objects.all()
  user = request.user
  full_name = user.get_full_name()
  gps = user.groups.all()
  return render(request,'blog/dashboard.html',{'posts':posts, 'full_name':full_name,'groups':gps})
 else:
  return HttpResponseRedirect('/login/')

#logout
def User_Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#login
def User_Login(request):
 if not request.user.is_authenticated:
  if request.method == 'POST':
   form = LoginForm(request=request, data=request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    if user is not None:
     login(request, user)
     messages.success(request, 'Logged in Successfully !!')
     return HttpResponseRedirect('/dashboard/')        
  else:
   form = LoginForm()
  return render(request,'blog/login.html',{'form':form})
 else:
  return HttpResponseRedirect('/dashboard/')

#Signup
def User_Signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      messages.success(request,'Congratulations!! You have become Author')
      user = form.save()
      group = Group.objects.get(name='Author')
      user.group.add(group)
  else:
   form = SignUpForm()
  return render(request,'blog/signup.html',{'form':form})

#add new post
def add_post(request):
 if request.user.is_authenticated:
  if request.method == "POST":
   form = PostForm(request.POST)
   if form.is_valid():
    title =form.cleaned_data['title']
    desc = form.cleaned_data['Desc']
    pst=Post(title=title,Desc=desc)
    pst.save()
    form=PostForm()
  else:
   form=PostForm()
  return render(request,'blog/addpost.html',{'form':form})
 else:
  return HttpResponseRedirect('/login/')
    
#update/Edit post
def update_post(request,id):
 if request.user.is_authenticated:
   if request.method == 'POST':
     pi = Post.objects.get(pk=id)
     form = PostForm(request.POST, instance=pi)
     if form.is_valid():
       form.save()
   else:
     pi = Post.objects.get(pk=id)
     form = PostForm(instance=pi)
   return render(request,'blog/updatepost.html',{'form':form})
 else:
   return HttpResponseRedirect('/login/')

#delete post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
          pi = Post.objects.get(pk=id)
          pi.delete()
          return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
