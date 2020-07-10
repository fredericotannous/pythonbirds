class Pessoa: #forma de criar seus tipos personalizados - forma de gelo
    olhos = 2 #atributo default

    def __init__(self, *filhos, nome = None, idade=23): #metodo
        self.idade = idade
        self.nome = nome #atributo de dado
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    frederico = Pessoa(renzo, nome='Frederico')
    print(Pessoa.cumprimentar(frederico))
    print(id(frederico))
    print(frederico.cumprimentar())
    print(frederico.nome)
    print(frederico.idade)
    for filho in frederico.filhos:
        print(filho.nome)
    frederico.sobrenome = 'Tannous'
    print(frederico.__dict__) #dunderdict
    print(renzo.__dict__)
    del frederico.filhos
