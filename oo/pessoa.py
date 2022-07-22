class Pessoa:
    olhos = 2 # esse é um atributo default ou atributo de classe (pois ele pode ser acessado pela classe)
              # útil quando for um atributo comum a todos ou a maioria dos objetos instanciados, economiza memória utilizada
              # não serão apresentados no __dict__
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
    print(fernando.__dict__) # apenas apresenta a referência dos atributos de instância e não para os atributos de classe
    print(gabriel.__dict__)
    del fernando.filhos # remoção dinâmica de atributo
    print(fernando.__dict__)
    print(Pessoa.olhos)
    print(fernando.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos), id(fernando.olhos), id(gabriel.olhos)) # apresentam o mesmo id, logo não ocupam 3 cantos
                                                                   # diferentes de memória

    print()
    print('Alterando um atributo de classe, o que gerou um atributo de instância')
    fernando.olhos = 1 # nesse caso só foi alterado o número de olhos do objeto fernando e atribuido dinamicamente esse atributo a esse objeto
                       # portanto esse atributo deixou de ser um atributo de classe (o qual não foi deletado) e passou sa ser um atributo de instância
                       # apenas para esse objeto
    print(gabriel.__dict__)
    print(fernando.__dict__)
    print(Pessoa.olhos)
    print(fernando.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos), id(fernando.olhos), id(gabriel.olhos))

    print()
    print('Trocando o valor de olhos para todas as pessoas.')
    Pessoa.olhos = 3 # aqui está se alterando o valor do atributo de classe, o que afeta todas os objetos que
                     # não foram alterados de forma particular como acima.
    print(gabriel.__dict__)
    print(fernando.__dict__)
    print(Pessoa.olhos)
    print(fernando.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos), id(fernando.olhos), id(gabriel.olhos))


    print()
    print('Deletando o atributo de instância.')
    del fernando.olhos # ao se deletar o atributo de instância o objeto volta a usar o atribudo de classe
    print(gabriel.__dict__)
    print(fernando.__dict__)
    print(Pessoa.olhos)
    print(fernando.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos), id(fernando.olhos), id(gabriel.olhos))