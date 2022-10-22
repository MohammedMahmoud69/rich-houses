from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404

urlpatterns = [
    # accounts urls
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls' , namespace='accounts')),

    # allauth url
    path('accounts/', include('allauth.urls')),

    # home page url
    path('', include('home.urls' , namespace='home')),

    # admin panel url
    path('admin/', admin.site.urls),

    # api urls
    path('api-auth/', include('rest_framework.urls')),

    # products page url
    path('products/', include('products.urls' , namespace='products')),

    # cart url
    path('cart/', include('cart_app.urls' , namespace='cart')),

    # about us url
    path('about_us/', include('about_us.urls' , namespace='about_us')),

    # contact url
    path('contact/', include('contact.urls' , namespace='contact')),

    # order url
    path('order/', include('orders.urls' , namespace='order')),

    # blog url
    path('blog/' , include('blog.urls' , namespace='blog')),
]

# handel 404 page
handler404 = 'home.views.page_404'

#static & media urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
** Don't delete this **
Backend development by sitescodes ( Mohammed Hassaan )
'''