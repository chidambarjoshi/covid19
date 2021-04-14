from django.shortcuts import render
import requests
import json
from dateutil.parser import parse

url = "https://covid-193.p.rapidapi.com/statistics"
headers = {
    'x-rapidapi-key': "4ddfd41466msh069fbd82db6e9bbp1c4c1ejsn4dbe74d83eaf",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers).json()


def  helloworldviews(request):
    noofresults=int(response['results'])
    mylist =[]
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])
    print(type(mylist))
    print(mylist.sort())
    selectedcountry='All'
    new=active=total=critical=recovered=deaths=newdeaths=""
    if request.POST:
        selectedcountry= request.POST['selectedcountry']
        print(selectedcountry)

    for x in range(0,noofresults):
        if selectedcountry==response['response'][x]['country']:
            new= response['response'][x]['cases']['new']
            
            active=response['response'][x]['cases']['active']
            
            total= response['response'][x]['cases']['total']
            
            critical=response['response'][x]['cases']['critical']
            
            recovered=response['response'][x]['cases']['recovered']
            
            deaths=response['response'][x]['deaths']['total']
            
            updatedtime=parse(response['response'][x]['time'])
            
            print(response['response'][x]['time'])
    context={
                'selectedcountry':selectedcountry,
                'new':new,
                'active':active,
                'total':total, 
                'critical':critical,
                'recovered':recovered,
                'deaths':deaths,
                'updatedtime':updatedtime,
                'mylist':sorted(mylist)
            }
            
    return render (request,'index.html',context)