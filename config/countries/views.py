from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Country
from django.shortcuts import get_object_or_404
from django.db.models import Count



def country_list(request):
    countries = Country.objects.all().order_by('name')

    search = request.GET.get('search', '')
    region = request.GET.get('region', '')

    if search:
        countries = countries.filter(name__icontains=search)

    if region:
        countries = countries.filter(region=region)

    paginator = Paginator(countries, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'countries/list.html', {
        'countries': page_obj,
        'regions': Country.objects.values_list('region', flat=True).distinct(),
        'search': search,
        'selected_region': region,
    })




def country_detail(request, cca3):
    country = get_object_or_404(Country, cca3=cca3)
    return render(request, 'countries/detail.html', {
        'country': country
    })
def stats(request):
    return render(request, 'countries/stats.html', {
        'total': Country.objects.count(),
        'top_population': Country.objects.order_by('-population')[:10],
        'top_area': Country.objects.order_by('-area')[:10],
        'by_region': Country.objects.values('region').annotate(total=Count('id')),
    })
