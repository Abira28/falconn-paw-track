from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import BookingForm, ContactForm

# ---------------------------------------------------------------------------
# EDIT THIS BLOCK: your clinic's real details. They appear across the site.
# ---------------------------------------------------------------------------
CLINIC = {
    'name': 'Falconn PawTrack Veterinary Clinic',
    'phone': '+254 700 205 777',
    'phone_link': '+254700000000',
    'email': 'info@falconnpawtrack.com',
    'address': 'Afya Center, Nairobi, Kenya',
    'map_query': 'Nairobi, Kenya',  # replace with your full address for an accurate map
}

# Opening hours used by the "Open now" badge. Monday is 0, Sunday is 6.
# Each entry is (opening hour, closing hour) in 24-hour time. Missing days are closed.
OPENING = {
    0: (8, 18), 1: (8, 18), 2: (8, 18), 3: (8, 18), 4: (8, 18),
    5: (9, 14),
}

# The same hours written out for visitors. Keep this in step with OPENING above.
HOURS_DISPLAY = [
    ('Monday to Friday', '8:00 am to 6:00 pm'),
    ('Saturday', '9:00 am to 12:00 pm'),
    ('Sunday', 'Closed, emergencies by phone'),
]

SERVICES = [
    ('Everyday care', [
        ('Check-ups', 'A full nose-to-tail exam, with advice on diet, weight and behaviour.'),
        ('Vaccinations', 'Core vaccines on schedule, with a reminder before each one is due.'),
        ('Parasite control', 'Deworming plus tick and flea prevention suited to your pet.'),
        ('Microchipping', 'A quick, permanent ID so a lost pet can be traced back to you.'),
    ]),
    ('Treatment', [
        ('Illness and injury', 'Diagnosis and treatment for infections, wounds, limping and sudden changes.'),
        ('Eyes and skin', 'Care for eye problems, rashes, allergies and hair loss.'),
        ('Dental care', 'Examination and cleaning to keep teeth and gums healthy.'),
        ('Laboratory tests', 'Blood, urine and stool tests, with results explained in plain language.'),
    ]),
    ('Surgery and emergencies', [
        ('Surgery', 'Spaying, neutering and soft-tissue operations, with pain relief and aftercare.'),
        ('Emergency care', 'Call us first, any day, and we will tell you how to get your pet seen.'),
        ('Livestock visits', 'Farm calls for cattle, goats, sheep and poultry, by arrangement.'),
    ]),
]
# ---------------------------------------------------------------------------


def _clock(hour):
    return f"{hour % 12 or 12}:00 {'am' if hour < 12 else 'pm'}"


def _status():
    now = timezone.localtime()
    hours = OPENING.get(now.weekday())
    current = now.hour + now.minute / 60
    if hours and hours[0] <= current < hours[1]:
        return {'open': True, 'text': f"Open now, until {_clock(hours[1])}"}
    return {'open': False, 'text': 'Closed right now'}


def _render(request, template, context=None):
    data = {
        'clinic': CLINIC,
        'hours': HOURS_DISPLAY,
        'status': _status(),
    }
    data.update(context or {})
    return render(request, template, data)


def home(request):
    everything = [item for _, items in SERVICES for item in items]
    return _render(request, 'clinic/home.html', {'featured': everything[:6]})


def about(request):
    return _render(request, 'clinic/about.html')


def services(request):
    return _render(request, 'clinic/services.html', {'groups': SERVICES})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.kind = 'GENERAL'
            enquiry.save()
            return redirect('thanks')
    else:
        form = ContactForm()
    return _render(request, 'clinic/contact.html', {'form': form})


def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.kind = 'BOOKING'
            enquiry.save()
            return redirect('thanks')
    else:
        form = BookingForm()
    return _render(request, 'clinic/book.html', {'form': form})


def thanks(request):
    return _render(request, 'clinic/thanks.html')
