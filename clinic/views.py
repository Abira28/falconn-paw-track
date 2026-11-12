from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import render
from django.utils import timezone

from .models import Owner, Pet, Appointment, Visit


@login_required
def dashboard(request):
    today = timezone.localdate()
    todays_appointments = (
        Appointment.objects.filter(scheduled_at__date=today)
        .select_related('pet', 'pet__owner', 'vet')
    )
    follow_ups = (
        Visit.objects.filter(
            follow_up_date__gte=today,
            follow_up_date__lte=today + timedelta(days=7),
        )
        .select_related('appointment__pet', 'appointment__pet__owner')
        .order_by('follow_up_date')
    )
    context = {
        'owner_count': Owner.objects.count(),
        'pet_count': Pet.objects.count(),
        'visit_count': Visit.objects.count(),
        'todays_appointments': todays_appointments,
        'follow_ups': follow_ups,
                'today': today,
        'recent_pets': Pet.objects.select_related('owner').order_by('-created_at')[:6],
    }
    return render(request, 'clinic/dashboard.html', context)


@login_required
def pet_list(request):
    query = request.GET.get('q', '').strip()
    pets = Pet.objects.select_related('owner')
    if query:
        pets = pets.filter(
            Q(name__icontains=query)
            | Q(breed__icontains=query)
            | Q(owner__first_name__icontains=query)
            | Q(owner__last_name__icontains=query)
        )
    return render(request, 'clinic/pet_list.html', {'pets': pets, 'query': query})


@login_required
def owner_list(request):
    query = request.GET.get('q', '').strip()
    owners = Owner.objects.annotate(pet_count=Count('pets'))
    if query:
        owners = owners.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(phone__icontains=query)
        )
    return render(request, 'clinic/owner_list.html', {'owners': owners, 'query': query})

def home(request):
    return render(request, 'clinic/home.html')