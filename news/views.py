from django.shortcuts import render
import requests

API_KEY ='5d701117be3e4d5980c66f3636e005ae'
# Create your views here.

def main(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        print(data)
        articles = data['articles']
    else:

        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        print(data)
        articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'main.html', context)
