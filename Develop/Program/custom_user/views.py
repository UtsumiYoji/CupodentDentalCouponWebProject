from django.contrib.auth import login
from django.contrib.auth import views
from django.db import models
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import forms as auth_forms

from . import models, forms


# Create your views here.
class CreateView(generic.CreateView):
    model = models.CustomUsers
    form_class = forms.UserCreationForm
    template_name = 'custom_user/create.html'
    success_url = '/user/detail'

    def form_valid(self, form):
        ret = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return ret

class LoginView(views.LoginView):
    template_name = 'custom_user/login.html'
    form_class = auth_forms.AuthenticationForm

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = models.CustomUsers
    template_name = 'custom_user/detail.html'
    context_object_name = 'user'
    
    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # get fields label name
        field_labels = {}
        for field in self.model._meta.fields:
            field_labels[field.name] = field.verbose_name.capitalize()
        
        # insert data
        context['labels'] = field_labels
        return context

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.CustomUsers
    form_class = forms.UserChangeForm
    template_name = 'custom_user/update.html'
    success_url = '/user/detail'

    def get_object(self, queryset=None):
        return self.request.user