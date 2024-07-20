from django.shortcuts import render
from first_app.models import Car

# Create your views here.
def my_view(request):
    cars_list = Car.objects.all()

    context = {
        'car_list' : cars_list
    }
    return render(request, "first_app/car_list.html", context)