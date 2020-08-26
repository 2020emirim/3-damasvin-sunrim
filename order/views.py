from django.shortcuts import render


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from order.models import Order


class OrderListView(ListView):
    model = Order


class OrderCreateView(CreateView):
    model = Order
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('order:list')

class OrderUpdateView(UpdateView):
    model = Order
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('order:list')

def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('order:list')