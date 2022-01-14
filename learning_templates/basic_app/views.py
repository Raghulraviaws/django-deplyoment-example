from django.shortcuts import render
import datetime


def index(request):
    my_date = datetime.datetime.now()
    context_dict = {'name':'Hello World!', 'my_date':my_date}
    return render(request, 'basic_app/index.html', context= context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_templates_url.html')
