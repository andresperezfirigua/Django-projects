from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .models import Product
from .forms import ProductForm


class ListProductsView(generic.TemplateView):
    template_name = "products/products_list.html"

    def get_context_data(self):
        return {"products_list": Product.objects.all().order_by("name")}


class AddProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('list_products')
    
    def form_valid(self, form) -> HttpResponse:
        form.save()
        return super().form_valid(form)