from django.shortcuts import render,redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, OrderForm
from .models import User, Order, Artwork
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.http import HttpResponse
from .decorator import user_logged_in


def logout_user(request):
    
    request.session.clear()
    return redirect('login')  

def user_details(request):
    userid = request.session.get('user_id')
    user = User.objects.get(id = userid)

    user_details = {
        'email': user.email,  
        'name': user.name  
        }
    return render(request, 'user_details.html', {'user_details': user_details})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User(
                email=form.cleaned_data['email'],
                name=form.cleaned_data['name'],
                password=form.cleaned_data['password']  
            )
            user.save()
            request.session['user_id'] = user.id
            return redirect('dashboard')  
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    request.session['user_id'] = user.id
                    return redirect('dashboard')  
                else:
                    error_message = "Invalid password"
            except User.DoesNotExist:
                error_message = "Invalid email "
    else:
        form = LoginForm()
        error_message = None

    return render(request, 'login.html', {'form': form, 'error_message': error_message})
        

def dashboard(request):
    artworks = Artwork.objects.all()
    return render(request, 'dashboard.html', {'artworks': artworks})

def artwork_details(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    if artwork.availability == 'No':
        return render(request, 'unavailable.html', {'artwork': artwork})
    return render(request, 'artdetails.html', {'artwork': artwork})
    

@user_logged_in
def place_order(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            if artwork.availability == 'No':
                return render(request, 'unavailable.html', {'artwork': artwork})
            user_id = request.session.get('user_id')
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            county = form.cleaned_data['county']

            order = Order(user_id=user_id, county=county, artwork=artwork, address=address, phone=phone)
            order.save()
            artwork.availability = 'No'
            artwork.save()
            messages.success(request, 'Order placed successfully!')
            return redirect('order_placed')
    else:
        form = OrderForm()
    if not request.session.get('user_id'):
        messages.error(request, 'You need to be logged in to place an order.')
    
    return render(request, 'place.html', {'form': form, 'artwork': artwork})

def order_placed(request):
    return render(request, 'oplaced.html')

def cont(request):
    return render(request, 'cont.html')
    
@user_logged_in
def cart(request):
    id = request.session.get('user_id')
    user_orders = Order.objects.filter(user_id=id)
    return render(request, 'cart.html', {'user_orders': user_orders})

def static_root_view(request):
    return HttpResponse(settings.STATIC_ROOT)