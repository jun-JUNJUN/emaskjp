from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django import db
from django import forms
import datetime

from .models import Entity, Demand
from .forms import EntityForm, DemandForm
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
        if receive_form.is_valid():
            new_entity = receive_form.save()
            DemandFormset = forms.formset_factory(form=DemandForm)
            InlineDemandFormsetFactory = forms.inlineformset_factory(
                Entity, Demand,
                form=DemandForm,
                max_num=5, can_delete=False)
            received_formset_demand_mask = InlineDemandFormsetFactory(
                request.POST, instance=new_entity
            )
            if received_formset_demand_mask.is_valid():
                for ddd in received_formset_demand_mask:
                    n_demand = demands.save()

                                                                     )
        form=EntityForm(request.POST, instance = new_entity)
        demandFormSet=forms.formset_factory(form = DemandForm)
        formset_mask=demandFormSet(request.POST, request.FILES)
        print(vars(request.POST))
        print(vars(formset_mask.))
        is_valid=True
#        for form_mm in formset_mask:
#            if not form_mm.is_valid():
#                is_valid = False
#                break

        if form.is_valid() and is_valid:
            is_successful=True
            with db.transaction.atomic():
                nnn=form.save(commit = False)
            #    formset_mask.save(commit=False)
                for form_mm in formset_mask:
                    form_mm.entity=nnn

                    nnn_mask_demand=form_mm.save(commit = False)
                    nnn_mask_demand.entity=nnn
                    nnn_mask_demand.save()

                if is_successful:
                    nnn.save()

            if is_successful:
                return HttpResponseRedirect('/emaskjp/thanks/')
            else:
                return HttpResponse('Error-55555.')
        else:
            return render(request, 'emaskjp/inputentity.html', {'form': form})

    else:
        model=Entity
        form_class=EntityForm()
        demandFormSet=forms.formset_factory(
            form = DemandForm,
            max_num = 3
        )          # reference: https://qiita.com/qtatsunishiura/items/a6cc11e025aca1c16ed1

        formset_mask=demandFormSet(
            initial = [
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
    demandFormSet=forms.formset_factory(form = DemandForm)
    if request.method == 'POST':
        form=EntityForm(request.POST)
        formset_mask=demandFormSet(request.POST, request.FILES)
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
