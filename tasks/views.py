from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


class NewTasksForm(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(
        request,
        "tasks/index.html",
        {
            "tasks": request.session["tasks"],
        },
    )


def addTask(request):
    if request.method == "POST":
        form = NewTasksForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {"form": form})

    return render(
        request,
        "tasks/add.html",
        {
            "form": NewTasksForm(),
        },
    )
