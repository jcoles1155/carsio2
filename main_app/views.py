from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import CarPost
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CommentForm
import uuid
import boto3
from .models import CarPost, Photo

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

# # route for cars index
def cars_index(request):
    cars = CarPost.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
    car = CarPost.objects.get(id=car_id)
    print(car)
    comment_form = CommentForm()
    return render(request, 'cars/detail.html', { 
        'car': car, 'comment_form': comment_form 
    })

class CarCreate(CreateView):
    model = CarPost
    fields = '__all__'

class CarUpdate(UpdateView):
    model = CarPost
    fields = ['title', 'make', 'carModel', 'color', 'year', 'body', 'description']

class CarDelete(DeleteView):
    model = CarPost
    success_url = '/cars/'

def add_comment(request, car_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.car_id = car_id
        new_comment.save()
    return redirect('detail', car_id=car_id)

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