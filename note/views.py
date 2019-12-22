from django.shortcuts import render , redirect , reverse
from .models import *
from datetime import date , timedelta

# Create your views here.

def review_entry(request):
    if request.method == 'POST':
        entry_id = request.POST.get('entry_id')
        days = int(request.POST.get('days'))
        e = Entry.objects.get(id = entry_id)
        e.review_date = e.review_date + timedelta(days = days)
        e.days_between = days
        e.save()
        return redirect(reverse('review_entry'))
    entrys = Entry.objects.filter(review_date__lte = date.today())
    entry_id = request.GET.get('entry_id')
    if entry_id:
        entry = Entry.objects.get(id = entry_id)
    else:
        entry = entrys.first()
    context = {}
    context['entrys'] = entrys
    context['entry'] = entry
    return render(request , 'review_entry.html' , context)
        
        