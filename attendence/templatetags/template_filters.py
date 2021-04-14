from django.template.defaulttags import register
...
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def subtract(value, arg):
	try:
		return abs(value - arg)
	except:
		return 0