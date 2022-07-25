"""
Para usar o framework de testes é necessário criar um arquivo (como esse) que começa com 'test' ou 'teste',
é possível usar 'teste' porque a palavra começa com 'test'.
Nesse framewor se usa o conceito de herança, herdando da classe TestCase, esta classe vem no pacote unittest,
que vem no interpretador padrão do python.
A classe que será usada para realizar o teste terá de possuir métodos com comecem com o prefixo 'test',
 ou 'teste' pela mesma razão de a palavra começar com 'test'.

Obs.: Quando se roda o teste clicando no método, o teste vai ser realizado apenas naquele método.

"""


from unittest import TestCase

from oo.carro import Motor

class CarroTest(TestCase):
    def test_velocidade(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
