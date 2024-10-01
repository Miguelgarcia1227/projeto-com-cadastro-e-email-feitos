from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AgendamentoForm


def agendamento(request):
    agendamento = Agendamento.objects.all()
    return render(request, 'agendamento/novo_agendamento.html', {'agendamento': agendamento})

def novo_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamento')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento/agendamento_form.html', {'form': form})

def agendamento_update(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('agendamento')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'agendamento/agendamento_form.html', {'form': form})

def agendamento_delete(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('agendamento')
    return render(request, 'agendamento/agendamento_confirm_delete.html', {'agendamento': agendamento})

    
