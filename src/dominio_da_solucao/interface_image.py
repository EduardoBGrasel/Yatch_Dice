class InterfaceImage:
    def __init__(self):
        super().__init__()
        self.message = ""
        self.lista_dados = []
        self.lista_selecionados = []
        self.pontuacoes = []
    
    def set_message(self, text):
        self.message = text
    
    def get_message(self):
        return self.message
    
    def set_lista_dados(self, lista):
        self.lista_dados = lista
    
    def get_lista_dados(self):
        return self.lista_dados
    
    def get_lista_selecionados(self):
        return self.lista_selecionados
    
    def set_lista_selecionados(self, lista):
        self.lista_selecionados = lista

    def set_pontuacoes(self, pontuacao):
        self.pontuacoes = pontuacao
    
    def get_pontuacoes(self):
        return self.pontuacao
    
