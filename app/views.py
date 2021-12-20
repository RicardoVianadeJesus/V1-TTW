from django.shortcuts import render, redirect
from app.forms import ComputadorForm
from app.models import Computador
from django.core.paginator import Paginator





# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Computador.objects.filter(origem__icontains=search)
    else:
        data['db'] = Computador.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ComputadorForm()
    return render(request, 'form.html', data)

def create(request):
    form = ComputadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Computador.objects.get(pk=pk)
    return render(request,'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Computador.objects.get(pk=pk)
    data['form'] = ComputadorForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Computador.objects.get(pk=pk)
    form = ComputadorForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Computador.objects.get(pk=pk)
    db.delete()
    return redirect('home')





