class produto:
    def __init__(self, nome, quantidade, preco, peso):
        self.preco = preco
        self.quantidade = quantidade
        self.nome = nome
        self.peso = peso
        
    def get_preco(self):
        return self.preco    
    
    def get_quantidade(self):
        return self.quantidade
    
    def get_nome(self):
        return self.nome
    
    def get_peso(self):
        return self.peso

    def recuperar(self):
        print ("Nome: {}".format(self.nome))
        print ("Preço: {}".format(self.preco))
        print ("Quantidade {}".format(self.quantidade))
        print ("Peso: {}".format(self.peso))