from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import CarPost
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
import uuid
import boto3
from .models import CarPost, Photo, UserProfile

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'carsio'

# class Car:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, manufacturer, year, carModel, color, body, isAvailable):
#         self.manufacturer = manufacturer
#         self.year = year
#         self.carModel = carModel
#         self.color = color
#         self.body = body

# cars = [
#     Car('Ford', '2011', 'F150', 'Grey', 'Crew Cab', True),
#     Car('Toyota', '2016', 'Tundra', 'Cobalt', 'Super Cab', True),
#     Car('Mercedes', '2017', 'S-Class', 'Blue',  'Coupe', False)
# ]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profile(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    context = {
        'profile': profile
    }
    print(profile)
    return render(request, 'profile/profile.html', context)


# # route for cars index
@login_required
def cars_index(request):
    print('testing', request.GET.get('make'))
    if request.GET.get('make'):
        cars = CarPost.objects.filter(make=request.GET.get('make'))
        return render(request, 'cars/index.html', { 'cars': cars })
    cars = CarPost.objects.filter(user=request.user)
    return render(request, 'cars/index.html', { 'cars': cars })

@login_required
def cars_detail(request, car_id):
    car = CarPost.objects.get(id=car_id)
    print(car)
    comment_form = CommentForm()
    return render(request, 'cars/detail.html', { 
        'car': car, 'comment_form': comment_form 
    })

def profiles_index(request):
    profile = UserProfile.objects.filter(user=request.user)
    return render(request, 'profile/profile.html', { 'profile': profile })

class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['proName', 'proLoc', 'proOcc', 'age', 'favoriteCar', 'carsOwned', 'carsOwn']

class CarCreate(LoginRequiredMixin, CreateView):
    model = CarPost
    fields = ['title', 'make', 'carModel', 'color', 'year', 'body', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = CarPost
    fields = ['title', 'make', 'carModel', 'color', 'year', 'body', 'description']

class CarDelete(LoginRequiredMixin, DeleteView):
    model = CarPost
    success_url = '/cars/'

@login_required
def add_comment(request, car_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.car_id = car_id
        new_comment.save()
    return redirect('detail', car_id=car_id)

@login_required
def add_photo(request, car_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, car_id=car_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', car_id=car_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            found_user = User.objects.get(id=user.id)
            user_profile = UserProfile(user=found_user)
            # user_profile.user = found_user
            user_profile.save()
            login(request, user)
            return redirect('profile_update', pk=user_profile.id)
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context) 

# class CarsFilter(BaseFilter):
#     search_fields = {
#         'search_text' : ['title', 'make', 'carModel', 'color', 'body', 'description', 'user'],
#         'search_year_exact' : { 'operator' : '__exact', 'fields' : ['year'] }
#     }

# class CarsSearchList(SearchListView):
#     model = CarPost
#     paginate_by = 10
#     template_name = "cars/index.html"
#     form_class = SearchForm
#     filter_class = CarsFilter