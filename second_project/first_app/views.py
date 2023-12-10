from django.shortcuts import render

from django.http import HttpResponse

def about(resquest):
    return HttpResponse('''<h1>This is my About page</h1>
        <a href='/second_app/feedback' >Feedback </a>
        <a href='/second_app/courses' >Courses </a>
        <a href='/first_app/about'>About </a>
        <a href='/first_app/contact' >Contact </a>
        ''')
def contact(resquest):
    return HttpResponse('''<h1>This is my Contact page</h1>
        <a href='/second_app/feedback' >Feedback </a>
        <a href='/second_app/courses' >Courses </a>
        <a href='/first_app/about' >About </a>
        <a href='/first_app/contact' >Contact </a>
        ''')