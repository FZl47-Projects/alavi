from django import template

register = template.Library()


# Check user packages template tag
@register.filter
def has_package(user, package_name):
    return user.has_package(package_name)
