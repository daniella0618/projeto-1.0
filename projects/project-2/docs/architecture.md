# Arquitetura do Sistema RAG (Projeto 2)

## Visão Geral

Este projeto implementa uma arquitetura baseada em RAG (Retrieval-Augmented Generation) para análise de conformidade em recomendações de investimento no contexto de Financial Services. A solução evolui uma API baseada em regras fixas para um sistema orientado por conhecimento, garantindo que as decisões sejam baseadas em documentos oficiais, atualizáveis e auditáveis.

## Fluxo da Arquitetura

Usuário → API (/analyze) → Retrieval (busca vetorial - ChromaDB) → Re-ranking → Construção do Contexto → LLM → Resposta + Fontes

## Componentes Principais

### Ingestão de Dados (src/rag/ingestion.py)
Responsável por ler os documentos da pasta knowledge_base, aplicar chunking (divisão em trechos menores), gerar embeddings utilizando TF-IDF e armazenar documentos, embeddings e metadados no banco vetorial ChromaDB. Essa etapa é idempotente e permite reprocessamento sem duplicação, garantindo que o conhecimento fique desacoplado do código.

### Banco Vetorial (ChromaDB)
Responsável por armazenar embeddings dos documentos, realizar buscas por similaridade semântica e servir como base de conhecimento central do sistema. Permite recuperação eficiente e contextual.

### Retrieval (src/rag/retrieval.py)
Responsável por receber a query do usuário, buscar os documentos mais relevantes no banco vetorial e retornar os top_k resultados com base em similaridade. Produz candidatos relevantes para análise.

### Re-ranking (src/rag/reranker.py)
Responsável por reordenar os documentos retornados pelo retrieval, priorizando os trechos mais relevantes para a intenção da query. Melhora significativamente a qualidade do contexto enviado ao LLM.

### Serviço de Orquestração (src/services/compliance_service.py)
Responsável por executar o pipeline RAG completo, chamando retrieval e rerank e construindo o prompt enriquecido com contexto. Centraliza toda a lógica da análise.

### LLM (src/core/llm_client.py)
Responsável por receber o prompt com contexto e gerar a resposta final baseada nos documentos recuperados, reduzindo alucinações e aumentando a confiabilidade.

### API (src/api/routes/analysis.py)
Endpoint: POST /analyze. Responsável por receber o input do usuário, executar o pipeline RAG e retornar resposta estruturada. Exemplo de resposta:
{
  "analysis": "A recomendação apresenta inconsistências...",
  "sources": [
    {
      "source_document": "politica_adequacao_investimento_v1.2.txt",
      "chunk_id": "documento_12"
    }
  ]
}
Garante rastreabilidade e auditabilidade.

## Princípios de Arquitetura

O sistema utiliza Retrieval-Augmented Generation (RAG), garantindo que a resposta do modelo seja baseada em contexto real recuperado da base de conhecimento. A arquitetura também garante auditabilidade, permitindo que cada análise inclua as fontes utilizadas. O conhecimento é desacoplado do código, estando nos documentos, e pode ser atualizado dinamicamente sem alteração da API. Além disso, o uso de re-ranking melhora a relevância e precisão dos resultados.

## Fluxo Completo de Execução

O usuário envia um texto via API. O sistema transforma esse input em uma query. O retrieval busca documentos relevantes no banco vetorial. O re-ranking melhora a ordem dos resultados. O contexto é construído com os documentos mais relevantes. O LLM gera a análise com base nesse contexto. A API retorna a resposta junto com as fontes utilizadas.

## Conclusão

A arquitetura implementada transforma uma API simples em um sistema inteligente baseado em conhecimento. A utilização de RAG garante que as respostas sejam baseadas em dados reais, auditáveis, atualizáveis e mais confiáveis. Essa abordagem reduz alucinações do modelo e aumenta a robustez da análise de conformidade.