from django.shortcuts import render,get_object_or_404
from .models import post
# Create your views here.
def home(request):

    posts =  post.objects.order_by('pub_data')

    return render(request,'posts/home.html',{'Post':posts})
def post_details(request, post_id):
    post_d = get_object_or_404 (post, pk=post_id)
    return render(request,'posts/post_detail.html',{'post':post_d})
