# Technical Decisions

## FastAPI
O FastAPI foi utilizado como framework para construção da API REST. Ele permite definir endpoints de forma simples e oferece integração nativa com validação de dados via Pydantic.

No projeto, o FastAPI é responsável por expor o endpoint `/analyze`, que recebe a requisição e delega o processamento para a camada de serviço.

## Pydantic
O Pydantic foi utilizado para definição dos modelos de dados de entrada e saída da API.

Foram definidos os seguintes schemas:
- `AnalysisRequest`: contém o texto da recomendação e o perfil do cliente
- `AnalysisResult`: estrutura padronizada da resposta, incluindo:
  - indicação de conformidade (`is_compliant`)
  - justificativa (`reason`)
  - produtos identificados (`mentioned_products`)

Isso garante consistência na comunicação entre cliente e API.

## Azure OpenAI
O Azure OpenAI foi utilizado como mecanismo de análise da recomendação de investimento.

A integração foi implementada na classe `AzureModel`, responsável por:
- configurar o cliente com variáveis de ambiente
- enviar requisições ao modelo via `chat.completions`
- retornar a resposta bruta do modelo

O modelo é utilizado para simular um especialista em compliance financeiro.

## Prompt Estruturado
Foi utilizado um prompt estruturado dentro da camada de serviço (`compliance_service`) com as seguintes características:
- definição explícita do papel do modelo ("especialista em compliance financeiro")
- regras claras de análise
- instrução para resposta obrigatória em formato JSON

Essa abordagem permite converter diretamente a resposta do modelo em um objeto Python utilizando `json.loads`, reduzindo ambiguidade.

## Arquitetura em Camadas
A aplicação foi organizada em três camadas principais:

- **API (`main.py`)**
  - Define o endpoint `/analyze`
  - Recebe a requisição e chama o serviço

- **Services (`compliance_service.py`)**
  - Contém a lógica de construção do prompt
  - Processa a resposta do modelo
  - Converte a saída para o schema definido

- **Core (`llm_client.py`)**
  - Responsável pela comunicação com o Azure OpenAI
  - Encapsula a configuração e chamada do modelo

Essa separação mantém o código organizado e facilita entendimento e manutenção.

## Tratamento de Erros
O tratamento de erros foi implementado na camada de serviço (`analyze_recommendation`).

Um bloco `try/except` encapsula:
- a chamada ao modelo
- o parsing da resposta JSON

Em caso de falha (ex: erro no formato retornado pelo modelo ou erro na chamada da API), é retornado um `AnalysisResult` com:
- `is_compliant = False`
- mensagem de erro no campo `reason`
- lista vazia de produtos

Essa abordagem evita que a API quebre e garante uma resposta consistente ao cliente, mesmo em cenários de erro.

## Teste Manual do Modelo
Foi criado um script (`tests/testes_llm.py`) para teste manual da integração com o modelo.

Esse script permite:
- enviar entradas diretamente pelo terminal
- visualizar respostas do modelo
- validar comportamento fora da API

Ele também inclui tratamento básico de erro para capturar falhas na chamada ao modelo.
``
