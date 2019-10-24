from django.shortcuts import render
from .models import SearchQuery



def searches_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user= request.user
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
    context = {'query': query}
    return render(request, 'searches.html', context)