from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_barang_watchlist = MyWatchList.objects.all()
    context = {
    'list_mywatchlist': data_barang_watchlist,
    'nama': 'RAFI RASENDRYA FAVIAN',
    'npm' : '2106751581'
}

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)

    # Jika JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)

    # Jika XML
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")