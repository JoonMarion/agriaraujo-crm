from django import template

register = template.Library()


@register.filter
def make_positive(value):
    if value:
        return abs(value)
    else:
        return value
