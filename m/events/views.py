from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.base import View
from events.models import Category
from django.views.generic.edit import CreateView
from events.models import MyClubUser


def index(request):
    return render(request, 'main.html')


class Login(TemplateView):
    template_name = "login.html"


class Main(TemplateView):
    template_name = "main.html"

    def index(request):
        return render(request, 'main.html', {})


class Sign(CreateView):
    model = MyClubUser
    fields = ['name', 'phone', 'email', 'password1', 'password2']
    success_url = reverse_lazy('main')


class Cater(TemplateView):
    template_name = "cater.html"


class Food(TemplateView):
    template_name = "food.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class Order(View):
    def post(request, *args, **kwargs):
        return redirect('login')
