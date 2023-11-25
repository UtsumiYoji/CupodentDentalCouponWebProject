from typing import Any
from django.db import models
from django.urls import reverse
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import generic

from . import models, forms

# Create your views here.
class CouponCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = models.Coupons
    form_class = forms.CouponCreateForm
    template_name = 'coupon/create.html'
    success_url = '/create/image'

    def test_func(self) -> bool | None:
        if not len(self.request.user.company_object.all()):
            return False
        return True

    def handle_no_permission(self) -> HttpResponseRedirect:
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()

        return redirect('/')

    # Comapny option are filtered by user belong
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['company_object'].queryset  = self.request.user.company_object.all()
        return form
    
    # add user information before save
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.custom_user_object = self.request.user
        ret = super().form_valid(form)
        self.request.session['coupon_id'] = self.object.id
        return ret

class CouponImageCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    template_name = 'coupon/image_create.html'

    def test_func(self) -> bool | None:
        self.request.session['coupon_id'] = 1
        if not self.request.session.get('coupon_id', False):
            return False
        return True

    def handle_no_permission(self) -> HttpResponseRedirect:
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()

        return redirect('coupon:create')

    def get_object(self, queryset=None):
        coupon_id = self.request.session.get('coupon_id')
        print(coupon_id)
        coupon_object = models.Coupons.objects.get(pk=coupon_id)
        return coupon_object

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        imgs = request.FILES.getlist('images')
        coupon_id = self.request.session.get('coupon_id')
        coupon_object = models.Coupons.objects.get(pk=coupon_id)
        for img in imgs:
            ins = forms.CouponImageCreateForm({'coupon_object':coupon_object}, {'image':img})
            if ins.is_valid():
                ins.save(commit=True)
        
        del self.request.session['coupon_id']
        return redirect(reverse('coupon:detail', args=[coupon_id]))

class CouponListView(generic.ListView):
    model = models.Coupons
    template_name = 'coupon/list.html'

class CouponDetailView(generic.DetailView):
    model = models.Coupons
    template_name = 'coupon/detail.html'
    context_object_name = 'coupon'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['images'] =  models.CouponImages.objects.filter(coupon_object=self.object)

        # get fields label name
        field_labels = {}
        for field in self.model._meta.fields:
            field_labels[field.name] = field.verbose_name.capitalize()
        
        # insert data
        context['labels'] = field_labels

        return context