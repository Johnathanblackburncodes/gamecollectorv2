from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('platforms/', views.platforms_index, name='platforms_index'),
  path('platforms/<int:platform_id>/', views.platforms_detail, name='platform_detail'),
  path('platforms/create/', views.PlatformCreate.as_view(), name='platforms_create'),
  path('platforms/<int:pk>/update/', views.PlatformUpdate.as_view(), name='platforms_update'),
  path('platforms/<int:pk>/delete/', views.PlatformDelete.as_view(), name='platforms_delete'),
  path('controllers/create/', views.ControllerCreate.as_view(), name='controllers_create'),
  path('controllers/<int:pk>/update/', views.ControllerUpdate.as_view(), name='controllers_update'),
  path('controllers/<int:pk>/delete/', views.ControllerDelete.as_view(), name='controllers_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('controllers/<int:pk>/', views.ControllerDetail.as_view(), name='Controller_detail'),
  path('controllers/', views.ControllerList.as_view(), name='controllers_index'),
  path('platforms/<int:platform_id>/add_game/', views.add_game, name='add_game'),
  path('playforms/<int:platform_id>/add_photo/', views.add_photo, name='add_photo'),
  path('platforms/<int:platform_id>/assoc_controller/<int:controller_id>/', views.assoc_controller, name='assoc_controller'),
  path('platforms/<int:platform_id>/unassoc_controller/<int:controller_id>/', views.unassoc_controller, name='unassoc_controller'),
]