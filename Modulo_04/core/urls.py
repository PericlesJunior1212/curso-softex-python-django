from django.urls import path
from . import views # O '.' importa as 'views' do app atual


urlpatterns = [

    # Quando a URL for a raiz (''), chame a função 'home' de 'views.py'
    path('home/', views.home, name='home'),
    path('segundo/', views.segundo, name='segundo'),
]
