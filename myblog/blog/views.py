from django.shortcuts import render ,get_object_or_404
from .models import Post
from django.http import HttpResponse
from django.views.generic import ListView,DetailView ,CreateView , UpdateView , DeleteView

from django.contrib.auth.mixins import  LoginRequiredMixin, UserPassesTestMixin



def blog_view(request):
    posts = Post.objects.all()
    
    return render(request, "blog.html",{'posts': posts})
def about_view(request):
    return render(request,'about.html')
class PostDetailView(DetailView):

    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','text']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
  
class PostDeleteview(DeleteView):
    model = Post
    success_url='/'
class PostUpdateView(UpdateView):
    model=Post
    fields=['title','text']  
# Create your views here.
