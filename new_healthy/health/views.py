from django.shortcuts import render, HttpResponse
import json
from health import models
# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, "index.html")

    else:
        pass

def emg(request):
    if request.method == "GET":
        all_emg_data = list(models.emg.objects.all().values())
        return render(request, "emg.html", {"all_emg_data": all_emg_data})
    else:
        pass

def electrocardiogram(request):
    if request.method == "GET":
        all_heart_rate_data = list(models.heart_rate.objects.all().values())
        return render(request, "electrocardiogram.html", {"all_heart_rate_data": all_heart_rate_data})

    else:
        pass

def spo2(request):
    if request.method == "GET":
        all_airflow_data = list(models.spo2.objects.all().values())
        return render(request, "spo2.html", {"all_airflow_data": all_airflow_data})
    else:
        pass

# def ele(request):
#     if request.method == "GET":
#         return render(request, "ele.html")
#     else:
#         pass


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        Email = request.POST.get('email')
        Password = request.POST.get('password')

        print(request.POST)
        print(Email, Password)

        if Email == "admin" and Password == "admin":
            return HttpResponse(json.dumps({"result": True}))
        else:
            return HttpResponse(json.dumps({"result": False}))


def sign_out(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        pass



def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        print(request.POST)

        if password == re_password:
            if username and email:
                return HttpResponse(json.dumps({"result": True}))
            else:
                return HttpResponse(json.dumps({"result": False}))

        else:
            return HttpResponse(json.dumps({"result": False}))



def test(request):
    import random
    for i in range(1000):
        a = random.randint(9, 11)
        models.emg.objects.create(data=a)

        b = random.randint(60, 120)
        models.heart_rate.objects.create(data=b)

        c = random.randint(80, 100)
        models.spo2.objects.create(data=c)

    return HttpResponse('ok')

def clean(request):
    models.spo2.objects.all().delete()
    models.heart_rate.objects.all().delete()
    models.emg.objects.all().delete()

    return HttpResponse('ok')