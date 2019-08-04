from django.shortcuts import render


def post_list(request,*args , **kwargs):
    return render(request,'blog/post_list.html', {})
# Create your views here.



