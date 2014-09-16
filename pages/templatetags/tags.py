from django import template
register = template.Library()

@register.simple_tag
def cut(value, arg):
    return value.replace(arg, '')


@register.assignment_tag()
def resize_image(url, width, height):
    url =  url + '?width=%s&height=%s'
    return url % (width, height)

@register.assignment_tag()
def getStr(strA , strB):
    s = strA + "  " + strB
    s = s[:40]
    return s