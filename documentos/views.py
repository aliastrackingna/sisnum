from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import TipoDocumento
from .forms import TipoDocumentoForm

@login_required(login_url='login')
def index(request):
    tipos = TipoDocumento.objects.all().order_by('nome')
    form = TipoDocumentoForm()
    
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de documento cadastrado com sucesso!')
            return redirect('index')
    
    context = {
        'tipos': tipos,
        'form': form,
    }
    return render(request, 'documentos/index.html', context)

@login_required(login_url='login')
def incrementar(request, tipo_id):
    tipo = get_object_or_404(TipoDocumento, pk=tipo_id)
    tipo.ultimo_numero += 1
    tipo.save()
    messages.success(request, f'Número do {tipo.nome} incrementado para {tipo.ultimo_numero}')
    return redirect('index')

@login_required(login_url='login')
def zerar_todos(request):
    if request.method == 'POST':
        TipoDocumento.objects.all().update(ultimo_numero=0)
        messages.warning(request, 'Todas as numerações foram zeradas!')
    return redirect('index')

@login_required(login_url='login')
def excluir_tipo(request, tipo_id):
    tipo = get_object_or_404(TipoDocumento, pk=tipo_id)
    nome = tipo.nome
    tipo.delete()
    messages.success(request, f'Tipo de documento "{nome}" excluído!')
    return redirect('index')

@login_required(login_url='login')
def editar_numero(request, tipo_id):
    tipo = get_object_or_404(TipoDocumento, pk=tipo_id)
    if request.method == 'POST':
        novo_numero = request.POST.get('ultimo_numero')
        try:
            tipo.ultimo_numero = int(novo_numero)
            tipo.save()
            messages.success(request, f'Número do {tipo.nome} atualizado para {tipo.ultimo_numero}')
        except ValueError:
            messages.error(request, 'Valor inválido!')
    return redirect('index')