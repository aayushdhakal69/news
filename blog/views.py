from django.db.models import query
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Post
from django.contrib import messages
# Create your views here.
def blogHome(request):
    allPosts= Post.objects.all()
    # print(allPosts)
    context={'allPosts': allPosts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request, slug):
    post=  Post.objects.filter(slug=slug).first()
    print(post)
    context={'post': post}
    return render(request,'blog/blogPost.html', context)
    # return HttpResponse(f"This is blogpost:{slug} ")
    
def search(request):
    query = request.GET['query']
    if len(query)> 100:
        allPosts= Post.objects.none()
    else:
        # allPosts= Post.objects.all()
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
        messages.error(request, "Please fill the form correctly")
        params= {'allPosts': allPosts,'query': query}
        return render(request,'blog/search.html',params)
        # return HttpResponse('K xa sathi')
