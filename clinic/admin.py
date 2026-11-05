from django.contrib import admin
from .models import Owner, Pet, Appointment


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'phone')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'owner')
    list_filter = ('species', 'sex')
    search_fields = ('name', 'owner__first_name', 'owner__last_name')

    

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet', 'vet', 'scheduled_at', 'reason', 'status')
    list_filter = ('status', 'vet')
    search_fields = ('pet__name', 'reason')
    date_hierarchy = 'scheduled_at'