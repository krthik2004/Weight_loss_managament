from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import WeightRecordForm
from .models import WeightUser, WeightRecord
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import WeightUser, WeightRecord
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from django.shortcuts import get_object_or_404
from django.contrib import messages



# Homepage with login and signup options
def homepage(request):
    return render(request, 'homepage.html')

# User signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a WeightUser instance for the newly created user
            WeightUser.objects.create(user=user)
            login(request, user)  # Automatically log in the user after signup
            return redirect('homepage.html')  # Redirect to Add Weight page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# User login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_weight.html')  # Redirect to Add Weight page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


# Add weight (restricted to logged-in users)
@login_required
def add_weight(request):
    weight_user = WeightUser.objects.get(user=request.user)

    if request.method == 'POST':
        form = WeightRecordForm(request.POST)
        if form.is_valid():
            date_today = timezone.now().date()
            if not WeightRecord.objects.filter(user=weight_user, date_added=date_today).exists():
                weight_record = form.save(commit=False)
                weight_record.user = weight_user
                weight_record.save()
                return redirect('weight_history')  # Redirect to weight history page after adding weight
            else:
                form.add_error(None, "You have already added your weight for today.")
    else:
        form = WeightRecordForm()

    return render(request, 'add_weight', {'form': form})



# View weight history (restricted to logged-in users)

@login_required
def weight_history(request):
    weight_user = WeightUser.objects.get(user=request.user)
    weight_records = WeightRecord.objects.filter(user=weight_user).order_by('-date_added')
  
    # Pagination setup
    paginator = Paginator(weight_records, 2)  # Show 5 records per page
    page = request.GET.get('page')

    try:
        weight_records = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        weight_records = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        weight_records = paginator.page(paginator.num_pages)
            # Check for any success messages from previous actions
    success_message = messages.get_messages(request)

    return render(request, 'weight_history.html',{ 
                  'weight_records': weight_records,
                   'messages': success_message,
                   })



@login_required
def user_logout(request):
    logout(request)
    return redirect('homepage')  # Redirect after logout


