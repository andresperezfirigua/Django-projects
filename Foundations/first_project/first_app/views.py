from django.shortcuts import render
from first_app.models import Car, Profile
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
def my_view(request):
    context = {
        'car_list': Car.objects.all().order_by('title')#.exclude(color=None)
    }
    return render(request, "first_app/car_list.html", context)

class CarListView(TemplateView):
    template_name = "first_app/car_list.html"
    
    def get_context_data(self):
        return {
            'car_list': Car.objects.all().order_by('title')#.exclude(color=None)
        }
    

def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

def show_profile(request, *args, **kwargs):
    context = {
        'profile': Profile.objects.filter(id=kwargs['author_id'])
    }
    return render(request, "first_app/user_profile.html", context)