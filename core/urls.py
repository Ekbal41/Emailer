
from django.urls import include, path
from .views import home, bulk_mail

urlpatterns = [
    path('', home, name='home'),
    path('bulk_mail', bulk_mail, name='bulk_mail'),
    
]
