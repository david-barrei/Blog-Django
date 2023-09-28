from django.urls import path
from pages import views as page_views


urlpatterns = [
     path('pagina/<str:slug>', page_views.page, name="page")
]



