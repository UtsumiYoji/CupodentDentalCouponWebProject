from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()

@register.filter
@stringfilter
def markdown_to_html(value):
    return markdown.markdown(value)

@register.filter
def clac_discount(normal, offer):
    print(normal, offer)
    normal = float(normal)
    offer = float(offer)
    result = 100 * ((normal-offer)/normal)
    result = str(round(result))
    return result