from django.urls import path
from .views import *
from django.views.generic.detail import DetailView
from .models import Photo
# name space --> photo:photo_upload instead of photo_upload directly
app_name = 'photo'

urlpatterns = [
    # index page is the photo list view
    # name is set to be used for href from templates
    path('', photo_list, name='photo_list'),
    path('detail/<int:pk>/', DetailView.as_view(model=Photo, template_name='photo/detail.html'), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>', PhotoUpdateView.as_view(), name='photo_update'),
]
