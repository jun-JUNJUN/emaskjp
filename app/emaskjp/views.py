from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django import db
from django import forms
import datetime

from .models import Entity, Demand, Supply, SupplyRequest
from .forms import EntityForm, DemandForm, DemandFormSet3, SupplierForm, SupplierContactForm, SupplyForm

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
        with db.transaction.atomic():
            if receive_form.is_valid():
                new_entity = receive_form.save(commit=False)

                received3 = DemandFormSet3(request.POST)
            if received3.is_valid():
                demandf1 = DemandForm()
                demand0 = demandf1.save(commit=False)
                demand0.entity = new_entity
                demand0.begin_date = received3.cleaned_data['demand0_date']
                demand0.begin_date_display = received3.cleaned_data['demand0_date_display']
                demand0.demand_qty = received3.cleaned_data['demand0_qty']
                demandf1 = DemandForm()
                demand1 = demandf1.save(commit=False)
                demand1.entity = new_entity
                demand1.begin_date = received3.cleaned_data['demand1_date']
                demand1.begin_date_display = received3.cleaned_data['demand1_date_display']
                demand1.demand_qty = received3.cleaned_data['demand1_qty']
                demandf2 = DemandForm()
                demand2 = demandf2.save(commit=False)
                demand2.entity = new_entity
                demand2.begin_date = received3.cleaned_data['demand2_date']
                demand2.begin_date_display = received3.cleaned_data['demand2_date_display']
                demand2.demand_qty = received3.cleaned_data['demand2_qty']

                srequest0 = SupplyRequest()
                srequest0.entity = new_entity
                srequest0.begin_date = received3.cleaned_data['demand0_date']
                srequest0.request_qty = received3.cleaned_data['demand0_qty']

                valid = new_entity.save()
                valid = demand0.save()
                valid = demand1.save()
                valid = demand2.save()
                valid = srequest0.save()
                is_successful = True

            else:
                is_successful = False

        if is_successful:
            return HttpResponseRedirect('/emaskjp/thanks/')
        else:
            return HttpResponse('Error-55555.')

    else:

        form_class = EntityForm()
        # reference: https://qiita.com/qtatsunishiura/items/a6cc11e025aca1c16ed1

        formset3 = DemandFormSet3(
            initial={
                'demand0_date': datetime.date(year=2020, month=5, day=1),
                'demand0_qty': 0,
                'demand0_date_display': '2020年5月',
                'demand1_date': datetime.date(year=2020, month=6, day=1),
                'demand1_qty': 0,
                'demand1_date_display': '2020年6月',
                'demand2_date': datetime.date(year=2020, month=7, day=1),
                'demand2_qty': 0,
                'demand2_date_display': '2020年7月',
            }
        )
        #    success_url = reverse_lazy('index')
        return render(request, 'emaskjp/inputentity.html', {
            'form': form_class,
            'formset3': formset3,
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


def supplysubmitview(request):
    return supplyformview(request)

# ここに表示するのは、所要の一覧です。Demandでは無いです。


def supplyformview(request):
    if request.method == 'POST':
        return render(request, 'emaskjp/XXXX.html')
    else:
        form_supply = SupplyForm()
        form_supplier = SupplierForm()
        form_suppliercontact = SupplierContactForm()

        supplyreqs = SupplyRequest.objects.filter(
            request_qty__gt='0').order_by('begin_date', 'last_calculated')[:2]

        return render(
            request,
            'emaskjp/supplyinput.html',
            {
                'form_supply': form_supply,
                'form_supplier': form_supplier,
                'form_suppliercontact': form_suppliercontact,
                'selected_reqs': supplyreqs,
            }
        )

# ここは、最近入力されたSupplyRequest を表示すべきなのは、所要の一覧です。


def toppageview(request):
    queryRequest = SupplyRequest.objects.filter(
        request_qty__gt='0').order_by('begin_date', 'last_calculated')[:5]
    context = {
        'supplyrequest_top': queryRequest,
    }

#    for rrr in queryRequest:
#        print(rrr.entity)
#        print(rrr.entity.entity_name)

    return render(request, 'emaskjp/top.html', context)


def cmdupdate(request):
    SupplyRequest.objects.all()

    context = {
        'item': 'xxx'
    }
    return render(request, 'emaskjp/mgmt_request.html', context)
