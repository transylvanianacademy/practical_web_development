import datetime
import random
from lorem import paragraph

from django.core.management.base import BaseCommand

from app_events.models import Event


class Command(BaseCommand):

    @staticmethod
    def create_events():
        number_of_events = random.randrange(10000)
        year = 2021

        for i in range(number_of_events):
            event_object = Event()
            event_object.title = paragraph()[:random.randint(2, 10)]
            event_object.description = paragraph()
            event_object.date = datetime.datetime.strptime('{} {}'.format(random.randint(1, 365), year), '%j %Y')
            event_object.number_of_participants = random.randint(0, 100)
            event_object.save()

    def handle(self, *args, **kwargs):
        print("Please wait until we populate the DB with events.")
        self.create_events()
        print("Thank you! You can now start to use the app.")
