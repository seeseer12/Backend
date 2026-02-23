from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render
# Create your views here.
def home(request):
    peoples = [
        {
            'name': 'Shishir',
            'age': 25,
            'city': 'Kathmandu'
        },


        {
            'name': 'Sita',
            'age': 30,
            'city': 'Lalitpur'
        },


        {
            'name': 'Ram',
            'age': 28,
            'city': 'Bhaktapur'
        }
    ]
    return render (request, 'home/index.html', context = {'peoples': peoples})


def about(request):
    return render(request, 'home/about.html', context={'page': 'about'})


def contact(request):
    return render(request, 'home/contact.html', context={'page': 'contact'})


def shishir(request):
    peoples = [
        {
            'name': 'Shishir',
            'age': 25,
            'city': 'Kathmandu'
        },


        {
            'name': 'Sita',
            'age': 30,
            'city': 'Lalitpur'
        },


        {
            'name': 'Ram',
            'age': 28,
            'city': 'Bhaktapur'
        },
    ]
    return render(request, 'home/index.html', context = {'peoples': peoples})



