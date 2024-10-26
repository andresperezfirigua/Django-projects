from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from .models import Product
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = "products/products_list.html"
    context_object_name = 'products'


class AddProductFormView(FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('list_products')
    
    
    def form_valid(self, form) -> HttpResponse:
        form.save()
        return super().form_valid(form)