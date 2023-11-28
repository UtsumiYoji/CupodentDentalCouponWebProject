from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import models, forms

# Create your views here.
class CreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Companies
    form_class = forms.CreateForm
    template_name = 'company/create.html'

    def form_valid(self, form):
        ret = super().form_valid(form)
        self.request.user.company_object.add(self.object)
        self.request.user.save()
        return ret
    
    def get_success_url(self) -> str:
        return reverse('company:detail', args=[self.object.pk])

class ListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = models.Companies
    template_name = 'company/list.html'

    def test_func(self) -> bool | None:
        if not len(self.request.user.company_object.all()):
            return False
        return True
        
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()

        return redirect('/')

    def get_queryset(self):
        return self.request.user.company_object.all()

class DetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = models.Companies
    template_name = 'company/detail.html'

    def test_func(self) -> bool | None:
        for q in self.request.user.company_object.all():
            if q.id == self.kwargs.get('pk'):
                return True
        else:
            return False

    def handle_no_permission(self):
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
