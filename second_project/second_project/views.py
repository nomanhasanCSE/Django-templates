from django.http import HttpResponse

def home(resquest):
    return HttpResponse("This my homepage")