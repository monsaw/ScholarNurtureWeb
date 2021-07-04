from django.urls import path
from simple import views

app_name = 'simple'

urlpatterns = [
    path('', views.index , name = 'index'),
    path('home/', views.Home.as_view() , name = 'home'),
    path('about_us/', views.about_us , name = 'about'),
    path('registration/', views.registration , name = 'registration'),
    path('login/', views.sign_in , name = 'login'),
    path('logout/', views.sign_out , name = 'logout'),
    path('gallery/', views.GalleryList.as_view() , name = 'lists'),
    path('create/', views.GalleryCreate.as_view() , name = 'create'),
    path('update/<pk>/', views.GalleryUpdate.as_view() , name = 'update'),
    path('delete/<pk>/', views.GalleryDelete.as_view() , name = 'delete'),

]
