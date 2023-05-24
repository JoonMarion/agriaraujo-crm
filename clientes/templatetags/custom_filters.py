from django import template

register = template.Library()


@register.filter
def make_positive(value):
    return abs(value)
