from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post,Comment
from django.views.generic import UpdateView,DeleteView
from .forms import PostModelForm, CommentModelForm, PostCreateModelForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def PostListCreate(request):
    query_set = Post.objects.all()
    context = {
        'query_set' : query_set,
    }
    return render(request,'pages/index.html',context)

def advertisement(request,advertisement_id):
    advertisement = get_object_or_404(Post,pk=advertisement_id)
    c_form = CommentModelForm(request.POST or None)
    if 'new_comment' in request.POST:
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = Post.objects.get(id=advertisement_id)
            instance.save()
            c_form = CommentModelForm()
    context = {
        'advertisement' :advertisement,
        'c_form' : c_form,
    }

    return render(request,'pages/advertisement.html',context)


def create_post(request):
    success_url = reverse_lazy('posts:PostListCreate')
    pc_form = PostCreateModelForm()
    post_added = False
    if 'Create_post' in request.POST:
        print(request.POST)
        pc_form = PostCreateModelForm(request.POST, request.FILES)
        if pc_form.is_valid():
            instance = pc_form.save(commit=False)
            instance.author = request.user
            instance.save()
            pc_form = PostCreateModelForm()
            post_added = True
            return redirect('posts:PostListCreate')

    context = {
        'pc_form': pc_form,
        'post_added': post_added,
    }
    return render(request,'posts/create_post.html',context)


class PostDeleteView(DeleteView):
    model : Post
    template_name = 'posts/confirm_delete.html'
    success_url = reverse_lazy('posts:PostListCreate')

    def get_object(self,*args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Post.objects.get(pk=pk)
        if not obj.author == self.request.user:
            messages.warning(self.request, 'You need to be the author of the post in order to delete it')
        return obj


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostModelForm
    template_name = 'posts/edit_post.html' 
    success_url = reverse_lazy('posts:PostListCreate')

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        obj = Post.objects.get(pk=pk)
        if obj.author == self.request.user : 
            return super().form_valid(form)
        else:
            form.add_error(None, "You need to be the author of the post in order to update it")
        return super().form_invalid(form)
    
    
    