from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee


def home(request):
    data={
        "emp_details": {
        'vaishnavi':'1827',
        'sarita':'8289',
        'raj':'6828'
        }
    }


    # emp_list=Employee.objects.all()


    return render(request, 'home.html', data)


