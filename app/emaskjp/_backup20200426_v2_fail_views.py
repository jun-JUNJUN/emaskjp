from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django import db
from django import forms
import datetime

from .models import Entity, Demand
from .forms import EntityForm, DemandForm, DemandFormSet
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
        receive_form = EntityForm(request.POST)
        is_successful = False
        if receive_form.is_valid():
            new_entity = receive_form.save(commit=False)

            InlineDemandFormsetFactory = forms.inlineformset_factory(
                Entity, Demand,
                form=DemandForm)
            received_formset_demand_mask = InlineDemandFormsetFactory(
                request.POST, request.FILES, instance=new_entity
            )
            if received_formset_demand_mask.is_valid():
                for ddd in received_formset_demand_mask:
                    n_demand = demands.save()

            else:
                is_successful = False
        else:
            is_successful = False

        if is_successful:
            return HttpResponseRedirect('/emaskjp/thanks/')
        else:
            return HttpResponse('Error-55555.')

    else:

        form_class = EntityForm()
        # reference: https://qiita.com/qtatsunishiura/items/a6cc11e025aca1c16ed1

        formset_mask = DemandFormSet(
            initial=[
                {
                    'begin_date': datetime.date(year=2020, month=4, day=1),
                    'begin_date_display': '2020年4月',
                    'demand_qty': 0},
                {
                    'begin_date': datetime.date(year=2020, month=5, day=1),
                    'begin_date_display': '2020年5月',
                    'demand_qty': 0},
                {
                    'begin_date': datetime.date(year=2020, month=6, day=1),
                    'begin_date_display': '2020年6月',
                    'demand_qty': 0},
            ]
        )

#    success_url = reverse_lazy('index')
    return render(request, 'emaskjp/inputentity.html', {
        'form': form_class,
        'formset_mask': formset_mask,
    })


def confirmview(request):
    demandFormSet = forms.formset_factory(form=DemandForm)
    if request.method == 'POST':
        form = EntityForm(request.POST)
        formset_mask = demandFormSet(request.POST, request.FILES)
        if form.is_valid():
            return render(
                request, 'emaskjp/confirmentity.html', {
                    'form': form,
                    'formset_mask': formset_mask,
                }
            )
        else:
            return render(request, 'emaskjp/inputentity.html', {
                'form': form,
                'formset_mask': formset_mask,
            }
            )
    else:
        new_form = EntityForm()
        demandFormSet = forms.formset_factory(
            form=DemandForm,
            max_num=3
        )          # reference: https://qiita.com/qtatsunishiura/items/a6cc11e025aca1c16ed1

        formset_mask = demandFormSet(
            initial=[
                {
                    'begin_date': datetime.date(year=2020, month=4, day=1),
                    'begin_date_display': '2020年4月',
                    'demand_qty': 0},
                {
                    'begin_date': datetime.date(year=2020, month=5, day=1),
                    'begin_date_display': '2020年5月',
                    'demand_qty': 0},
                {
                    'begin_date': datetime.date(year=2020, month=6, day=1),
                    'begin_date_display': '2020年6月',
                    'demand_qty': 0},
            ]
        )
        return render(request, 'emaskjp/inputentity.html', {
            'form': new_form,
            'formset_mask': formset_mask,
        }
        )


def submitview(request):
    return formview(request)


def thanksview(request):
    return render(request, 'emaskjp/thanks.html')
