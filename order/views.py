from django.shortcuts import render


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from menu.models import Drink
from order.models import Order


class OrderListView(ListView):
    model = Order

def get_context_data(self, *, object_list=None, **kwargs):
    context = super().get_context_data(**kwargs)
    context['menu_list'] = Drink.objects.all()
    return context

class OrderCreateView(CreateView):
    model = Order
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('order:list')

def get_initial(self):
    initial = super().get_initial()
    initial['drink'] = self.kwargs.get('menu_id')
    return initial

class OrderUpdateView(UpdateView):
    model = Order
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('order:list')

def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('order:list')