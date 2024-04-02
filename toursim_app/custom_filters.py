# custom_filters.py

from django import template
from django.apps import apps

register = template.Library()

@register.filter(name='chunks')
def chunks(value, size):
    size = int(size)
    return [value[i:i + size] for i in range(0, len(value), size)]

# Add the following lines at the end of custom_filters.py
app_name = 'toursim_app'
app = apps.get_app_config(app_name)
register.tag('chunks', chunks, getattr(app, 'models_module', None))
