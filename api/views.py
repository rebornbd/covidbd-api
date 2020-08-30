import os
import math
import json
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

from django.shortcuts import render
from django.views.generic import View
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse

def getURL():
    url = os.environ.get("SET_LINK")
    return url

def getDistricts():
    url = getURL()
    response = requests.get(url)
    html = response.content

    soup = bs(html, 'html.parser')
    table = soup.find('div', attrs={'class': 'ritz grid-container'})
    tbody = table.find('tbody')
    districts = tbody.find_all('tr')
    return districts

def getCountNumber(number):
    try:
        return int(number)
    except ValueError:
        return int(0)
        
def getLastUpdatedDate():
    districts = getDistricts()

    indx = 0
    date = ''
    for dist in districts:
        indx = indx + 1

        if (indx == 3):
            distrow = dist.find_all('td')
            distData = [distcol.text.strip() for distcol in distrow]
            date = distData[4]

    return date

def home(request):
    data = { "end_point" : 'http://localhost' }
    return render(request, 'home.html', context=data)

def getDistrictData(request):
    districts = getDistricts()

    data = []
    indx = 0
    districtIdMap = [3, 17, 28, 32, 40, 50, 54, 60]
    districtNameIdMap = [54, 60]
    districtMapValue = ['Barguna', 'Joypurhat']
    for dist in districts:
        indx = indx + 1

        if (indx <= 2):
            continue
        if (indx == 68):
            break

        distrow = dist.find_all('td')
        distData = [distcol.text.strip() for distcol in distrow]

        if (indx in districtIdMap):
            distNameMap = distData[0]
            if (indx in districtNameIdMap):
                if (indx == 54):
                    distNameMap = districtMapValue[0]
                else:
                    distNameMap = districtMapValue[1]
            
            distObj = {
                "id" : indx,
                "name" : distNameMap,
                "count" : getCountNumber(distData[2])
            }
            data.append(distObj)
        else:
            distObj = {
                "id" : indx,
                "name" : distData[0],
                "count" : getCountNumber(distData[1])
            }
            data.append(distObj)
    
    distFinalObj = {
        "district": data,
        "updated_on" : getLastUpdatedDate()
    }

    distFinalData = json.dumps(distFinalObj)
    return HttpResponse(distFinalData, content_type="application/json")
        
def getDivisionData(request):
    districts = getDistricts()
    divisionIdMap = [3, 17, 28, 32, 40, 50, 54, 60]
    divisionMapValue = ['Dhaka', 'Chattogram', 'Sylhet', 'Rangpur', 'Khulna', 'Mymensingh', 'Barishal', 'Rajshahi']
    
    data = []
    indx = 0
    countDiv = 1
    for dist in districts:
        indx = indx + 1

        if (indx in divisionIdMap):
            distrow = dist.find_all('td')
            distData = [distcol.text.strip() for distcol in distrow]

            divObj = {
                "id" : countDiv,
                "name" : divisionMapValue[countDiv-1],
                "total" : getCountNumber(distData[3])
            }

            countDiv = countDiv + 1
            data.append(divObj)
            
    divFinalObj = {
        "division": data,
        "updated_on" : getLastUpdatedDate()
    }

    divFinalData = json.dumps(divFinalObj)
    return HttpResponse(divFinalData, content_type="application/json")

def getStatus(request):
    url = getURL()
    response = requests.get(url)
    status = response.content

    return HttpResponse(status, content_type="application/json")

def about(request):
    data = {
        "info": {
            "name": "Dipta Dhar",
            "github": "github.com/dipta-dhar",
            "intro": "Think simply & solve complex world"
        }
    }
    finalData = json.dumps(data)
    return HttpResponse(finalData, content_type="application/json")
