from django.shortcuts import render

# Create your views here.
def main_view(request, *args, **kwargs): #*args, **kwargs
	return render(request, "main.html",{})
