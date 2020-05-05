from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import RFI
# Create your views here.


def home(request):
    a = 33
    b = 22
    c = a + b
    return HttpResponse('Hello, Django in Docker!')


def listRFItext(request):
    latest_RFI_list = RFI.objects.order_by('-create_dt')[:5]
    output = ', '.join([r.customer_name for r in latest_RFI_list])
    return HttpResponse(output)


def listRFI(request):
    latest_RFI_list = RFI.objects.order_by('-create_dt')[:5]
    context = {
        'latest_RFI_list': latest_RFI_list,
    }
    return render(request, 'forwarderchat/list.html', context)


def detailRFI(request, RFI_id):
    try:
        rr = RFI.objects.get(pk=RFI_id)
    except RFI.DoesNotExist:
        raise Http404("Something trouble [ERR-50001]")
    return render(request, 'forwarderchat/detail.html', {'RFI': rr})


def testforminput(request):
    error_message = ''
    context = {
        'error_message': error_message,
    }
    return render(request, 'forwarderchat/testforminput.html', context)


def inputrfi(request):
    return render(request, 'forwarderchat/detail.html')
