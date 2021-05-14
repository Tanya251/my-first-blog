from django.shortcuts import render

# Сreate your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {})
    
