from django import template
register = template.Library()
@register.filter('fieldtype')
def fieldtype(obj):
    return obj.__class__.__name__
