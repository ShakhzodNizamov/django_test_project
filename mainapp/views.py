from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import PostForm, CommentForm
from .models import Post, Comment


class MainPage(View):
    model = Post
    template_name = "main_page.html"

    def get(self, request):
        posts = Post.objects.filter()
        return render(request, 'main_page.html', {'posts': posts})


class CreatePostPage(View):
    model = Post
    template_name = "add_new_post.html"

    def get(self, request):
        return render(request, 'add_new_post.html')


class PostDetailPage(View):
    model = Post
    template_name = 'post_detail.html'

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        comment_list = post.get_comments()
        print('PostDetailPage class')
        return render(request, 'post_detail.html', {'post': post, 'comment_list': comment_list})


class AddPost(View):
    def post(self, request, username):
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            obj: Post = form.instance
            obj.username = username
            obj.save()
        return redirect('/')


class AddComment(View):
    def post(self, request, post_id):
        form = CommentForm(request.POST)
        username = request.user.username
        if form.is_valid():
            obj: Comment = form.instance
            obj.username = username
            obj.post_id = post_id
            obj.save()
        post = Post.objects.get(id=post_id)
        comment_list = post.get_comments()
        print('PostDetailPage class')
        # return render(request, 'post_detail.html', {'post': post, 'comment_list': comment_list})
        return redirect(f'/detail/{post_id}', 'post_detail.html', {'post': post, 'comment_list': comment_list})
