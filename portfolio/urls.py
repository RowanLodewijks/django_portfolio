from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import werken.views
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', werken.views.home, name='home'),
    path('werken/', include('werken.urls')),
    
    # navbar links
    path('aboutme/', views.aboutme, name='aboutme'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 