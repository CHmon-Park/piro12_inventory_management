from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from inventory.models import Inventory, Opponent


def list_inven(request):
    invens = Inventory.objects.all()
    data = {
        'invens':invens
    }
    return render(request, 'list_inven.html', data)

def create_inven(request):
    if request.method=='POST':
        name = request.POST.get('name', None)
        image = request.POST.get('image', None)
        desc = request.POST.get('desc', None)
        price = request.POST.get('price', None)
        quantity = request.POST.get('quantity', None)
        opponent = request.POST.get('opponent', None)

        if name and desc and price and quantity:
            inven = Inventory.objects.create(
                name=name,
                image=image,
                desc=desc,
                price=price,
                quantity=quantity,
                opponent=opponent
            )

            return redirect(reverse('detail_inven', kwargs={'pk':inven.pk}))
    return render(request, 'create_inven.html')



def detail_inven(request, pk):
    invens=Inventory.objects.get(pk=pk)
    data = {
        'invens':invens
    }
    return render(request, 'detail_inven.html', data)

def update_inven(request, pk):
    invens = Inventory.objects.get(pk=pk)
    data = {
        'invens':invens
    }
    return render(request, 'update_inven.html', data)

def apply_opponent(request):
    if request.method=='POST':
        name = request.POST.get('name', None)
        tel = request.POST.get('tel', None)
        address = request.POST.get('address', None)

        if name and tel and address:
            inven = Inventory.objects.create(
                name=name,
                tel=tel,
                address=address,
            )

            return redirect(reverse('detail_opponent', kwargs={'pk':inven.pk}))
    return render(request, 'apply_opponent.html')

def detail_opponent(request, pk):
    opponents = Opponent.objects.get(pk=pk)
    data = {
        'opponents':opponents
    }
    return render(request, 'detail_opponent.html', data)

def list_opponent(request):
    opponents = Opponent.objects.all()
    data = {
        'opponents':opponents
    }
    return render(request, 'list_opponent.html', data)