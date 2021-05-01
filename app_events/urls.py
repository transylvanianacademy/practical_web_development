from django.urls import path
# from django.views.decorators.cache import cache_page
# from django.conf import settings

from app_events.views import EventsListView, EventDetailsView

urlpatterns = [
    # this is her as an example if we want to cache this page
    # path('', cache_page(settings.REDIS_CACHED_TIME)(EventsListView.as_view()), name='events_list'),
    path('', EventsListView.as_view(), name='events_list'),
    path('event/<slug:slug>', EventDetailsView.as_view(), name='event_details'),
]
