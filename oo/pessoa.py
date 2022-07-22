class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    gabriel = Pessoa(nome='Gabriel')
    natalia = Pessoa(nome='Natália')
    fernando = Pessoa(gabriel, natalia, nome='Fernando')
    print(Pessoa.cumprimentar(fernando))
    print(id(fernando))
    print(fernando.cumprimentar())
    print(fernando.nome)
    print(fernando.idade)
    for filho in fernando.filhos:
        print(filho.nome)
    fernando.sobrenome = 'Piazenski' #atributo adicionado dinamicamente
    print(fernando.sobrenome)
    print(fernando.__dict__)
    print(gabriel.__dict__)
    del fernando.filhos # remoção dinâmica de atributo
    print(fernando.__dict__)