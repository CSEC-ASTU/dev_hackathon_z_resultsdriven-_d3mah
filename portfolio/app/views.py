from django.shortcuts import redirect, render
from .models import *
# Create your views here.
from .scrape_medium import *

from .form import *


def home(req):

    achivement = list(Achivement.objects.all())
    product = list(Project.objects.all())
    blog = list(Blog.objects.all())
    # scrape_medium_user_blog()
    context = {
        "achivement": achivement,
        "product": product,
        "blog": blog,
    }

    return render(req, "index.html", context)


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()  # Save the form data to the database

    return redirect('/')
