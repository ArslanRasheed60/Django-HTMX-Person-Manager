from django.shortcuts import render
from .models import Person
from .forms import PersonForm
from django.db.models import Q 


def index(request):
    people = Person.objects.all().order_by('-pk')
    context = {'form': PersonForm(), 'people':people}
    return render(request, 'index.html', context)

def person_list(request):
    if request.method == 'POST':
        form = PersonForm(request.POST or None)
        if form.is_valid():
            new_person = form.save()
            people = Person.objects.order_by('-pk')

            return render(request, 'partials/person_list.html', {'people': people})
        pass

    if request.method == 'GET':
        search_query = request.GET.get('search')
        people = Person.objects.all().order_by('-pk')
        if search_query:
            people = people.filter(
                Q(name__icontains=search_query) | Q(email__icontains=search_query)
            )

        return render(request, 'partials/person_list.html', {'people': people})


