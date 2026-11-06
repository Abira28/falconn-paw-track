from datetime import timedelta

from django.contrib.auth.decorators import login_required
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
    }
    return render(request, 'clinic/dashboard.html', context)