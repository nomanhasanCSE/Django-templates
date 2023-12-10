from django.shortcuts import render

from django.http import HttpResponse

def courses(resquest):
    return HttpResponse('''<h1>This is my Courses page</h1>
        <a href='/second_app/feedback' >Feedback </a>
        <a href='/second_app/courses' >Courses </a>
        <a href='/first_app/about' >About </a>
        <a href='/first_app/contact' >Contact </a>
        ''')
def feedback(resquest):
    return HttpResponse(
        '''<h1>This is my feedback page</h1>
        <a href='/second_app/feedback' >Feedback </a>
        <a href='/second_app/courses' >Courses </a>
        <a href='/first_app/about' >About </a>
        <a href='/first_app/contact' >Contact </a>
        ''')