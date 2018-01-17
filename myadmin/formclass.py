from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from filters.models import Filter
from .forms import *


class FilterCreate(TemplateView):
    form = None
    template_name = "Admin/add.html"

    def get(self, *args, **kwargs):
        self.form = FilterForm()
        return super(FilterCreate, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FilterCreate, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.form = FilterForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            # messages.add_message(request, messages.SUCCESS, "Актер успешно добавлен в таблицу")
            return redirect("admin_filter")
        else:
            return super(FilterCreate, self).get(request, *args, **kwargs)


class FilterEdit(TemplateView):
    form = None
    template_name = "Admin/edit.html"

    def get(self, *args, **kwargs):
        filter_obj = Filter.objects.get(pk=kwargs['id'])
        self.form = FilterForm(instance=filter_obj)
        return super(FilterEdit, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FilterEdit, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        obj = Filter.objects.get(pk=kwargs["id"])
        self.form = FilterForm(request.POST, instance=obj)
        if self.form.is_valid():
            self.form.save()
            return redirect("admin_filter")
        else:
            return super(FilterEdit, self).get(request, *args, **kwargs)


class FilterDelete(TemplateView):
    form = None
    template_name = "Admin/del.html"

    def get(self, *args, **kwargs):
        filter_obj = Filter.objects.get(pk=kwargs['id'])
        self.form = FilterForm(instance=filter_obj)
        return super(FilterDelete, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FilterDelete, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        obj = Filter.objects.get(pk=kwargs["id"])
        self.form = FilterForm(request.POST, instance=obj)
        if "yes" in request.POST:
            obj.delete()
            return redirect("admin_filter")
        else:
            return redirect("admin_filter")


class BrandCreate(TemplateView):
    form = None
    template_name = "Admin/add.html"

    def get(self, *args, **kwargs):
        self.form = BrandForm()
        return super(BrandCreate, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BrandCreate, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.form = BrandForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            # messages.add_message(request, messages.SUCCESS, "Актер успешно добавлен в таблицу")
            return redirect("admin_brand")
        else:
            return super(BrandCreate, self).get(request, *args, **kwargs)


class BrandEdit(TemplateView):
    form = None
    template_name = "Admin/edit.html"

    def get(self, *args, **kwargs):
        brand_obj = Brand.objects.get(pk=kwargs['id'])
        self.form = BrandForm(instance=brand_obj)
        return super(BrandEdit, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BrandEdit, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        obj = Brand.objects.get(pk=kwargs["id"])
        self.form = BrandForm(request.POST, instance=obj)
        if self.form.is_valid():
            self.form.save()
            return redirect("admin_brand")
        else:
            return super(BrandEdit, self).get(request, *args, **kwargs)


class CategoryCreate(TemplateView):
    form = None
    template_name = "Admin/add.html"

    def get(self, *args, **kwargs):
        self.form = CategoryForm()
        return super(CategoryCreate, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryCreate, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.form = CategoryForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            # messages.add_message(request, messages.SUCCESS, "Актер успешно добавлен в таблицу")
            return redirect("admin_cat")
        else:
            return super(CategoryCreate, self).get(request, *args, **kwargs)


class CategoryEdit(TemplateView):
    form = None
    template_name = "Admin/add.html"

    def get(self, *args, **kwargs):
        category_obj = Category.objects.get(pk=kwargs['id'])
        self.form = CategoryForm(instance=category_obj)
        return super(CategoryEdit, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryEdit, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        category_obj = Category.objects.get(pk=kwargs['id'])
        self.form = CategoryForm(request.POST, instance=category_obj)
        if self.form.is_valid():
            self.form.save()
            # messages.add_message(request, messages.SUCCESS, "Актер успешно добавлен в таблицу")
            return redirect("admin_cat")
        else:
            return super(CategoryEdit, self).get(request, *args, **kwargs)
        
class OrderCreate(TemplateView):
    form = None
    template_name = "Admin/add.html"

    def get(self, *args, **kwargs):
        self.form = OrderForm()
        return super(OrderCreate, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrderCreate, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.form = OrderForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            # messages.add_message(request, messages.SUCCESS, "Актер успешно добавлен в таблицу")
            return redirect("admin_order")
        else:
            return super(OrderCreate, self).get(request, *args, **kwargs)
        
class OrderEdit(TemplateView):
    form = None
    template_name = "Admin/add.html"

    def get(self, *args, **kwargs):
        order_obj = Order.objects.get(pk=kwargs['id'])
        self.form = OrderForm(instance=order_obj)
        return super(OrderEdit, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrderEdit, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        order_obj = Order.objects.get(pk=kwargs['id'])
        self.form = OrderForm(request.POST, instance=order_obj)
        if self.form.is_valid():
            self.form.save()
            # messages.add_message(request, messages.SUCCESS, "Актер успешно добавлен в таблицу")
            return redirect("admin_order")
        else:
            return super(OrderEdit, self).get(request, *args, **kwargs)
