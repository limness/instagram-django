
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from django.views.generic.edit import CreateView

from .forms import ImageForm, DescriptionForm
from .models import Image, Description
from .serializers import ImageSerializer, DescriptionSerializer

from .utils import UpdateModelMixin
from .helpers import *

#
def index(req):
    image = Image.objects.all()
    description = Description.objects.all()
    data = form_stat()
    context = {'images': image, 'descriptions': description, 'data' : data}

    return render(req, 'image_manager/index.html', context)

#### Stats

class ShowStat(APIView):

    def get(self, request, format=None):
        """Form response data"""
        data = form_stat()
        return Response(data)

#### Images Templates

class CreateImageFromForm(CreateView):

    form_class = ImageForm
    template_name = 'image_manager/create_image.html'
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        return HttpResponse(f"form is invalid.. {str(form)}")

class CreateDescriptionFromForm(CreateView):

    form_class = DescriptionForm
    template_name = 'image_manager/create_description.html'
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        return HttpResponse(f"form is invalid.. {str(form)}")

#### Images

class CreateImage(CreateAPIView):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class DeleteImage(DestroyAPIView):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class UpdateImage(UpdateAPIView):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class RetrieveImage(RetrieveAPIView):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

#### Descriptions

class CreateDescription(CreateAPIView):

    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer

class DeleteDescription(DestroyAPIView):

    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer

class UpdateDescription(UpdateModelMixin, UpdateAPIView):

    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer

class RetrieveDescription(RetrieveAPIView):

    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
