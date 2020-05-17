class Pessoa:
    olhos = 2 #atributo default

    def __init__(self, *filhos, nome = None, idade = 23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self): #MÉTODO
        return f'olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls): #quando você quer acessar dados da própria classe
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    mister = Pessoa(nome = 'Mister')
    luciano = Pessoa(mister, nome ='Luciano') #objeto
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    del luciano.filhos
    luciano.olhos = 1 #muda a id de luciano.olhos id(luciano.olhos)
    luciano.sobrenome = 'Ramalho'
    print(luciano.__dict__)  #quais os atributos de instância de um objeto?
    print(mister.__dict__)
    print(Pessoa.olhos)
    print(mister.olhos)
    print(luciano.olhos)
    print(id(mister.olhos), id(luciano.olhos), id(Pessoa.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())