from django import template

register = template.Library()

@register.filter(name='sum_amount')
def sum_amount(queryset):
    return sum(item.amount for item in queryset)