from django import template

register = template.Library()


@register.filter(name='fcut')   # decorators 
def fcut(value,arg):
    """
this curt out all value "arg" from string !
    """
    return value.replace(arg,'')




#register.filter('cut',fcut)     >>decorators 
