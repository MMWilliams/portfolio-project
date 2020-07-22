
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static #serve up images
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')), #if blog appears in the url, send to blog urls.py file
    #includes all urls from blog/urls.py
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #this is where we should look for files
