from django import template

from clinic.models import Enquiry

register = template.Library()


@register.simple_tag
def enquiry_summary(limit=5):
    """Unhandled website enquiries, for the staff dashboard."""
    waiting = Enquiry.objects.filter(handled=False)
    return {'count': waiting.count(), 'recent': list(waiting[:limit])}
