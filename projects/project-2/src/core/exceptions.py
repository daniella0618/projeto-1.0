# Define as exceções personalizadas para a aplicação (permite criar tipos de erro específicos para diferentes situações, facilitando o tratamento de erros e a comunicação de problemas)
class APIConnectionError(Exception):
    pass