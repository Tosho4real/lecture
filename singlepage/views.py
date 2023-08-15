from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "singlepage/index.html")


texts = [
    "Lorem Ipsum has been the industrys standard dummy text ever since the 1500s",
    "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock",
    "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",
]

def practice(request):
    return render(request, "singlepage/practice.html")


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        return Http404("No such section")