from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_barang_watchlist = MyWatchList.objects.all()
    pesan = ""
    context = {
    'list_mywatchlist': data_barang_watchlist,
    'nama': 'RAFI RASENDRYA FAVIAN',
    'npm' : '2106751581',
    'pesan' : ""
    }

    # Variabel untuk menyimpan data jumlah film
    belum_nonton = 0
    udah_nonton  = 0

    # Looping pengecekan film
    for movies in data_barang_watchlist :

        # Jika belum
        if (movies.film_watched == "No") :
            belum_nonton = belum_nonton + 1
        
        # Jika sudah
        elif (movies.film_watched == "Yes") :
            udah_nonton = udah_nonton + 1

        else :
            continue    
    
    # Conditional film ditonton lebih sedikit
    if (udah_nonton < belum_nonton) :
        context['pesan'] = "Wah, kamu masih sedikit menonton!"

     # Conditional film ditonton lebih banyak
    else :
        context['pesan'] = "Selamat, kamu sudah banyak menonton!"

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