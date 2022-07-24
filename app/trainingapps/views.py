from trainingapps.models import ContactUs, Rate, Source
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from trainingapps.forms import SourceForm
from faker import Faker
import requests

# Create your views here.
fake = Faker()

"""
DATA GET OR GENERATION FUNCTIONS
"""


def gen_fake_info(request):  # Gen fake data
    for _ in range(10):

        data = ContactUs(
            email_from=fake.email(),
            email_to=fake.email(),
            subject=fake.text(20),
            message=fake.text(30))
        data.save()

    return HttpResponse("Data gen!", status=201)


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

    return HttpResponse("Data's succesfull save!", status=201)


def gen_source_info(request):
    for _ in range(10):

        fakedata = Source(
            source_url=fake.url(),
            name=fake.company())
        fakedata.save()
    return HttpResponse("Data gen!", status=201)


"""
WORKING WITH PAGES
"""


def index(request):
    return render(request, "index.html", status=200)


def show_ratelist(request):
    context = {
        "message": "Сurrent currency table.",
        "datalist": Rate.objects.all()
    }
    return render(request, "rate_list.html", context=context, status=200)


def show_contactuslist(request):
    context = {
        "message": "Link table.",
        "datalist": ContactUs.objects.all()
    }
    return render(request, "contactus_list.html", context=context, status=200)


def show_sourcelist(request):
    context = {
        "message": "Table of source.",
        "datalist": Source.objects.all()
    }
    return render(request, "source_list.html", context=context, status=200)


"""
WORKING WITH FORMS
"""


def create_source(request):
    if request.method == "POST":
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/data/source")
    elif request.method == "GET":
        form = SourceForm()

    context = {
        "form": form,
        "message": "Let's create new source data."
    }
    return render(request, "create_source.html", context=context, status=201)


def update_source(request, idin: int):
    source_id = get_object_or_404(Source, id=idin)

    if request.method == "POST":
        form = SourceForm(request.POST, instance=source_id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/data/source")
    elif request.method == "GET":
        form = SourceForm(instance=source_id)

    context = {
        "form": form,
        "message": "Let's update source data."
    }
    return render(request, "update_source.html", context=context, status=200)


def detail_source(request, idin):
    source_id = get_object_or_404(Source, id=idin)
    context = {
        "data": source_id,
        "message": "Details of id"
    }
    return render(request, "detail_source.html", context=context, status=200)


def delete_source(request, idin):
    source_id = get_object_or_404(Source, id=idin)

    if request.method == "POST":
        source_id.delete()
        return HttpResponseRedirect("/data/source")

    context = {
        "instance": source_id,
        "message": "Please press button to delete this data"
    }
    return render(request, "delete_source.html", context=context, status=200)
