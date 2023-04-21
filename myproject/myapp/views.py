from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
import json
import urllib

# Create your views here.
def index(request):

    features = Feature.objects.all
    no_street = 23
    street_name = 'Longstaff' 
    street_type = 'Road'
    suburb = 'Bayswater'
    postcode = 3153
    res = urllib.request.urlopen(f'https://www.land.vic.gov.au/property-report/property-dashboard2/street_suggestions.json?extraQuery=amendment-id&profile=amendment-id&partial_query={no_street}%20{street_name.upper()}%20{street_type.upper()}%20{suburb.upper()}%20{postcode}').read()
    data = json.loads(res.decode('utf-8'))
    key = data[0]['key']
    pfi_data = urllib.request.urlopen(f'https://www.land.vic.gov.au/property-report/property-dashboard2/get_street_key.json?query={key}').read()
    pfi = json.loads(pfi_data.decode('utf-8'))['pfi']
    # address_data = urllib.request.urlopen(f'https://www.land.vic.gov.au/property-report/property-dashboard2/get_street_address.json?query={pfi}').read()
    # address = json.loads(address_data.decode('utf-8'))['pfi']
    url = f'https://production-detailed-report-pdf.s3-ap-southeast-2.amazonaws.com/{no_street}-{street_name}-{street_type}-{suburb}-(ID{pfi})-Detailed-Property-Report.pdf'
    return render(request, 'index.html', {'features': features, 'key': key, 'result': pfi, 'url': url}) # link it to the index.html in the template

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount':amount_of_words})


