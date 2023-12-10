
from django import template
from django.template.loader import get_template

register = template.Library()

def my_template(value,arg):
    if arg =='change':
       value = 'Rahim'
       return value
    if arg == 'title':
       return value.title()
def get_courses():
    courses = [
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
         ]
    return {'courses': courses}

courses_template = get_template('first_app/courses.html')
register.filter('change_name', my_template)
register.inclusion_tag(courses_template) (get_courses)
        
