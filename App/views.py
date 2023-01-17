from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import register

def registration(request):
    if request.method=="POST":
        post=register()
        post.name=request.POST['name']
        post.email=request.POST['email']
        post.phone=request.POST['phone']
        post.address=request.POST['address']
        post.save()
        return render(request, 'FormSubmit/Form.html')
    else:
        return render(request, 'FormSubmit/Form.html')