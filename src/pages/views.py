from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    home_context = {
        "key_1": "This is fun 😄"
    }
    return render(request, 'home.html', home_context)


def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is me!",
        "my_number": 6549873217
    }
    return render(request, "contact.html", my_context)
