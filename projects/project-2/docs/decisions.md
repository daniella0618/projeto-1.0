# Registro de Decisões Arquiteturais (ADRs)

Este documento registra as principais decisões arquiteturais tomadas ao longo do desenvolvimento do Projeto 2 – Sistema RAG para análise de compliance.

---

## ADR 001 – Adoção de Arquitetura RAG

### Contexto
A versão inicial da API utilizava regras fixas embutidas no prompt, dificultando manutenção, atualização e auditabilidade.

### Decisão
Adotar uma arquitetura baseada em Retrieval-Augmented Generation (RAG), onde o modelo de linguagem utiliza contexto recuperado de uma base de conhecimento.

### Consequências
- As respostas passam a ser baseadas em documentos reais
- O sistema se torna auditável
- Permite atualização do conhecimento sem alterar o código
- Reduz alucinação do modelo

---

## ADR 002 – Utilização de ChromaDB como Banco Vetorial

### Contexto
Era necessário armazenar e consultar embeddings de documentos de forma eficiente.

### Decisão
Utilizar ChromaDB como banco vetorial local.

### Consequências
- Fácil setup e integração com Python
- Não depende de serviços externos
- Ideal para prototipagem e desenvolvimento local

---

## ADR 003 – Estratégia de Embeddings com TF-IDF

### Contexto
Era necessário converter texto em vetores para busca por similaridade.

### Decisão
Utilizar TF-IDF para geração de embeddings.

### Consequências
- Simples e sem dependência externa
- Baixo custo computacional
- Menor qualidade semântica comparado a embeddings avançados

---

## ADR 004 – Estratégia de Chunking Simples

### Contexto
Os documentos são longos e precisam ser divididos para melhor recuperação.

### Decisão
Dividir os documentos em trechos com base em linhas de texto.

### Consequências
- Implementação simples
- Permite granularidade na busca
- Pode não capturar completamente o contexto semântico

---

## ADR 005 – Implementação de Re-ranking

### Contexto
Os resultados do retrieval nem sempre estavam ordenados por relevância ideal.

### Decisão
Adicionar etapa de re-ranking após a recuperação inicial.

### Consequências
- Melhora a qualidade dos resultados
- Aumenta precisão da resposta
- Introduz pequena complexidade adicional

---

## ADR 006 – Uso de múltiplos documentos (top_k)

### Contexto
Um único documento pode não fornecer contexto suficiente.

### Decisão
Retornar vários documentos relevantes (top_k = 3).

### Consequências
- Maior robustez na resposta
- Melhor cobertura de contexto
- Necessidade de ordenação (re-ranking)

---

## ADR 007 – Orquestração via Serviço de Compliance

### Contexto
Era necessário estruturar o fluxo do pipeline RAG.

### Decisão
Centralizar a lógica no serviço `compliance_service.py`.

### Consequências
- Código mais organizado
- Separação clara de responsabilidades
- Facilita manutenção e testes

---

## ADR 008 – Inclusão de Fontes na Resposta

### Contexto
A análise de compliance exige rastreabilidade.

### Decisão
Retornar documento e chunk_id utilizados na geração da resposta.

### Consequências
- Aumenta transparência
- Permite auditoria
- Diferencial importante do sistema

---

## ADR 009 – Uso de FastAPI

### Contexto
Era necessário expor o sistema como API.

### Decisão
Utilizar FastAPI como framework.

### Consequências
- Desenvolvimento rápido
- Documentação automática (Swagger)
- Boa performance

---

## Conclusão

As decisões arquiteturais priorizaram simplicidade, auditabilidade e eficiência, permitindo a construção de um sistema RAG funcional e extensível.

Possíveis evoluções futuras incluem:
- Uso de embeddings baseados em deep learning
- Chunking semântico mais sofisticado
- Banco vetorial em nuvem
- Técnicas avançadas de re-ranking
