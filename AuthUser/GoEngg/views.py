from django.shortcuts import render
# Create your views here.

def helloview(request):
	return render(request,"GoEngg/Index.html",{})