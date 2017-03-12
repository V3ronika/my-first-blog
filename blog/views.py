from django.shortcuts import render

# Create your views here.
def post_list(request): #input from user in 'request'
    return render(request, 'blog/post_list.html', {}) #hlavna stranka na zobrazenie
