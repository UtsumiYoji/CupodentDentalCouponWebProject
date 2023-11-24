from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from . import models, forms

# Create your views here.
class CouponCreateView(generic.CreateView):
    model = models.Coupons
    form_class = forms.CouponCreateForm
    template_name = 'coupon/create.html'
    success_url = '/create/image'

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

class CouponImageCreateView(generic.CreateView):
    model = models.CouponImages
    template_name = 'coupon/image_create.html'
    success_url = '/'

    def get_form(self, form_class=None):
        coupon_id = self.request.session.get('coupon_id')
        coupon_object = models.Coupons.objects.get(pk=coupon_id)
        form = forms.coupon_image_forms(instance=coupon_object)

        return form

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