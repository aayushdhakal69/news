#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db.models import query
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Post
from django.contrib import messages


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)


def search(request):
    query = request.GET['query']
    if len(query) > 100:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
        messages.error(request, 'Please fill the form correctly')
        params = {'allPosts': allPosts, 'query': query}
        return render(request, 'blog/search.html', params)
