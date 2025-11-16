from django import template
import re
from django.template.defaultfilters import stringfilter

register = template.Library()


BAD_WORDS = ['редиска', 'хрюндель', 'балда']


@register.filter(name='censor')
@stringfilter
def censor(value):
    """
    Заменяет нецензурные слова на звездочки.
    """
    if not isinstance(value, str):
        raise template.TemplateSyntaxError("Фильтр 'censor' можно применять только к строковым переменным")

    for word in BAD_WORDS:
        pattern = r'(?<!\w){}(?!\w)'.format(re.escape(word))
        replacement = word[0] + '*' * (len(word) - 1)
        value = re.sub(pattern, replacement, value, flags=re.IGNORECASE)

    return value