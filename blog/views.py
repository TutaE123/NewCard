from django.shortcuts import render
from django.utils import timezone
from .models import Denunc, Koloda, Cart
from django.shortcuts import render, get_object_or_404
from .forms import DenuncForm, KolodaForm, CartForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



def koloda_list(request):
    kolodas = Koloda.objects.all()
    return render(request, 'blog/koloda_list.html', {'kolodas': kolodas})

def koloda_detail(request, pk):
    koloda = get_object_or_404(Koloda, pk=pk)
    return render(request, 'blog/koloda_detail.html', {'koloda': koloda})


@login_required
def koloda_new(request):
    if request.method == "POST":
        form = KolodaForm(request.POST)
        if form.is_valid():
            koloda = form.save(commit=False)
            koloda.author = request.user
            koloda.save()
            return redirect('koloda_detail', pk=koloda.pk)
    else:
        form = KolodaForm()
    return render(request, 'blog/koloda_edit.html', {'form': form})

 
@login_required
def koloda_edit(request, pk):
    koloda = get_object_or_404(Koloda, pk=pk)
    if request.method == "POST":
        form = KolodaForm(request.POST, instance=koloda)
        if form.is_valid():
            koloda = form.save(commit=False)
            koloda.author = request.user
            koloda.save()
            return redirect('koloda_detail', pk=koloda.pk)
    else:
        form = KolodaForm(instance=koloda)
    return render(request, 'blog/koloda_edit.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = UserCreationForm()
    return render(request, 'registration/register.html', {'register_form': register_form})


def profil(request):
    return render(request, 'blog/profil.html')




def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'blog/card_detail.html', {'carts': carts})

def cart_detail(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    return render(request, 'blog/cart_list.html', {'cart': cart})

@login_required
def cart_new(request):
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.save()
            return redirect('card_detail', pk=cart.pk)
    else:
        form = CartForm()
    return render(request, 'blog/cart_edit.html', {'form': form})

@login_required
def cart_edit(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    if request.method == "POST":
        form = CartForm(request.POST, instance=cart)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.author = request.user
            cart.save()
            return redirect('koloda_detail', pk=cart.pk)
    else:
        form = CartForm(instance=cart)
    return render(request, 'blog/cart_edit.html', {'form': form})
