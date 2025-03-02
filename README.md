# Projeto Rick and Morty API e Interface Web

Este projeto Django implementa um CRUD completo para personagens e localizações da série Rick and Morty, consumindo dados da [Rick and Morty API](https://rickandmortyapi.com/documentation) e oferecendo uma interface web interativa.

## Desafio Cumprido

Este projeto foi desenvolvido para cumprir os requisitos de um desafio de projeto Django, que incluía:

-   Implementação de um CRUD completo com duas ou mais entidades relacionadas (personagens e localizações).
-   Consumo de uma API externa gratuita (Rick and Morty API).
-   Utilização de `.gitignore`, `requirements.txt`, `README.md` e `Dockerfile`.

## Funcionalidades

### Gerenciamento de Dados

-   **Consumo da API Externa:** Busca e armazena dados de personagens e localizações da Rick and Morty API no banco de dados local.
-   **CRUD Completo:** Permite criar, ler, atualizar e deletar personagens e localizações através de uma interface web.
-   **Gerenciamento de Personagens:** Lista, cria, edita e exclui personagens com facilidade.
-   **Gerenciamento de Localizações:** Lista, cria, edita e exclui localizações com facilidade.

### Interface Web

-   **Interface Web Amigável:** Utiliza Django Templates e Bootstrap para uma experiência de usuário agradável.
-   **Páginas Informativas:** Contém páginas Home, Sobre e Index, fornecendo informações sobre o projeto e os personagens.

### Implantação

-   **Integração com Docker:** Facilita a implantação e execução do projeto em containers.
-   **Integração com Docker-Compose:** Facilita a configuração do banco de dados Postgres e a execução do projeto em containers.

## Pré-requisitos

-   Python 3.12 ou superior
-   Pip (gerenciador de pacotes do Python)
-   Docker e Docker Compose (opcional, para execução em container)
-   Postgres

## Configuração

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/IgorBrito02/wsBackend-Fabrica25.1.git
    cd wsBackend-Fabrica25.1
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**

    -   No Windows:

        ```bash
        venv\Scripts\activate
        ```

    -   No macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure o banco de dados:**
    * Crie um banco de dados PostgreSQL.
    * Edite `rickandmortyapi/settings.py` e configure a seção `DATABASES` com suas credenciais.
    * Execute as migrações:

    ```bash
    python manage.py migrate
    ```

6.  **Execute o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

    O servidor estará disponível em `http://127.0.0.1:8000/`.

### Usando Docker-Compose (Recomendado)

1.  **Execute o Docker Compose:**

    ```bash
    docker-compose up --build
    ```

    A API estará disponível em `http://localhost:8000/`.

## Uso

### URLs Disponíveis

-   `/fetch-characters/`: Busca personagens e localizações da API Rick and Morty e os salva no banco de dados.
-   `/characters/`: Lista todos os personagens salvos no banco de dados.
-   `/characters/create/`: Permite criar um novo personagem.
-   `/characters/update/<id>/`: Permite atualizar um personagem existente (substitua `<id>` pelo ID do personagem).
-   `/characters/delete/<id>/`: Permite deletar um personagem existente (substitua `<id>` pelo ID do personagem).
-   `/locations/`: Lista todas as localizações salvas no banco de dados.
-   `/locations/create/`: Permite criar uma nova localização.
-   `/locations/update/<id>/`: Permite atualizar uma localização existente (substitua `<id>` pelo ID da localização).
-   `/locations/delete/<id>/`: Permite deletar uma localização existente (substitua `<id>` pelo ID da localização).
-   `/admin/`: Acesso à interface de administração do Django.
-   `/`: Acesso a página inicial do projeto.
-   `/index/`: Acesso a página inicial do projeto.
-   `/about/`: Acesso a página Sobre do projeto.
-   `/home/`: Acesso a página Home do projeto.

### Interface Web

-   **Listar Personagens:** Acesse `http://localhost:8000/characters/` para visualizar todos os personagens.
-   **Criar Personagem:** Acesse `http://localhost:8000/characters/create/` para adicionar um novo personagem.
-   **Editar Personagem:** Acesse `http://localhost:8000/characters/update/<id>/` para editar um personagem existente.
-   **Excluir Personagem:** Acesse `http://localhost:8000/characters/delete/<id>/` para excluir um personagem.
-   **Listar Localizações:** Acesse `http://localhost:8000/locations/` para visualizar todas as localizações.
-   **Criar Localização:** Acesse `http://localhost:8000/locations/create/` para adicionar uma nova localização.
-   **Editar Localização:** Acesse `http://localhost:8000/locations/update/<id>/` para editar uma localização existente.
-   **Excluir Localização:** Acesse `http://localhost:8000/locations/delete/<id>/` para excluir uma localização.

## Estrutura do Projeto

wsBackend-Fabrica25.1/
├── characters/
│   ├── pycache/
│   ├── migrations/
│   ├── templates/characters/
│   │   ├── about.html
│   │   ├── home.html
│   │   ├── index.html
│   │   ├── characters_confirm_delete.html
│   │   ├── characters_form.html
│   │   └── characters_list.html
│   ├── static/
│   │   └── bootstrap/
│   │       ├── css/
│   │       │   └── bootstrap.min.css
│   │       └── js/
│   │           └── bootstrap.bundle.min.js
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── rickandmortyapi/
│   ├── pycache/
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/
├── db.sqlite3
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── manage.py


## Dependências

-   Django
-   Requests
-   django-bootstrap5
-   psycopg2-binary

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. Para relatar bugs ou solicitar novos recursos, por favor, abra uma issue no repositório.

## Agradecimentos

Agradecemos à [Rick and Morty API](https://rickandmortyapi.com/documentation) por fornecer os dados utilizados neste projeto. Também agradecemos às comunidades de Django, Python e Bootstrap por suas excelentes bibliotecas e documentação.