from django import template

register = template.Library()


# Check if user has package (Filter)
@register.filter
def has_package(user, package_name):
    if user.is_authenticated:
        return user.has_package(package_name)


# Price thousands separator (Filter)
@register.filter
def format_price(value):
    if value:
        return '{:,}'.format(int(value))


# Rials to tooman (Filter)
@register.filter
def to_tooman(value):
    if value:
        value = str(value)
        return value[:-1]
