from django.contrib import admin
from django.urls import path,include
from searches.views import searches_view
from .views import home_page,contact_page,about_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('djangoblog.urls')),
    
    path('contact', contact_page),
    path('searches/', searches_view),
]
