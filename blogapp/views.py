from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def all_posts(request):
    all_posts = Post.objects.filter(active=True)

    return render(request,'all_posts.html',{
        'all_posts':all_posts,
    })

def post(request,id):
    post = get_object_or_404(Post,id=id)


    return render(request,'post_detail.html',{
        'post':post,
    })

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

            return redirect('/blog/')

    else:
        form = PostForm()
    return render(request,'create_post.html',{
        'form':form,
    })

def edit_post(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/blog/')

    else:
        form = PostForm(instance=post)
    return render(request,'edit_post.html',{
        'form':form,
    })
