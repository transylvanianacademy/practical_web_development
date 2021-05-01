import datetime
import random
from lorem import paragraph

from django import template
from django.conf import settings

from app_events.models import Event


register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.simple_tag()
def docker_container_name():
    return settings.DOCKER_CONTAINER_ID


@register.simple_tag()
def simulate_db_load():
    """
    we delete 200 events and then we create 200 more
    """
    events = Event.objects.all().order_by('-date')[:200]

    year = 2021
    for e in events:
        e.delete()

    for i in range(200):
        event_object = Event()
        event_object.title = paragraph()[:random.randint(2, 10)]
        event_object.description = paragraph()
        event_object.date = datetime.datetime.strptime('{} {}'.format(random.randint(1, 365), year), '%j %Y')
        event_object.number_of_participants = random.randint(0, 100)
        event_object.save()

    return ''
