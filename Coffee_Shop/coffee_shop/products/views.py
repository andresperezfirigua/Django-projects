from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product


class ListProductsView(TemplateView):
    template_name = "products/products_list.html"

    def get_context_data(self):
        return {"products_list": Product.objects.all().order_by("name")}
