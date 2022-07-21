from trainingapps.models import ContactUs, Rate
from django.http import HttpResponse
# from django.shortcuts import render
from faker import Faker
import requests

# Create your views here.
fake = Faker()


def main(request):  # Show main page

    return HttpResponse("This is main page!")


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

    if db == "ContactUs":
        data_list = list()
        for data in ContactUs.objects.all():

            text = f"""
            id : {data.id}<br>
            Email from : {data.email_from}<br>
            Email to : {data.email_to}<br>
            Object : {data.subject}<br>
            Message : {data.message}<br><br>"""

            data_list.append(text)

        return HttpResponse(data_list)

    elif db == "Rate":
        data_list = list()
        for data in Rate.objects.all():

            text = f"""
            id : {data.id}<br>
            Currency : {data.ccy}<br>
            Base currency : {data.base_ccy}<br>
            Buy : {float(data.buy)}<br>
            Sell : {float(data.sell)}<br><br>"""

            data_list.append(text)

        return HttpResponse(data_list)

    else:
        return HttpResponse("Please, chose table /data/txt/?dbshow=...nameDB")

# def show_info_html(request):

#     return render()
#     pass
