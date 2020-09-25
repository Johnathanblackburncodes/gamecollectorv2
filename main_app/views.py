from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic  import DetailView, ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GameForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'gamecollec'

import uuid
import boto3
from .models import Platform, Controller, Photo


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def platforms_index(request):
  platforms = Platform.objects.filter(user=request.user)
  return render(request, 'platforms/index.html', { 'platforms': platforms })

def platforms_detail(request, platform_id):
  platform = Platform.objects.get(id=platform_id)
  controllers_platform_doesnt_have = Controller.objects.exclude(id__in = platform.controllers.all().values_list('id'))
  game_form = GameForm()
  return render(request, 'platforms/detail.html', {
    'platform': platform, 'game_form': game_form,
    'controllers': controllers_platform_doesnt_have
  })

@login_required
def add_game(request, platform_id):
  form = GameForm(request.POST)
  if form.is_valid():
    new_game = form.save(commit=False)
    new_game.platform_id = platform_id
    new_game.save()
  return redirect('platform_detail', platform_id=platform_id)

@login_required
def assoc_controller(request, platform_id, controller_id):
    Platform.objects.get(id=platform_id).controllers.add(controller_id)
    return redirect('platform_detail', platform_id=platform_id)

@login_required
def unassoc_controller(request, platform_id, controller_id):
    Platform.objects.get(id=platform_id).controllers.remove(controller_id)
    return redirect('platform_detail', platform_id=platform_id)

@login_required
def add_photo(request, platform_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, cat_id=cat_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('platform_detail', platform_id=platform_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class PlatformCreate(LoginRequiredMixin, CreateView):
  model = Platform
  fields = '__all__'
  success_url = '/platforms/'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class PlatformUpdate(LoginRequiredMixin, UpdateView):
  model = Platform
  fields = ['name', 'release_year']

class PlatformDelete(LoginRequiredMixin, DeleteView):
  model = Platform
  success_url = '/platforms/'

class ControllerCreate(LoginRequiredMixin, CreateView):
  model = Controller
  fields = '__all__'

class ControllerDetail(LoginRequiredMixin, DetailView):
  model = Controller

class ControllerList(LoginRequiredMixin, ListView):
  model = Controller

class ControllerUpdate(LoginRequiredMixin, UpdateView):
  model = Controller
  fields = '__all__'

class ControllerDelete(LoginRequiredMixin, DeleteView):
  model = Controller
  success_url = '/controllers/'