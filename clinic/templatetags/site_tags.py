from django import template

from clinic.service_info import FAQS, SERVICE_DETAILS

register = template.Library()


@register.simple_tag
def service_detail(name):
    """What is included in a service, or an empty dict if we have no details."""
    return SERVICE_DETAILS.get(name, {})


@register.simple_tag
def faq_list():
    return FAQS
