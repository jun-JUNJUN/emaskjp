from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .models import Entity
from .forms import EntityForm
# Create your views here.

"""
def home(request):
    topDemand = Demand.objects.order_by  # todo: 何をSort基準として表示するのか、考えること
    context = {
        'topDemand': topDemand,
    }
    return render(request, 'emaskjp/home.html', context)
"""


def formview(request):
    # if this is a POST request, we need to process validation of retriving data
    if request.method == 'POST':
        # create a form instance and process retriving data
        new_entity = Entity()
        form = EntityForm(request.POST, instance=new_entity)
        if form.is_valid():
            nnn = form.save()
    # form.save_m2m()
            return HttpResponseRedirect('/thanks/')
        else:
            return render(request, 'emaskjp/inputentity.html', {'form': form})

    else:
        model = Entity
        form_class = EntityForm()
#    success_url = reverse_lazy('index')
    return render(request, 'emaskjp/inputentity.html', {'form': form_class})
