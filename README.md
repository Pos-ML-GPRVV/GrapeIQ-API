# API de Extração de Dados de Comercialização de Uvas

Este projeto consiste em uma API REST desenvolvida em Python/Flask para coletar, processar e disponibilizar dados sobre a comercialização de uvas no Brasil. A aplicação realiza web scraping diretamente do site da **Embrapa**, estruturando e armazenando os dados em um banco de dados PostgreSQL hospedado na plataforma **Neon**.

---

## 🗂️ Estrutura do Projeto

```
Grapi/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   ├── crud_routes.py
│   │   └── scrape_routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── scraping_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── auth.py
│   └── config.py
├── requirements.txt
├── Dockerfile
├── README.md
└── run.py
```

- **app/**: Diretório principal do aplicativo.
  - **routes/**: Contém as rotas organizadas por funcionalidades.
  - **services/**: Serviços para lógica de negócios, como scraping.
  - **utils/**: Utilitários, como autenticação.
  - **config.py**: Configurações da aplicação Flask.
- **run.py**: Ponto de entrada para iniciar o aplicativo.
- **requirements.txt**: Lista de dependências do projeto.
- **Dockerfile**: Configurações para Docker.
- **README.md**: Documentação do projeto.

---

## 🚀 Funcionalidades

- Web scraping automatizado dos dados de comercialização de uvas do site da Embrapa
- API RESTful com documentação interativa via Swagger
- Autenticação básica HTTP
- Cache de dados para otimização de performance
- Persistência dos dados em banco PostgreSQL (Neon)
- Processamento e estruturação dos dados para consumo

---

## 📋 Pré-requisitos

- Python 3.8+
- Conta no Neon (PostgreSQL gerenciado na nuvem)
- pip (gerenciador de pacotes Python)

---

## 🔧 Instalação

Clone o repositório:
```sh
git clone [https://github.com/Pos-ML-GPRVV/Grapi.git]
cd [https://github.com/Pos-ML-GPRVV/Grapi.git]
```

Crie e ative um ambiente virtual:
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate   # Windows
```

Instale as dependências:
```sh
pip install -r requirements.txt
```

Configure as variáveis de ambiente:

Copie o arquivo `.env.example` para `.env` e ajuste os valores conforme necessário:
```env
DB_HOST='ep-empty-thunder-ac035frq-pooler.sa-east-1.aws.neon.tech'
DB_NAME='neondb'
DB_USER='neondb_owner'
DB_PASSWORD='npg_p3vyrFiK0blB'
```
> Utilize as credenciais fornecidas pelo Neon para conectar ao banco de dados.

---

## 🚀 Executando a aplicação

Ative o ambiente virtual (se ainda não estiver ativo).

Execute a aplicação:
```sh
python app/app.py
```

A API estará disponível em [http://localhost:5432](http://localhost:5432)

---

## 📚 Documentação da API

A documentação completa da API está disponível via Swagger UI em:  
[http://localhost:5432/apidocs/](http://localhost:5432/apidocs/)

### Endpoints principais

- `GET /extractor?year={ano}`: Retorna dados brutos do web scraping realizado no site da Embrapa
- `GET /download?year={ano}`: Retorna dados estruturados em formato CSV compactado (.zip)

---

## 🛠️ Tecnologias Utilizadas

- Flask - Framework web
- Beautiful Soup 4 - Web scraping
- Flasgger - Documentação Swagger
- PostgreSQL (Neon) - Banco de dados na nuvem
- Flask-HTTPAuth - Autenticação
- Pandas - Processamento de dados
- Requests - Requisições HTTP

---

## 👥 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona NovaFeature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença [INSERIR TIPO DE LICENÇA] - veja o arquivo LICENSE.md para detalhes.