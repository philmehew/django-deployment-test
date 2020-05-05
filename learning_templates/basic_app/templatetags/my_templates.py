from django import template

register  = template.Library()

def cutfunc(value,arg):
  """
  This cuts out all values of agr from the SyntaxWarning
  """
  return value.replace(arg,"")
register.filter('philcut',cutfunc)

@register.filter(name='anothercut')  # using decorator function instead of passing a function to a function
def altcutfunc(value,arg):
  """
  This cuts out all values of agr from the SyntaxWarning
  """
  return value.replace(arg,"")
#register.filter('philcut',cutfunc)
