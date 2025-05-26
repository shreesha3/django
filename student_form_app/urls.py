from django.contrib import admin
from django.urls import path
from students.views import student_form
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_form, name='student_form'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
