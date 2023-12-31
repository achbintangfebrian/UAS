from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Shop
from datetime import datetime

def index(request) :
    context = {
        'shop_list' : Shop.objects.all()
    }
    return render(request, "shops/index.html", context)

def add(request):
    return render(request, "shops/form.html")

def save(request):
    buy = Shop(
        barang = request.POST['barang'],
        publish = request.POST['publish'],
        harga = request.POST['harga']
    )
    buy.save()

    return HttpResponseRedirect (reverse ('shops.index'))

def delete(request, buy_id):
    buy = get_object_or_404(Shop, pk=buy_id)
    buy.delete()
    return HttpResponseRedirect(reverse('shops.index'))

def edit(request, buy_id):
    buy = get_object_or_404(Shop, pk=buy_id)
    publish = buy.publish.date()
    context = {
        'id' : buy_id,
        'barang' : buy.barang,
        'publish' : publish.strftime("%Y-%m-%d"),
        'harga' : buy.harga,
    }
    return render(request, 'shops/form_edit.html', context)


def update(request, buy_id):
    buy = get_object_or_404(Shop, pk=buy_id)
    buy.barang = request.POST['barang']
    buy.publish = request.POST['publish']
    buy.harga = request.POST['harga']

    buy.save()

    return HttpResponseRedirect (reverse ('shops.index'))