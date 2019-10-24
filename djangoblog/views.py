from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404,HttpResponse
from .models import BlogPost
from .forms import BlogPostModelForm

#CRUD
#GET => Retrieves/List
#POST => Create, Update, Delete

def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    context = {'object_list':qs}
    return render(request, 'list.html', context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    context = {'form':form}
    return render(request, 'form.html', context)
    

def blog_post_detail_view(request, slug):
    # 1 object => detail view
    obj =get_object_or_404(BlogPost,slug=slug)
    query_list = BlogPost.objects.all()
    query = request.GET.get('q')
    if query:
        query=query_list.objects.filter(title__icontains=query)
        
    context = {'object':obj,'query':query}
    return render(request, 'detail.html', context)
    
@staff_member_required   
def blog_post_update_view(request, slug):
    obj =get_object_or_404(BlogPost,slug=slug)
    form = BlogPostModelForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        form =BlogPostModelForm
    context = {'object':obj,'form':form}
    return render(request, 'form.html', context)
    
@staff_member_required
def blog_post_delete_view(request, slug):
    obj =get_object_or_404(BlogPost,slug=slug)
    if request.method =="POST":
        obj.delete()
        return redirect("/blog")
    context = {'object':obj}
    return render(request, 'delete.html', context)