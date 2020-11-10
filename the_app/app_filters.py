from django import template
from datetime import datetime
register = template.Library()
@register.filter(name='convert_str_date')
def convert_str_date(value):
    return str(datetime.strptime(value, '%Y-%m-%d').date())