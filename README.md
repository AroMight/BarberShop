<p align="center">
  <img src="https://github.com/wsvincent/awesome-django/raw/main/assets/django-logo-negative.svg" />
</p>


## Configuração do Projeto

Para configurar este projeto em seu ambiente local, siga estas etapas:

1. Clone o repositório para sua máquina local usando `git clone`.
2. Instale as dependências do projeto com `pip install -r requirements.txt`.
3. Configure o banco de dados executando `python manage.py migrate`.
4. Crie um arquivo .env e configure as variáveis de ambiente necessárias. O projeto possui um arquivo .env-example para lhe ajudar.
5. Inicie o servidor de desenvolvimento com `python manage.py runserver`.

## Melhorias

Uma lista de melhorias e revisões que pretendo fazer. A medida que for descobrindo as respostas de cada ponto, irei atualizando.

1. Com certeza deve haver uma forma mais apropriada de integrar as messages do que com a solução encontrada;
2. Reorganizar os arquivos `static` que estão dentro da pasta principal do projeto;
3. Existe uma forma melhor de criar novos "customers" usando o form de registro do que sobscrevendo o método `save()` do form?
  <br> Sim, signals. A princípio o pre_save parece ser uma boa forma de realizar isso. Irei testar.
  <br> Testei. A principio achei a solução original mais adequada, porém com o aprendizado sobre os signals
  <br> consegui setar signals para que o "User" associado ao modelo "Customer" ou "Employee" seja excluido
  <br> quando um "Customer" ou "Employee" for excluido. Muito útil!
  <br> ✅ Concluido
4. Reorganizar o arquivo `admin.py` do app "users";
5. O django-debug-toolbar não está funcionando. Fix it!
  <br>✅ Concluido:  O problema estava na configuração do INTERNAL_IP
6. O `allowed_host` precisa ir para o arquivo `.env`;
  <br>✅ Concluido
07. O design do forms está horrível. Consertar;
08. Entender melhor a forma mais adequada de lidar com assets;
09. Extrair modelos dos cards de "services" e "staff" para arquivos .html;
  <br>✅ Concluido: Feito, porém percebi que como o design da home depende dos "services", "staffs" e "branches" cadastradas, talvez não seja uma boa idéia fazer dessa maneira.
10. Desenvolver a API com Django Rest Framework;
11. Configurar o método `delete()` do models Customers e Staff para excluir também o "user" correspondente;

## Contribuindo

Contribuições são bem-vindas!

## Licença

Este projeto está licenciado sob a licença MIT.
