from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import views
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import forms as auth_forms

from . import models, forms


# Create your views here.
def index(request):
    pass

class CreateView(generic.CreateView):
    model = models.CustomUsers
    form_class = forms.UserCreationForm
    template_name = 'custom_user/create.html'
    success_url = '/'

    def form_valid(self, form):
        ret = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return ret

class LoginView(views.LoginView):
    template_name = 'custom_user/login.html'
    form_class = auth_forms.AuthenticationForm

# class DetailView(LoginRequiredMixin, generic.DetailView):
#     template_name = 'custom_user/detail.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user'] = self.request.user
#         return context

# class OtherView(LoginRequiredMixin, generic.UpdateView):
#     template_name = 'custom_user/update.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['users'] = User.objects.exclude(username=self.request.user.username)
#         return context