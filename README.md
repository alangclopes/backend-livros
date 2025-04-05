# 📚 Desafio Django com DRF e Docker

Este projeto foi desenvolvido como parte de um desafio técnico, com o objetivo de criar uma API RESTful para gerenciamento de autores e livros, utilizando Django REST Framework e Docker.

---

## 🚀 Tecnologias Utilizadas

- Python 3.11
- Django 4+
- Django REST Framework
- PostgreSQL (via Docker)
- Docker & Docker Compose

---

## ⚙️ Funcionalidades Implementadas

### 🔧 Funcionalidades básicas
- [x] Cadastro de autores
- [x] Cadastro de livros
- [x] Relacionamento de 1 autor para N livros
- [x] Endpoints criados manualmente com `@api_view`

### 🔎 Funcionalidade extra
- [x] **Busca de livros em tempo real** (`GET /api/livros/?search=palavra`)

### 🏆 Diferenciais implementados
- [x] **Endpoint de top autores com mais livros**
  - `GET /api/autores/top/`
  - Retorna os 5 autores com mais livros cadastrados
- [x] **Notificação ao cadastrar autor**
  - Ao criar um novo autor, é disparado um `print` simulando uma notificação no backend.

---

