from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from models import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from forms import PostForm

def home(request):
    posts = Post.objects.all().order_by('-datetime')
    return render_to_response("home_blog.html", {'posts':posts}, context_instance=RequestContext(request))

def single_post(request, blog):
    post = get_object_or_404(Post, pk=blog)
    posts = Post.objects.all().order_by('-datetime')
    return render_to_response("single_post.html", {'post':post, 'posts':posts}, context_instance=RequestContext(request))
    
def tag_search(request, tag):
    posts = Post.objects.filter(tags=tag)
    return render_to_response("home_blog.html", {'posts':posts}, context_instance=RequestContext(request))

@login_required
def enter_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            #still needs the ability to create tags from this view
            return redirect("/blog/")
    else:
        form = PostForm()
    return render_to_response("enter_post.html", {'form':form}, context_instance=RequestContext(request))
