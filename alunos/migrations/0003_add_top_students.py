from django.db import migrations


def create_top_students(apps, schema_editor):
    Aluno = apps.get_model('alunos', 'Aluno')
    # Create two students with very high grades so they become the top two
    Aluno.objects.create(nome='Jonathan Dias', nota1=10.0, nota2=10.0, nota3=9.9)
    Aluno.objects.create(nome='Maria Karen Carvalho ', nota1=10.0, nota2=10.0, nota3=9.8)


def delete_top_students(apps, schema_editor):
    Aluno = apps.get_model('alunos', 'Aluno')
    Aluno.objects.filter(nome__in=['Jonathan Dias', 'Maria Karen Carvalho']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_populate_alunos'),
    ]

    # This migration was reverted (students removed). Make this migration a no-op
    # so it won't re-insert Jonathan and Maria Karen if applied accidentally.
    operations = []
