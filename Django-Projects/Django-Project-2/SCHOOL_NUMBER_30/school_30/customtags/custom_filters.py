from django import template


register = template.Library()

@register.filter(name='experience_years')
def experience_years(value):
    if 11 <= value % 100 <= 14:
        return f"{value} лет"
    if value % 10 == 1:
        return f"{value} год"
    if 2 <= value % 10 <= 4:
        return f"{value} года"
    return f"{value} лет"

@register.filter(name='total_staff_count')
def total_staff_count():
    return None

