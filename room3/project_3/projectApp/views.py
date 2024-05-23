from django.shortcuts import render
import datetime
def home(request):
    d={'Author':'Asif','age':20 ,'val':[1,5,6,7,8],'list':['python','is','best'],'Birthday':datetime.datetime.now() ,'course':[
        {
            'id':1,
            'Name':'python',
            'fee':5502
        },
        {
            'id':2,
            'Name':'django',
            'fee':3202
        },
        {
            'id':2,
            'Name':'c++',
            'fee':2502
        }
    ]}
    return render(request,'project/home.html',d)
 