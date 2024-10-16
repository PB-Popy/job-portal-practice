
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobfeedPage/',jobfeedPage,name='jobfeedPage'),
    path('loginPage/',loginPage,name='loginPage'),
    path('signupPage/',signupPage,name='signupPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

