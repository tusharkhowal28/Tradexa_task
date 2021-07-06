from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import Post
from .forms import SignupForm,PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import get_object_or_404




# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
   
@login_required
def home(request):
    post = Post.objects.all()
    return render(request,'display.html',{'post' : post,'media_url':settings.MEDIA_URL})


@login_required
def write(request):
    form = PostForm(request.POST,request.FILES,)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/post/")
        else:
            if request.user is not None:
                redirect('/post/')      
    args = {'form' : form}
    return render(request,'create_post.html',args) 



def view_post(request):
    login_user = request.user
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'view_post.html', {'posts': user_posts,'media_url':settings.MEDIA_URL})          


@login_required
def post_edit(request,id):  
    form = PostForm(instance = Post.objects.get(pk = id))
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance = Post.objects.get(pk = id))    
        if form.is_valid():                 
            edit = form.save()
            return redirect('/view/', id)
    else:
        PostForm(instance=Post.objects.get(pk = id))

    return render(request, 'edit_post.html', {'form': form})      

@login_required
def post_delete(request, id):
        dele = Post.objects.get(id=id)
        dele.delete()
        return redirect('/view/')

