class Pessoa:
    olhos = 2 # esse é um atributo default ou atributo de classe (pois ele pode ser acessado pela classe)
              # útil quando for um atributo comum a todos ou a maioria dos objetos instanciados, economiza memória utilizada
              # não serão apresentados no __dict__
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls}  - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'
    # Aqui foi implementado a sobrescrita de método. Uma sobrecrita simples iria substituir por completo o método da classe pai,
    # contudo foi usado uma lógica que acrescenta ao método da classe pai, o método 'super()' faz com que seja utilizado/buscado
    # o méotod da classe pai.

class Mutante(Pessoa):
    olhos = 3 # como esse atributo já existe na classe pai, há uma sobrescrita de atributo


if __name__ == '__main__':
    gabriel = Mutante(nome='Gabriel')
    # Foi alterado o tipo do objeto, de Pessoa para Homem, mas como foi utlizado o método herânca a classe filho (Homem)
    # apresenta todos os atributos (sentido amplo - atributos de dados e métodos) da classe pai, por isso não deve ocorrer
    # nenhum problema com essa alteração de objeto.

    natalia = Pessoa(nome='Natália') # Poderia ser trocado o objeto, de Pessoa para Homem, aqui também
    fernando = Homem(gabriel, natalia, nome='Fernando')
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
    # Pessoa.olhos = 3 # aqui está se alterando o valor do atributo de classe, o que afeta todas os objetos que
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

    print()
    print('Teste do is instance') # serve para sabe se um ojbeto é de determinado tipo/classe
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(gabriel, Homem))
    print(isinstance(fernando, Homem))
    print(isinstance(gabriel, Pessoa))
    print(isinstance(fernando, Pessoa))

    print()
    print('Parte sobre sobrescrita de atributos')
    print(gabriel.olhos)

    print()
    print(gabriel.cumprimentar())
    print(fernando.cumprimentar())
