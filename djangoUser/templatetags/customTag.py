from django import template

register =template.Library()

def getElement(data,key):
    a=data[key]
    return a

register.filter('getElement',getElement)
