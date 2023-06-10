from django.shortcuts import render
from .models import *
# Create your views here.
from .scrape_medium import *


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
