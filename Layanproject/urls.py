"""
URL configuration for Layanproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mobile import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path("",views.Landpage,name='landpage'),
    path('admin/', admin.site.urls),
    path('welcome/',views.Welcome),
    path('getdata/d/',views.Getdata),
    path('senddata/<str:name>/',views.datasend),
    path('add/<int:d1>/<int:d2>',views.Add),
    path('example/<str:p1>/<str:p2>/<str:p12>/', views.example),
    path('runindex/', views.runindex),
    path('aboutus/', views.Aboutus,name='aboutus'),
    path('blog/', views.blog, name='blog'),
    path('getphone/', views.GetphoneMenu, name='getphone'),
    path('invoice/',views.invoice, name='invoice'),
    path('details/',views.Details,name='details'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('checkout/',views.Checkout,name='checkout'),
    path('auth_login/',views.auth_login,name='auth_login'),
    path('auth_register/',views.auth_register,name='auth_register'),
    path('last/',views.lastInvoice, name='last')



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
