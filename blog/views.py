from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-id') # 블로그의 객체들을 가져와야함
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False) #임시저장(pubdate)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')
    # new_blog = Blog()
    # new_blog.title = request.POST['title']
    # new_blog.writer = request.POST['writer']
    # new_blog.body = request.POST['body']
    # new_blog.pub_date = timezone.now()
    # new_blog.image = request.FILES['image']
    # new_blog.save()
    # return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save() # 필수!
    return redirect('detail', update_blog.id)
  
def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')