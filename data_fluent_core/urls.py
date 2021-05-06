from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # AUTH
    # path('accounts/', include('accounts.urls')),
    # path('admin/', admin.site.urls),

    # HOMEPAGE
    path('', views.dashboard, name='dashboard'),
]
# This makes sure that when the /static is visited it goes to the right direcory
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
