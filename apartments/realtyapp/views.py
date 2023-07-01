from django.shortcuts import render, get_object_or_404, redirect
from .models import Apartment, ApartmentImage, Favorites, Purchases
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import floatformat

User = get_user_model()

def index(request):
    apartments = Apartment.objects.all()
    images_list = ApartmentImage.objects.filter(apartment__in=apartments)
    if request.user.is_authenticated:
        user_favorites = request.user.favorites.values_list('apartment_id', flat=True)
    else:
        user_favorites = []
    context = {
        'apartments': apartments,
        'images': images_list,
        'user_favorites': user_favorites,
    }

    return render(request, './index.html', context)


def new_buildings(request):
    apartments = Apartment.objects.filter(category='New Buildings')
    images_list = ApartmentImage.objects.filter(apartment__in=apartments)
    if request.user.is_authenticated:
        user_favorites = request.user.favorites.values_list('apartment_id', flat=True)
    else:
        user_favorites = []
    context = {
        'apartments': apartments,
        'images': images_list,
        'user_favorites': user_favorites,
    }

    return render(request, './new_buildings.html', context)


@login_required(login_url='login')
def favorites(request):
    user_favorites = request.user.favorites.values_list('apartment_id', flat=True)

    # Get the list of favorite apartments
    favorite_apartments = Apartment.objects.filter(id__in=user_favorites)

    # Get the images associated with the favorite apartments
    images_list = ApartmentImage.objects.filter(apartment__in=favorite_apartments)
    context = {
        'user_favorites': user_favorites,
        'images': images_list,
        'apartments': favorite_apartments,
    }
    return render(request, 'favorites.html', context)

@login_required(login_url='login')
def purchases(request):
    user_purchases = Purchases.objects.filter(user=request.user).distinct()
    purchases_apartments = [purchase.apartment_id for purchase in user_purchases]
    images_list = ApartmentImage.objects.filter(apartment__in=purchases_apartments)
    context = {
        'user_purchases': user_purchases,
        'images': images_list,
        'apartments': purchases_apartments,
    }
    print(purchases_apartments)
    return render(request, 'purchases.html', context)
    


def garages(request):
    apartments = Apartment.objects.filter(category='Garages')
    images_list = ApartmentImage.objects.filter(apartment__in=apartments)
    if request.user.is_authenticated:
        user_favorites = request.user.favorites.values_list('apartment_id', flat=True)
    else:
        user_favorites = []
    context = {
        'apartments': apartments,
        'images': images_list,
        'user_favorites': user_favorites,
    }
    return render(request, './garages.html', context)

def houses(request):
    apartments = Apartment.objects.filter(category='Houses')
    images_list = ApartmentImage.objects.filter(apartment__in=apartments)
    
    if request.user.is_authenticated:
        user_favorites = request.user.favorites.values_list('apartment_id', flat=True)
    else:
        user_favorites = []
    context = {
        'apartments': apartments,
        'images': images_list,
        'user_favorites': user_favorites,
    }
    
    return render(request, './houses.html', context)

def apartment(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    price_for_square = apartment.price / apartment.area
    formatted_price_for_square = floatformat(price_for_square, 2)
    if request.user.is_authenticated:
        user_favorites = request.user.favorites.values_list('apartment_id', flat=True)
        purchases = request.user.purchases.values_list('apartment_id', flat=True)
    else:
        purchases = []
        user_favorites = []
    
    context = {
        'apartment': apartment,
        'user_favorites': user_favorites,
        'purchases': purchases,
        'price_for_square': formatted_price_for_square,
    }
    return render(request, './apartment.html', context)

def apartment_test(request):
    return render(request, './apartment.html')

@login_required(login_url='login')
def add_to_favorites(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    user_id = request.user
    Favorites.objects.create(user=user_id, apartment_id=apartment)
    next_url = request.GET.get('next')  # Assumes 'next' is passed as a query parameter in the URL

    return redirect(next_url)

@login_required(login_url='login')
def add_to_purchases(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    user_id = request.user
    Purchases.objects.create(user=user_id, apartment_id=apartment)    
    return redirect('apartment', id=apartment.id)


@login_required(login_url='login')
def delete_from_favorites(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    user_id = request.user
    Favorites.objects.filter(user_id=user_id, apartment_id=apartment.id).delete()
    # Get the 'next' parameter from the request (URL or form data)
    next_url = request.GET.get('next')  # Assumes 'next' is passed as a query parameter in the URL

    if next_url:
        # If 'next' parameter exists, redirect to the provided URL
        return redirect(next_url)
