from random import randint
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    response = render(request, 'index.html')
    return HttpResponse(response)

def portfolio_page(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_urls.append('https://picsum.photos/400/600/?image={}'.format(random_number))
    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_page(request):
    context = {
        'skills': ['dancing', 'climbing', 'asking random questions'],
        'interests': ['health and wellness', 'people and relationships', 'family dynamics']
    }
    response = render(request, 'about.html', context)
    return HttpResponse(response)

def favourites_page(request):
    context = {
        'fave_links': 'https://lmgtfy.com'
    }
    response = render(request, 'favourites.html', context)
    return HttpResponse(response)
