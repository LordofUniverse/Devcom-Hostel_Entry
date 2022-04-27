from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend import views

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'hostel_entries', views.Hostel_Entries, 'hostel_entries')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/', include(router.urls)),
    path('api/entry/', views.Enter_into_Hostel.as_view()),
    path('api/exit/', views.Exit_from_Hostel.as_view()),
    path('api/not_exited/', views.Details_of_not_exited.as_view()),

]
