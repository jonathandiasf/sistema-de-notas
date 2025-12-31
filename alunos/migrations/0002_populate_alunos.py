from django.db import migrations


def create_alunos(apps, schema_editor):
    Aluno = apps.get_model('alunos', 'Aluno')
    alunos = [
        Aluno(nome='Jonathan Dias', nota1=10.0, nota2=10.0, nota3=9.9),
        Aluno(nome='Maria Karen Carvalho', nota1=10.0, nota2=10.0, nota3=9.8),
        Aluno(nome='Miguel Silva', nota1=9.8, nota2=9.5, nota3=9.7),
        Aluno(nome='Alice Santos', nota1=9.5, nota2=9.0, nota3=9.2),
        Aluno(nome='Lucas Oliveira', nota1=8.5, nota2=8.0, nota3=8.6),
        Aluno(nome='Sofia Pereira', nota1=8.2, nota2=7.8, nota3=8.0),
        Aluno(nome='Gabriel Costa', nota1=7.5, nota2=7.2, nota3=7.8),
        Aluno(nome='Mariana Rodrigues', nota1=7.0, nota2=7.5, nota3=7.1),
        Aluno(nome='Pedro Almeida', nota1=6.8, nota2=6.5, nota3=6.9),
        Aluno(nome='Laura Ferreira', nota1=6.4, nota2=6.2, nota3=6.0),
        Aluno(nome='Rafael Gomes', nota1=5.5, nota2=5.8, nota3=6.0),
        Aluno(nome='Beatriz Martins', nota1=7.9, nota2=8.1, nota3=8.0),
        Aluno(nome='João Araújo', nota1=7.6, nota2=7.4, nota3=7.7),
        Aluno(nome='Camila Ribeiro', nota1=7.3, nota2=7.0, nota3=7.5),
        Aluno(nome='Thiago Lima', nota1=4.5, nota2=5.0, nota3=4.8),
        Aluno(nome='Isabela Cardoso', nota1=9.2, nota2=9.0, nota3=9.3),
        Aluno(nome='Henrique Nunes', nota1=8.8, nota2=8.6, nota3=8.9),
    ]
    # Create all entries
    Aluno.objects.bulk_create(alunos)


def delete_alunos(apps, schema_editor):
    Aluno = apps.get_model('alunos', 'Aluno')
    nomes = [
        'Jonathan Dias', 'Maria Karen Carvalho', 'Miguel Silva', 'Alice Santos', 'Lucas Oliveira', 'Sofia Pereira',
        'Gabriel Costa', 'Mariana Rodrigues', 'Pedro Almeida', 'Laura Ferreira',
        'Rafael Gomes', 'Beatriz Martins', 'João Araújo', 'Camila Ribeiro',
        'Thiago Lima', 'Isabela Cardoso', 'Henrique Nunes'
    ]
    Aluno.objects.filter(nome__in=nomes).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_alunos, delete_alunos),
    ]
