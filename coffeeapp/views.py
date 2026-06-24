from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Coffee
from .forms import CoffeeForm

class IndexView(generic.ListView):
    template_name = "coffeeapp/index.html"
    context_object_name = "coffee_list"

    def get_queryset(self):
        return Coffee.objects.order_by("-roast_date")[:5]

# def index(request):
#     coffee_list = Coffee.objects.order_by("-roast_date")[:5]
#     context = {"coffee_list": coffee_list}
#     return render(request, "coffeeapp/index.html", context)

class CoffeeDetailView(generic.DetailView):
    model = Coffee
    template_name = "coffeeapp/coffee_detail.html"

# def coffee_detail(request, coffee_id):
#     coffee = get_object_or_404(Coffee, pk=coffee_id)
#     context = {"coffee": coffee}
#     return render(request, "coffeeapp/coffee_detail.html", context)

def new_coffee(request):

    if request.method == "POST":
        form = CoffeeForm(request.POST)

        if form.is_valid():

            form.save()
            
            return HttpResponseRedirect("/coffee/")
        
    else:
        form = CoffeeForm()

    return render(request, "coffeeapp/new_coffee.html", {"form": form})
