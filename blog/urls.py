from django.contrib import admin
from django.urls import path, include
from blog import views
from blog.views import blog_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('https://pawansarap.github.io/blog/', views.home, name='home'),
    path('https://pawansarap.github.io/blog/login', views.loginuser, name='loginuser'),
    path('https://pawansarap.github.io/blog/logout', views.logoutuser, name='logoutuser'),
    # path('blog', views.blog, name='blog'),
    path('https://pawansarap.github.io/blog/add-blog', views.add_blog, name='add-blog'),
    path('https://pawansarap.github.io/blog/blog', views.blog_view, name='blog'),
    path('https://pawansarap.github.io/blog/contact', views.contact, name='contact')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)