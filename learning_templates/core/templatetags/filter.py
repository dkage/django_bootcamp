from django import template


register = template.Library()


@register.filter()
def cut(value, arg):
    """
    This function cuts out all values 'arg' from a given string as value
    """
    return value.replace(arg, '')
