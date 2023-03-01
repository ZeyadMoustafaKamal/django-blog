from django.shortcuts import render,redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.models import User , Group

@login_required(login_url='/accounts/login')
@permission_required('posts.can_create_posts', login_url='/accounts/login')
def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.auther = request.user
            post.save()

            return redirect('index')
    else:
        form = PostForm()
    return render(request,'create_post.html',{'form':form})
def permission_denied(request, exception):
    return redirect('/accounts/login')


class Posts(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    def post(self,request,*args,**kwrags):
        post = Post.objects.filter(id=request.POST.get('delete-post')).first()
        user = User.objects.filter(id=request.POST.get('ban-user')).first()
        if 'delete-post' in request.POST:
            if post:
                if (request.user == post.auther) or request.user.has_perm('posts.can_delete_post'):
                    post.delete()
                
        elif 'ban-user' in request.POST:
            if request.user.has_perm('auth.can_ban_users'):
                group = Group.objects.get(name='default')
                group.user_set.remove(user)
        return redirect(reverse_lazy('posts'))
