from django.shortcuts import render, redirect
from .models import Aluno


def home(request):
    return render(request, 'alunos/home.html')


def lista_alunos(request):
    # Handle form submission to create a new Aluno
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        try:
            nota1 = float(request.POST.get('nota1', '0') or 0)
            nota2 = float(request.POST.get('nota2', '0') or 0)
            nota3 = float(request.POST.get('nota3', '0') or 0)
        except ValueError:
            # Invalid input: ignore and redirect back
            return redirect('lista_alunos')

        if nome:
            Aluno.objects.create(nome=nome, nota1=nota1, nota2=nota2, nota3=nota3)
        return redirect('lista_alunos')

    alunos = Aluno.objects.all()
    # compute approved / failed lists
    aprovados = [a for a in alunos if a.media >= 7]
    reprovados = [a for a in alunos if a.media < 7]

    # determine top two students by media
    sorted_by_media = sorted(alunos, key=lambda a: a.media, reverse=True)
    first_pk = sorted_by_media[0].pk if len(sorted_by_media) >= 1 else None
    second_pk = sorted_by_media[1].pk if len(sorted_by_media) >= 2 else None

    contexto = {
        'alunos': alunos,
        'aprovados': aprovados,
        'reprovados': reprovados,
        'first_pk': first_pk,
        'second_pk': second_pk,
    }
    return render(request, 'alunos/lista.html', contexto)
