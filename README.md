# 🎬 Onde Assistir

Este projeto é um **buscador de filmes**, que consulta a API do **The Movie Database (TMDb)** para descobrir **em quais plataformas de streaming um filme está disponível no Brasil**.

A principal ideia é **evitar requisições desnecessárias à API**, armazenando os resultados localmente no banco de dados MongoDB.

---

## O que esse projeto faz?

1. Recebe o **título de um filme** digitado pelo usuário
2. **Procura primeiro no banco de dados (MongoDB)**  
   - Se o filme já existir no banco, o resultado é retornado imediatamente (cache)
3. Caso o filme **não esteja salvo**:
   - Consulta a **API do TMDb**
   - Busca o filme pelo título
   - Obtém o ID do filme
   - Consulta os **provedores de streaming disponíveis no Brasil**
   - Salva o resultado no MongoDB
4. Exibe ao usuário:
   - Título do filme
   - Ano de lançamento
   - Plataformas onde está disponível para streaming

---

## Funcionamento do cache (fluxo da aplicação)

Usuário digita o título
➡️
Busca no MongoDB
➡️
[Encontrou?] ── Sim → Retorna dados do banco
│
Não
➡️
Consulta API do TMDb
➡️
Processa dados do filme
➡️
Salva no MongoDB
➡️
Exibe resultado ao usuário

Esse fluxo garante mais **performance**, **menos requisições externas** e **persistência dos dados**.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **MongoDB**
- **Requests** (requisições HTTP)
- **TMDb API** (informações de filmes e streaming)

---

## Resultado no terminal e no Banco:

<img width="500" height="894" alt="Image" src="https://github.com/user-attachments/assets/2ad2133b-fcd8-484f-b5c5-934364ca9273" />
<img width="423" height="247" alt="Image" src="https://github.com/user-attachments/assets/2e01f955-20a4-4742-a787-7d91dc9e50c4" />
