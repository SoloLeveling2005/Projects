from django import template

register = template.Library()


@register.simple_tag()
def split_str(var):
    print(var)
    var = str(var)[::-1]
    n = 3
    result = [str(var)[i:i+n] for i in range(0, len(str(var)), n)]
    result = " ".join(result)[::-1]

    return result
