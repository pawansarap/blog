from django.contrib import admin
from django.urls import path, include
from blog import views
from blog.views import blog_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginuser, name='loginuser'),
    path('logout', views.logoutuser, name='logoutuser'),
    # path('blog', views.blog, name='blog'),
    path('add-blog', views.add_blog, name='add-blog'),
    path('blog', views.blog_view, name='blog'),
    path('contact', views.contact, name='contact')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)