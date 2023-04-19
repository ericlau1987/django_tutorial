from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
import json
import urllib

# Create your views here.
def index(request):

    features = Feature.objects.all

    res = urllib.request.urlopen('https://www.land.vic.gov.au/property-report/property-dashboard2/street_suggestions.json?extraQuery=amendment-id&profile=amendment-id&partial_query=29%20LONGSTAFF%20ROAD%20BAYSWATER%203153').read()
    data = json.loads(res.decode('utf-8'))
    # key = data[0]['key']
    key = 'GST7YMc0AM9UOsKtGTyVGST7YMc0AM9UOsExAi9XOc50YTc2KQWmObktGMytaikZQBkKM5NKMoFF'
    pfi_data = urllib.request.urlopen(f'https://www.land.vic.gov.au/property-report/property-dashboard2/get_street_key.json?query={key}').read()
    pfi = json.loads(pfi_data.decode('utf-8'))['pfi']
    # address_data = urllib.request.urlopen(f'https://www.land.vic.gov.au/property-report/property-dashboard2/get_street_address.json?query={pfi}').read()
    # address = json.loads(address_data.decode('utf-8'))['pfi']
    return render(request, 'index.html', {'features': features, 'result': pfi}) # link it to the index.html in the template

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount':amount_of_words})


