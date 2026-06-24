from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import F

from .models import Coffee, Roaster
from .forms import CoffeeForm

class IndexView(generic.ListView):
    template_name = "coffeeapp/index.html"
    context_object_name = "coffee_list"

    def get_queryset(self):
        return Coffee.objects.order_by("-roast_date")[:5]

class CoffeeDetailView(generic.DetailView):
    model = Coffee
    template_name = "coffeeapp/coffee_detail.html"

class RoasterDetailView(generic.DetailView):
    model = Roaster
    template_name = "coffeeapp/roaster_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coffee_list"] = Coffee.objects.filter(roaster__pk=self.kwargs["pk"])
        return context

def new_coffee(request):

    if request.method == "POST":
        form = CoffeeForm(request.POST)

        if form.is_valid():

            form.save()
            
            return HttpResponseRedirect("/coffee/")
        
    else:
        form = CoffeeForm()

    return render(request, "coffeeapp/new_coffee.html", {"form": form})
