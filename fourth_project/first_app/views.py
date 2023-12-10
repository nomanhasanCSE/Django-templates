from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'./first_app/home.html', context={'courses':[
        {'id': 1001,
         'course': 'Java',
         'teacher':'Noman'
         },
        {'id': 1002,
         'course': 'C++',
         'teacher':'Faruk'},
        {'id': 1003,
         'course': 'Python',
         'teacher':'Niloy'},
         ]})

def about(request):
    return render(request,'./first_app/about.html', {'author': "glenn maxwell"})