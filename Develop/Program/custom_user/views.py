from django.contrib.auth import login
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from . import models, forms


# Create your views here.
def index(request):
    return render(request, 'custom_user/sample.html')


class CustomUserCreateView(generic.CreateView):
    model = models.CustomUsers
    form_class = forms.CustomUserForm
    template_name = 'custom_user/create.html'
    success_url = '/'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ret = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return ret