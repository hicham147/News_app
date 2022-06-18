from django.shortcuts import render
import requests
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def home(request):
    date_today = date.today()
    category_list = ['fashion','sport','business','technology','travel','news',"stories","Climate"]

    result_list = []
    url = (
            'https://newsapi.org/v2/top-headlines?'
            'q=news&'
            'from=date_today'
            'sortBy=popularity&'
            'apiKey=cffb758a2a4e4ab5b6e2bea10b383593')

    response = requests.get(url)
    result = response.json()
        


    context = {"result":result['articles'],
               "date_today":date_today}
    return render(request,'home.html',context)
 




 



def about(request):
    return render(request,'about.html')
    
def contect(request):
    return render(request,'contact.html')
    
    
    
def page(request):
    return render(request,'page.html')