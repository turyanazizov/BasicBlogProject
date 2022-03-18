from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # path('jet/', include('jet.urls','jet')),
    # path('jet/dashboard',include('jet.dashboard.urls','jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('about/', include('about.urls', namespace='about')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
