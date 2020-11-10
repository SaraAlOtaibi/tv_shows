from django import template
import datetime
register = template.Library()
@register.filter(name='convert_str_date')
def convert_str_date(value):
    return value.strftime('%Y-%m-%d')
    #return str(datetime.date.strftime(value, '%Y-%m-%d').date())