class Pessoa:
    def __init__(self, nome = None, idade = 23):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Mister'
    print(p.nome)