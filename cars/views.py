from cars.models import car
from cars.form import CarModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView




class CarListView(ListView):
    model = car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class CarDetailView(DetailView):
    model = car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
     model = car
     form_class = CarModelForm
     template_name = 'new_car.html'
     success_url = '/cars/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = car
    form_class = CarModelForm
    template_name = 'car_update.html'
    seccess_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = car
    template_name = 'car_delete.html'
    success_url = '/cars/'
