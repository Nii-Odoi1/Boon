from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from requests import request
from .models import Route
from .forms import RouterForm
from django.views.generic import ListView

# Create your views here.
def home(request):
    BASE_URL = request.get_raw_uri()
    # return HttpResponse('Site is working')
    form = RouterForm(request.POST or None)
    if form.is_valid():
        form.save()
        key = form.cleaned_data.get('key')
        messages.success(request, f"URL has been successfully shortened to {BASE_URL}{key}")
        return redirect('home')
    return render(request, 'router/home.html', {"form": form})

def how_to(request):
    # return HttpResponse("<h1>About Page</h1>")
    return render(request, 'router/how_to_use.html')

def landing(request):
    # return HttpResponse("<h1>About Page</h1>")
    return render(request, 'router/landing.html')

class URLListView(ListView):
    model = Route
    context_object_name = 'urls'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super(URLListView, self).get_context_data(*args, **kwargs)
        uri = str(self.request.build_absolute_uri()).split(self.request.path)[0]
        context['base_uri'] = uri
        return context

def redirector(request, key):

    instance = get_object_or_404(Route, key= key)
    return redirect(instance.original_url)