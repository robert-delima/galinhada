# 🐔 Galinhada

## 📌 Sobre o projeto

O **Galinhada** é um sistema desenvolvido em Python para auxiliar na gestão de uma pequena produção de ovos de galinha.

A ideia surgiu a partir de uma necessidade real: um amigo que trabalha com produção de ovos precisava de uma ferramenta para registrar e acompanhar melhor os números da produção.

O projeto começou como uma aplicação simples executada pelo terminal e vem evoluindo conforme avanço nos meus estudos de desenvolvimento back-end.

Atualmente, o sistema utiliza **SQLite para persistência dos dados** e também possui uma **API REST desenvolvida com FastAPI**, permitindo consultar, cadastrar, editar e excluir registros da produção.

---

## ⚙️ Funcionalidades

### 🥚 Controle de produção

- Cadastro diário da produção
- Registro da quantidade de galinhas
- Registro da quantidade de ovos
- Registro do consumo de ração
- Consulta de todas as produções
- Consulta por ID
- Consulta por data
- Consulta por período
- Edição de registros
- Exclusão de registros

### 📊 Relatórios e cálculos

- Total de ovos produzidos
- Total de ração consumida
- Projeções de produção
- Cálculos diários, semanais e mensais

### 🌐 API REST

A API foi desenvolvida com **FastAPI** e utiliza o mesmo banco de dados SQLite da aplicação principal.

Endpoints disponíveis:

| Método | Endpoint | Função |
|---|---|---|
| GET | `/producoes` | Lista todas as produções |
| GET | `/producoes/{id}` | Consulta uma produção pelo ID |
| POST | `/producoes` | Cadastra uma nova produção |
| PATCH | `/producoes/{id}/ovos` | Atualiza a quantidade de ovos |
| PATCH | `/producoes/{id}/racao` | Atualiza a quantidade de ração |
| PATCH | `/producoes/{id}/galinhas` | Atualiza a quantidade de galinhas |
| PATCH | `/producoes/{id}/data` | Atualiza a data |
| DELETE | `/producoes/{id}` | Exclui uma produção |

A API também possui tratamento de registros inexistentes com retorno **404 Not Found** e validação dos dados recebidos utilizando **Pydantic**.

---

## 🗄️ Banco de dados

O projeto utiliza **SQLite** para armazenar os registros da produção.

A aplicação executada pelo terminal e a API utilizam o mesmo banco de dados, permitindo que informações cadastradas por uma interface possam ser consultadas pela outra.

---

## ▶️ Executando a API

Com as dependências instaladas, execute:

```bash
fastapi dev api.py
```

A documentação interativa da API estará disponível em:

```text
http://127.0.0.1:8000/docs
```

Por meio do Swagger UI é possível testar os endpoints diretamente pelo navegador.

---

## 🛠️ Tecnologias utilizadas

- Python
- FastAPI
- Pydantic
- SQLite
- Git
- GitHub

---

## 🚀 Próximas melhorias

O projeto continuará evoluindo conforme avanço nos estudos de desenvolvimento back-end.

Algumas melhorias planejadas:

- Cadastro de custos da produção
- Controle do preço de venda dos ovos
- Cálculo mais completo de custos e lucros
- Gráficos para acompanhamento da produção
- Melhorias na organização e arquitetura do código
- Interface mais amigável para utilização do sistema

---

## 📚 Status do projeto

🚧 **Em desenvolvimento**

O Galinhada começou como um projeto simples para praticar Python e atualmente está evoluindo para uma aplicação back-end com banco de dados e API REST.

O objetivo é continuar aplicando novos conhecimentos ao projeto enquanto resolvo necessidades reais da produção.