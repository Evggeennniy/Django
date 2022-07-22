from trainingapps.models import ContactUs, Rate
from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker
import requests

# Create your views here.
fake = Faker()


def index(request):
    return render(request, "index.html")


def gen_fake_info(request):  # Gen fake data
    for _ in range(10):

        acc = ContactUs(
            email_from=fake.email(),
            email_to=fake.email(),
            subject=fake.text(20),
            message=fake.text(30))
        acc.save()

    return HttpResponse("Data gen!")


def get_currency_info(request):  # Gen currency information PRIVATBANK

    url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"

    req = requests.get(url)
    data_list = req.json()

    for data in data_list:

        rate = Rate(
            ccy=data.get("ccy", "Empty or Failed"),
            base_ccy=data.get("base_ccy", "Empty or Failed"),
            buy=data.get("buy", "Empty or Failed"),
            sell=data.get("sale", "Empty or Failed"))
        rate.save()

    return HttpResponse("Data's succesfull save!")


def dbshow(request):  # Show info from db

    db = str(request.GET.get("db"))

    if db == "rate":
        context = {
            "message": "Сurrent currency table",
            "datalist": Rate.objects.all(),

            "db": db
        }
        return render(request, "datalist.html", context=context)
    elif db == "contactus":
        context = {
            "message": "Link table",
            "datalist": ContactUs.objects.all(),

            "db": db
        }
        return render(request, "datalist.html", context=context)
    else:
        return HttpResponse("Please, chose database data/?db=...namedb")
