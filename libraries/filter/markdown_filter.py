from django import template
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])

#1. 先執行 stringfilter(markdown)
#2. 把stringfilter(markdown) 代回 register.filter register.filter(stringfilter(markdown))
## 1.2. 相當於 register.filter(stringfilter(markdown))