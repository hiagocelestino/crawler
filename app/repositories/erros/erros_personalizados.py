class ErrorPersistirDados(Exception):
    def __init__(self, message = 'Erro ao persistir dados no banco.'):
        super().__init__(message)


class ErrorBuscarDados(Exception):
    def __init__(self, message = 'Erro ao buscar dados no banco.'):
        super().__init__(message)
