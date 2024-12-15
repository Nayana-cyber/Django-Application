from django.shortcuts import render
from django.http import HttpResponse

# Hardcoded data for events
upcoming_events_data = [
    {"title": "Event 1", "date": "2024-05-01", "description": "Description for Event 1"},
    {"title": "Event 2", "date": "2024-06-15", "description": "Description for Event 2"},
]

past_events_data = [
    {"title": "Past Event 1", "date": "2023-01-10", "feedback": "Great event!"},
    {"title": "Past Event 2", "date": "2023-02-20", "feedback": "Learned a lot."},
]

def homepage(request):
    return render(request, 'home.html')

def upcoming_events(request):
    return render(request, 'upcoming_events.html', {'events': upcoming_events_data})

def past_events(request):
    return render(request, 'past_events.html', {'events': past_events_data})

def event_details(request, event_id):
    event = upcoming_events_data[event_id] if event_id < len(upcoming_events_data) else None
    return render(request, 'event_details.html', {'event': event})

def contact(request):
    return render(request, 'contact.html')
