from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.
def home(request):
    return render(request, "myapp/home.html", {"title": "Home"})

def about(request):
    return render(request, "myapp/about.html", {"title": "About"})

def thanks(request):
    return render(request, "myapp/thanks.html", {"title": "Thanks"})
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thanks")
    else:
        form = ContactForm()
    return render(request, "myapp/contact.html", {'form': form})