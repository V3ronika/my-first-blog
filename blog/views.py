from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
def post_list(request):#input from user in 'request', zobrazi sa ked natiahneme hlavnu stranku
    posts = Post.objects.filter(published_date__lte=timezone.now()) #zoznam postov, ktore maju published date (maju sa publikovat) lte = less than or equal
    return render(request, 'blog/post_list.html', {'posts':posts}) #hlavna stranka na zobrazenie

def post_detail(request, pk):#input from user in 'request', zobrazi sa ked natiahneme hlavnu stranku
    post = Post.objects.get(pk=pk) #primarny kluc
    return render(request, 'blog/post_detail.html', {'post':post})
