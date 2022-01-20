
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_image/', views.CreateImageFromForm.as_view(), name='create_image'),
    path('create_description/', views.CreateDescriptionFromForm.as_view(), name='create_description'),
    path('api/stat/', views.ShowStat.as_view()),
    path('api/create_image/', views.CreateImage.as_view()),
    path('api/delete_image/<pk>', views.DeleteImage.as_view()),
    path('api/update_image/<pk>', views.UpdateImage.as_view()),
    path('api/retrieve_image/<pk>', views.RetrieveImage.as_view()),
    path('api/create_description/', views.CreateDescription.as_view()),
    path('api/delete_description/<pk>', views.DeleteDescription.as_view()),
    path('api/update_description/<pk>', views.UpdateDescription.as_view()),
    path('api/retrieve_description/<pk>', views.RetrieveDescription.as_view()),
]
