# Decisões Técnicas – Compliance Checker API

## 1. Arquitetura em Camadas

Optamos por uma arquitetura em camadas para garantir separação de responsabilidades e facilitar manutenção e escalabilidade.

- **api/**: responsável por expor os endpoints HTTP (FastAPI)
- **schemas/**: define contratos de entrada e saída da API usando Pydantic
- **services/**: contém a lógica de negócio desacoplada da camada HTTP
- **core/**: centraliza configurações e integração com serviços externos (LLM)

Benefício: facilita testes, manutenção e evolução do sistema.

---

## 2. Uso do FastAPI

Escolhemos o FastAPI por:

- Alta performance
- Facilidade de criação de APIs REST
- Documentação automática via Swagger/OpenAPI (`/docs`)
- Integração nativa com Pydantic

Benefício: acelera desenvolvimento e garante documentação padronizada.

---

## 3. Uso do Pydantic

Utilizamos Pydantic para:

- Validar dados de entrada (request)
- Garantir estrutura do retorno (response)
- Evitar inconsistências no contrato da API

Benefício: maior confiabilidade e padronização das respostas.

---

## 4. Integração com Azure OpenAI (LLM)

Optamos por utilizar o Azure OpenAI como motor de inteligência do sistema.

A integração foi encapsulada em um cliente reutilizável (`llm_client.py`), responsável por:

- Gerenciar autenticação via `.env`
- Enviar prompts estruturados
- Receber respostas do modelo

Benefício: desacopla a lógica de IA do restante da aplicação.

---

## 5. Prompt Engineering

Foi criado um prompt estruturado para:

- Garantir respostas em formato JSON
- Evitar respostas ambíguas ou inconsistentes
- Orientar o modelo com regras de compliance

Exemplo de regras:
- Proibir promessas de lucro garantido
- Exigir menção a riscos
- Avaliar contexto do texto

Benefício: melhora a qualidade e previsibilidade das respostas do LLM.

---

## 6. Tratamento de Erros

Implementamos tratamento de erros para:

- Falhas na chamada do LLM
- Respostas inválidas (JSON mal formatado)

Em caso de erro:
- A API retorna uma resposta padronizada
- Evita quebra do sistema

Benefício: maior robustez e estabilidade.

---

## 7. Containerização com Docker

Criamos um `Dockerfile` para:

- Empacotar a aplicação
- Garantir ambiente consistente
- Facilitar deploy

Comando de execução:

```bash
docker run -p 8000:8000 --env-file .env compliance-api