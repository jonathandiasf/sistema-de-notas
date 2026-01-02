# Sistema de Notas 

Este é um aplicativo Django para gerenciar notas de alunos da Turma A.

## Funcionalidades

- Página inicial com acesso à lista de alunos
- Adicionar, visualizar e gerenciar alunos com notas
- Cálculo automático de médias e status (aprovado/reprovado)
- Destaque para os top 2 alunos
- Busca, ordenação e filtragem na lista

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/jonathandiasf/sistema-de-notas.git
   cd sistema-notas-escola
   ```

2. Crie um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Execute as migrações:
   ```
   python manage.py migrate
   ```

5. Inicie o servidor:
   ```
   python manage.py runserver
   ```

## Estrutura do Projeto

- `escola_alunos_app/`: Configurações principais do Django
- `alunos/`: App principal com modelos, views e templates
- `static/alunos/`: Arquivos CSS e estáticos
- `templates/alunos/`: Templates HTML

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
