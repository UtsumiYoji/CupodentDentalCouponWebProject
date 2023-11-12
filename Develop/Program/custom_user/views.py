from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import generic

from . import models, forms


# Create your views here.
def index(request):
    return render(request, 'custom_user/sample.html')


class CustomUserCreateView(generic.CreateView):
    model = models.CustomUsers
    form_class = forms.CustomUserForm
    template_name = 'custom_user/create.html'
    success_url = 'user'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        pass
        return ctx