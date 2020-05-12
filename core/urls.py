from django.urls    import path
from .              import views

urlpatterns = [
    path('', views.inprocces, name='inprocces'),
    path('done', views.done, name='done'),
]