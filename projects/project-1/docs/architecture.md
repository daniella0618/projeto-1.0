# Arquitetura

A aplicação foi desenvolvida utilizando uma arquitetura em camadas, com o objetivo de garantir organização, separação de responsabilidades, escalabilidade e facilidade de manutenção.

## Visão Geral

A solução consiste em uma API REST construída com FastAPI, que utiliza um modelo de linguagem (Azure OpenAI) para analisar recomendações de investimento de forma automatizada.

## Fluxo da Aplicação

O fluxo da aplicação funciona da seguinte forma:

1. O cliente envia uma requisição HTTP para o endpoint `/analyze`.
2. A requisição é recebida pela camada de API (FastAPI).
3. Os dados são validados por meio dos schemas Pydantic (`AnalysisRequest`).
4. A requisição é encaminhada para a camada de serviço (`compliance_service`).
5. O serviço chama o cliente de LLM (`llm_client`) localizado na camada `core`.
6. O modelo de linguagem (Azure OpenAI) processa o texto com base em um prompt estruturado.
7. A resposta da IA é retornada e convertida para JSON.
8. A API devolve a resposta estruturada ao cliente (`AnalysisResponse`).

## Estrutura de Pastas

A arquitetura do projeto está organizada nas seguintes camadas:

- **api/**  
  Responsável pela exposição dos endpoints HTTP e pela comunicação com o cliente.

- **schemas/**  
  Define os contratos de entrada e saída da API utilizando Pydantic, garantindo validação e padronização.

- **services/**  
  Contém a lógica de negócio da aplicação, desacoplada da camada HTTP.

- **core/**  
  Centraliza integrações externas e configurações, incluindo a comunicação com o Azure OpenAI.

## Integração com IA (LLM)

A análise de conformidade é realizada utilizando o Azure OpenAI.  
A integração está encapsulada em um cliente reutilizável (`llm_client.py`), responsável por:

- Gerenciar autenticação via variáveis de ambiente (`.env`)
- Enviar prompts estruturados ao modelo
- Receber e retornar a resposta da IA

Foi utilizado um prompt estruturado para garantir que a resposta do modelo seja consistente e no formato JSON.

## Tratamento de Respostas e Erros

A resposta do modelo de linguagem é processada e convertida para JSON utilizando `json.loads`.

Para garantir robustez, foi implementado um mecanismo de fallback que retorna uma resposta padrão caso haja falha na interpretação do JSON ou erro na chamada do LLM.

## Containerização

A aplicação foi containerizada utilizando Docker, permitindo sua execução em diferentes ambientes de forma consistente.

Execução do container:

```bash
docker run -p 8000:8000 --env-file .env compliance-api