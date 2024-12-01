
from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from home.views import * 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('produce/', produce, name='produce'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('homemenu/', homemenu, name='homemenu'),
    path('menu/', menu, name='menu'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('product/', product, name='product'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 