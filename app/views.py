from django.shortcuts import render

# Create your views here.
def madhu(request):
    return render (request,'madhu.html')

def form(request):
    return render(request,'form.html')


def form1(request):
    return render(request,'form1.html')

def sun(request):
    return render(request,'sun.html')

def marquee(request):
    return render (request,'marquee.html')

def jspider(request):
    return render(request,'jspider.html')