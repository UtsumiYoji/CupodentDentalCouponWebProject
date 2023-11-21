from typing import Any
from django.contrib.auth import login
from django.contrib.auth import views
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import forms as auth_forms
from django.shortcuts import redirect

from . import models, forms


# Create your views here.
class UserCreateView(generic.CreateView):
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

class UserDetailView(LoginRequiredMixin, generic.DetailView):
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
        context['labels'] = field_labels

        return context

class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.CustomUsers
    form_class = forms.UserChangeForm
    template_name = 'custom_user/update.html'
    success_url = '/user/detail'

    def get_object(self, queryset=None):
        return self.request.user
    
class CompanyCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Companies
    form_class = forms.CompanyCreateForm
    template_name = 'custom_user/company_create.html'
    success_url = '/user/company/detail'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ret = super().form_valid(form)
        self.request.user.company_object.add(self.object)
        self.request.user.save()
        return ret

class CompanyListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = models.Companies
    template_name = 'custom_user/company_list.html'

    def test_func(self) -> bool | None:
        if not len(self.request.user.company_object.all()):
            return False
        return True
        
    def handle_no_permission(self) -> HttpResponseRedirect:
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()

        return redirect('/')

    def get_queryset(self) -> QuerySet[Any]:
        return self.request.user.company_object.all()

class CompanyDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = models.Companies
    template_name = 'custom_user/company_detail.html'

    def test_func(self) -> bool | None:
        for q in self.request.user.company_object.all():
            if q.id == self.kwargs.get('pk'):
                return True
        else:
            return False

    def handle_no_permission(self) -> HttpResponseRedirect:
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()

        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # get fields label name
        field_labels = {}
        for field in self.model._meta.fields:
            field_labels[field.name] = field.verbose_name.capitalize()
        context['labels'] = field_labels

        # get company member data
        context['members'] = self.object.customusers_set.all()

        return context
    
