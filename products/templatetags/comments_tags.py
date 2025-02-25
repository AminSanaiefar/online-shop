from django import template

register = template.Library()


@register.filter
def only_active_comments(comments):
    return comments.filter(is_active=True).order_by('-datetime_created')

