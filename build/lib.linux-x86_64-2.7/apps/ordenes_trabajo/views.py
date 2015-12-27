from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.http import JsonResponse
from datatableview.views import DatatableView, XEditableDatatableView
from datatableview import helpers


class RegisterView(SuccessMessageMixin, FormView):
    success_url = '/ordenes_trabajo/registro/'
    form_class = Ordenes_TrabajoForm
    template_name = 'registro_orden.html'

    def get_form(self, form_class=None):
        f = super(RegisterView, self).get_form(form_class)
        #print self.get_form_kwargs()
        f.set_jefe_taller(self.request.user.username)
        return f

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 
            "Se ha registrado exitosamente la orden de trabajo " )
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 
            "No se pudo registrar la orden de trabajo" )
        return super(RegisterView, self).form_invalid(form)

class AutorizarRepuestoView(SuccessMessageMixin, FormView):
    success_url = '/ordenes_trabajo/repuesto/'
    form_class = Orden_RepuestoForm
    template_name = 'orden_repuesto.html'


    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 
            "Se ha registrado el repuesto a la orden de trabajo " )
        return super(AutorizarRepuestoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 
            "No se pudo autorizar el respuesto de la orden de trabajo" )
        return super(AutorizarRepuestoView, self).form_invalid(form)


class OrderDataTableView(XEditableDatatableView):
    model = Ordenes_Trabajo
    template_name = 'orders_list.html'
    datatable_options = {
        'columns': [
            #("Hora", 'timestamp', helpers.make_xeditable),
            #("Mecanico", 'mecanico_asignado', helpers.make_xeditable),
            ("Descripcion", 'descripcion', helpers.make_xeditable),
            #("Matricula", 'matricula_vehiculo', helpers.make_xeditable),
            ("Costo", "costo", helpers.make_xeditable),
            ("Estado", "estado", helpers.make_xeditable),
           ]
        }

    def get_queryset(self):
        self.queryset = Ordenes_Trabajo.objects.filter(jefe_taller=self.request.user.id_document)
        #print "queryset 1", self.queryset
        queryset = super(OrderDataTableView, self).get_queryset()
        #print "queryset 2 ", queryset
        return queryset