# TESTES UNITÁRIOS COM PYTHON E DJANGO FRAMEWORK

### Comandos Utilizados:
 python -m venv venv
 .venv/Scripts/acivate / .venv/bin/acivate (PARA LINUX)

 pip install Django

 django-admin startproject core .
 
 python manage.py startapp myapp

 -- Incluir a app criada em INSTALLED APPS (core/settings.py)

 python manage.py migrate

  -- Criar a model 'Livro'

 python manage.py makemigrations myapp

 python manage.py migrate (novamente)

 -- Adicionar a model no admin.py

 python manage.py createsuperuser

 -- Login: Admin

 -- Senha: 123456

 python manage.py runserver

 -- Acessar: http://127.0.0.1:8000/admin
 
 -- Inserir o Login e Senha

 -- Em tests.py escrever os testes unitários

 python manage.py test myapp (Para rodar os testes)

 ## Explicando os Testes Unitários criados

 1. Testa a Criação do Livro (test_criacao_livro)
Este teste verifica se o objeto Livro foi criado corretamente com os atributos esperados.

    Objetivo: Confirmar que os dados do livro (titulo, autor, data_publicacao) são corretamente armazenados no banco de dados.

    Explicação: Este teste cria um objeto Livro no método setUp. Ele então verifica se os atributos titulo, autor e data_publicacao do objeto Livro correspondem aos valores esperados.

    O método setUp é chamado antes de cada método de teste ser executado. Ele é usado para preparar o cenário necessário para os testes. Isso pode incluir a criação de objetos no banco de dados, a configuração de variáveis de instância, ou qualquer outra preparação necessária para que os testes possam ser executados corretamente.

2. Testa o Método __str__ do Modelo (test_metodo_str)
Este teste verifica se o método __str__ do modelo Livro retorna o valor correto.

    Objetivo: Garantir que a representação em string do objeto Livro é o valor do atributo titulo.

    Explicação: Este teste verifica se o método __str__ do objeto Livro retorna corretamente o título do livro.

3. Testa a Atualização de um Livro (test_atualizacao_livro)
Este teste verifica se um objeto Livro pode ser atualizado corretamente.

    Objetivo: Confirmar que os dados de um livro podem ser atualizados no banco de dados.

    Explicação: Este teste altera o título do livro e salva a alteração no banco de dados. Ele então verifica se a atualização foi feita corretamente.

4. Testa a Exclusão de um Livro (test_exclusao_livro)
Este teste verifica se um objeto Livro pode ser excluído corretamente.

    Objetivo: Garantir que um livro pode ser deletado do banco de dados e que ele não pode ser recuperado após a exclusão.

    Explicação: Este teste exclui o objeto Livro e verifica se ele não pode mais ser encontrado no banco de dados.

5. Testa a Contagem de Livros no Banco de Dados (test_contagem_livros)
Este teste verifica se a contagem de objetos Livro no banco de dados está correta.

    Objetivo: Confirmar que a contagem de livros no banco de dados reflete corretamente o número de objetos Livro armazenados.

    Explicação: Este teste inicialmente verifica se há um livro no banco de dados. Em seguida, ele cria um novo livro e verifica se a contagem de livros foi incrementada corretamente.
