from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm

class home_view(TemplateView):
    template_name = 'invApp/home.html'

class product_list_view(ListView):
    model = Product
    template_name = 'invApp/product_list.html'
    context_object_name = 'products'

class product_create_view(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'invApp/product_form.html'
    success_url = reverse_lazy('product_list')

class product_update_view(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'invApp/product_form.html'
    success_url = reverse_lazy('product_list')
    pk_url_kwarg = 'product_id'

class product_delete_view(DeleteView):
    model = Product
    template_name = 'invApp/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
    pk_url_kwarg = 'product_id'
