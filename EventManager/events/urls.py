from django.urls import path
from .views import homepage, upcoming_events, past_events, event_details, contact

urlpatterns = [
    path('', homepage, name='homepage'),
    path('events/upcoming/', upcoming_events, name='upcoming_events'),
    path('events/past/', past_events, name='past_events'),
    path('event/<int:event_id>/', event_details, name='event_details'),
    path('contact/', contact, name='contact'),
]
