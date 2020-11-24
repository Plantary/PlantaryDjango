from django.conf.urls import url,include
from django.contrib import admin
#from ourdiary import views
import Main.views
import ourdiary.views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('ourdiary/', include('ourdiary.urls')),
    path('', Main.views.ourdiary_list, name = 'home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

