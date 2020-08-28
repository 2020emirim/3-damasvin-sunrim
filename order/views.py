from django.shortcuts import render

from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from menu.models import Drink
from order.forms import OrderModelForm
from order.models import Order


class OrderListView(ListView):
    model = Order

def get_context_data(self, *, object_list=None, **kwargs):
    context = super().get_context_data(**kwargs)
    context['menu_list'] = Drink.objects.all()
    context['total_price'] = Order.objects.all().aggregate(total_price=Sum('price')).get('total_price', 0)
    return context

class OrderCreateView(CreateView):
    model = Order
    # fields = '__all__'
    form_class = OrderModelForm
    template_name_suffix = '_create'
    success_url = reverse_lazy('order:list')

def get_initial(self):
    initial = super().get_initial()
    initial['drink'] = self.kwargs.get('menu_id')
    initial['price'] = Drink.objects.get(id=self.kwargs.get('menu_id')).price
    return initial

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['drink_price'] = Drink.objects.get(id=self.kwargs['menu_id']).price
    return context

class OrderUpdateView(UpdateView):
    model = Order
    # fields = '__all__'
    form_class = OrderModelForm
    template_name_suffix = '_update'
    success_url = reverse_lazy('order:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['drink_price'] = Order.objects.get(id=self.kwargs['pk']).drink.price
        return context


def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('order:list')

class OrderResultView(ListView):
    model = Order
    template_name_suffix = '_result'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_price'] = Order.objects.all().aggregate(total_price=Sum('price')).get('total_price', 0)
        return context

def pay(request):
    orders = Order.objects.all()
    orders.delete()
    return redirect('order:list')