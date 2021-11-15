from django.shortcuts import render,get_object_or_404

def index(request):
    return render(request,'ui/index.html')
def  ip_check(request):
    return render(request,'ui/ip_check.html')
def wifi(request):
    return render(request,'ui/wifi.html')
def ps(request):
    return render(request,'ui/ps.html')
def mitm(request):
    return render(request,'ui/mitm.html')
def mirai(request):
    return render(request,'ui/mirai.html')
def dos(request):
    return render(request,'ui/dos.html')
def ripple(request):
    return render(request,'ui/ripple.html')
def net(request):
    return render(request,'ui/net.html')