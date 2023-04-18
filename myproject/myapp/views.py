from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # context = {
    #     'name': 'Lin',
    #     'age': 24,
    #     'nationality':' Chinese'
    # }
    return render(request, 'index.html') # link it to the index.html in the template

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount':amount_of_words})