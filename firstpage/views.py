from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscriberForm

# Create your views here.
def home(request):
    name = "Jiro"
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        new_form = form.save()
    return render(request, 'firstpage/firstpage.html' , locals())
