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

@register.filter
def get_batch(dictionary,key):
	key1=key[0]
	key2=key[1]
	return dictionary.get(key1, {}).get(key2)