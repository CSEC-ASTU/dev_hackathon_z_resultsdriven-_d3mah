from django.shortcuts import redirect, render
from .models import *
# Create your views here.
from .scrape_medium import *
from .stats import stat_update

from .form import *


def home(req):

    achivement = list(Achivement.objects.all())
    product = list(Project.objects.all())
    blog = list(Blog.objects.all())
    stats = list(Stats.objects.all())
    # scrape_medium_user_blog()
    # stat_update()
    context = {
        "achivement": achivement,
        "product": product,
        "blog": blog,
        "stats": stats,
    }

    return render(req, "index.html", context)


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()  # Save the form data to the database

    return redirect('/')
