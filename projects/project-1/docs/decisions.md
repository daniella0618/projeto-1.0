# Technical Decisions

## Uso do FastAPI
O FastAPI foi escolhido por sua simplicidade na criação de APIs REST, alta performance e geração automática de documentação interativa via Swagger.

## Uso do Pydantic
O Pydantic foi utilizado para definir os schemas de entrada e saída da API, garantindo validação de dados e consistência no formato das respostas.

## Uso do Azure OpenAI
Foi utilizado o Azure OpenAI para simular um analista de compliance automatizado, capaz de avaliar recomendações de investimento com base no perfil de risco do cliente.

## Uso de Prompt Estruturado
O prompt foi estruturado para forçar o modelo de linguagem a retornar a resposta em formato JSON. Isso evita ambiguidades e facilita o processamento da resposta dentro da aplicação.

## Arquitetura em Camadas
A aplicação foi organizada em camadas:
- API (endpoints)
- Services (lógica de negócio)
- Core (cliente do LLM)

Essa separação melhora a manutenção, organização e escalabilidade do sistema.

## Tratamento de Erros
Foi implementado tratamento de exceções para garantir que falhas na chamada ao modelo não quebrem a API, retornando uma resposta controlada ao usuário.
