from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, FormView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from .forms import InventoryForm
from .models import Inventory

class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "inventory_delete.html"
    model = Inventory
    success_url = reverse_lazy('inventory_browse:home')

class InventoryCreateView(LoginRequiredMixin, CreateView):
    template_name = "inventory_create.html"
    form_class = InventoryForm
    # success_url = reverse_lazy('inventory_register:create_success')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

# class InventoryCreateSuccessView(LoginRequiredMixin, TemplateView):
#     template_name = 'inventory_create_success.html'

class InventoryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'inventory_detail.html'
    model = Inventory


class InventoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'inventory_update.html'
    model = Inventory
    form_class = InventoryForm

'''
https://daeudaeu.com/django-detailview/#DetailView
https://daeudaeu.com/django-updateview/#UpdateView-8
'''