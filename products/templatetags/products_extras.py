from django import template

register = template.Library()



@register.filter(name='relatedget')
def related_fields_get(values, pid):
    for value in values:
        if value.product.id == pid:
            return value
        else:
            return False

    
