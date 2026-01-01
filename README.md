# Nesta estrutura:

- api/v1/endpoints/: Contém os arquivos de roteamento específicos para diferentes recursos como usuários, empresas e NPS.
- apps/: Contém a lógica de negócio e acesso a dados.
- auth/: Contém tudo relacionado à autenticação e autorização.
- core/: Configurações centrais do projeto.
- db/: Configuração de banco de dados e migrações.
- exceptions/: Exceções personalizadas.
- helpers/: Funções auxiliares.
- models/: Modelos de banco de dados ORM.
- schemas/: Esquemas Pydantic para validação de dados.
- services/: Lógica de negócio e serviços da aplicação.
- configs/: Arquivos de configuração para diferentes ambientes.
- tests/: Testes de unidade e integração.
- resources/: Templates de email e arquivos estáticos.
- Os arquivos na raiz do projeto são para configuração do ambiente de desenvolvimento e produção, instruções de como rodar o projeto, e o ponto de entrada da aplicação (main.py).

### No diretório celery_worker:

- tasks/: Contém as definições das tarefas que o Celery executará.
- celery_config.py: Contém as configurações do Celery, como o broker de mensagens e o backend de resultados.
- celery_app.py: Cria a aplicação do Celery e importa as tarefas.
- beat_schedule.py: (Opcional) Se estiver usando o Celery Beat, esse arquivo conteria o cronograma das tarefas periódicas.

```
your_project_name/
│
├── api/
│   ├── v1/
│   │   ├── endpoints/
│   │   │   ├── user_routes.py
│   │   │   ├── company_routes.py
│   │   │   ├── nps_routes.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   └── __init__.py
│
├── apps/
│   ├── auth/
│   │   ├── jwt_handler.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   └── __init__.py
│   ├── db/
│   │   ├── database.py
│   │   ├── migrations/
│   │   └── __init__.py
│   ├── exceptions/
│   │   └── custom_exceptions.py
│   ├── helpers/
│   │   ├── nps_calculator.py
│   │   └── __init__.py
│   ├── models/
│   │   ├── user_model.py
│   │   ├── company_model.py
│   │   ├── nps_model.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── company_schema.py
│   │   ├── nps_schema.py
│   │   └── __init__.py
│   └── services/
│       ├── user_service.py
│       ├── company_service.py
│       ├── nps_service.py
│       └── __init__.py
│
├── celery_worker/
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── email_tasks.py
│   │   └── nps_tasks.py
│   ├── celery_config.py
│   ├── celery_app.py
│   └── beat_schedule.py
│
├── configs/
│   ├── development.py
│   ├── production.py
│   ├── testing.py
│   └── __init__.py
│
├── tests/
│   ├── test_user.py
│   ├── test_company.py
│   ├── test_nps.py
│   └── __init__.py
│
├── resources/
│   ├── email_templates/
│   └── static_files/
│
├── .env
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
├── main.py
└── start.sh

```