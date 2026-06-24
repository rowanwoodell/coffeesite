from django import template

register = template.Library()

@register.filter(name="pretty_list")
def pretty_list(value):
    value = [str(item) for item in value]

    if len(value) == 1:
        return value[0]
    
    all_but_last = ", ".join(value[:-1])
    return "%s and %s" % (all_but_last, value[-1])