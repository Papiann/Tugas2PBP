from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.
def show_mywatchlist(request):
    data_barang_watchlist = MyWatchList.objects.all()
    context = {
    'list_mywatchlist': data_barang_watchlist,
    'nama': 'RAFI RASENDRYA FAVIAN',
    'npm' : '2106751581'
}

    return render(request, "mywatchlist.html", context)