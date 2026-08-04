from urllib import request

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .models import Jogo
from .forms import CriarUsuarioForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Jogo, Locacao

def lista_jogos(request):  
    jogos = Jogo.objects.all()
    return render(request, 'core/lista_jogos.html', {'jogos': jogos})

def cadastro(request):
  if request.method == 'POST':
    form = CriarUsuarioForm(request.POST)
    if form.is_valid():
      novo_usuario = form.save()
      auth_login(request, novo_usuario)
      username = form.cleaned_data.get('username')
      messages.success(request, f'Olá {username}, sua conta foi criada com sucesso')
      return redirect ('home')

  else:
      form = CriarUsuarioForm()

  return render (request, 'core/cadastro.html', {'form': form})

    
@login_required
def alugar_jogo(request, jogo_id):
   jogo = get_object_or_404(Jogo, id=jogo_id)

   if jogo.alugado:
    messages.error(request, 'este jogo está alugado no momento..')
    return redirect ('home')

   if request.method == 'POST':
      dias_informados = int(request.POST.get('dias', 1))

      Locacao.objects.create(
      cliente = request.user,
      jogo = jogo,
      dias = dias_informados 
      )

      jogo.alugado= True
      jogo.save()

      messages.success(request, f'você alugou {jogo.titulo} por {dias_informados} dias com sucesso')
      return redirect ('home')

   return render(request, 'core/alugar_jogo.html', {'jogo': jogo})



@login_required
def devolver_jogo(request, locacao_id):
    
    if request.method == 'POST':
        
        locacao = get_object_or_404(Locacao, id=locacao_id, cliente=request.user)

        
        locacao.devolvido = True
        locacao.save()

        
        jogo = locacao.jogo
        jogo.alugado = False
        jogo.save()

        messages.success(request, f'O jogo "{jogo.titulo}" foi devolvido com sucesso e já está disponível na loja!')

   
    return redirect('meus_jogos')


@login_required
def meus_jogos(request):
    locacoes_ativas = Locacao.objects.filter(cliente=request.user, devolvido=False)
    return render(request, 'core/meus_jogos.html', {'locacoes': locacoes_ativas})