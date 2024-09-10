Classe - 1° letra MAIÚSCULA se mais palavras, devem ficar juntas ex:PrimeiraLetraMaiuscula

lembrando que inicia com 


nome da Classe - classe define métodos a serem aplicados
_______________

atributos - características do objeto
_______________

método - sequências de instruções para acessar dados
______________

ex:

classe - cachorro
______________

atributo

nome, raça, peso, cor dos pelos (características)

coloca-se o tipo, se é int, float, str, 

______________

método

late, come, dorme, morde (comportamento)

void - função sem retorno ou função com retorno


1. criar classe:

palavras chave = class e o nome dela, ex: class NomeDela:

2. criar objeto vazio:

Nome da classe mais () ex: Nomeclasse()

3. iniciar objeto construtor:

construtor/método _ _init__ , dois uinderscrol de cada lado (dunder methods.)

aqui define os valores para os parãmetros

4. self:

refere-se que está falando das características do objeto em si, e não qualquer outro

para saber o n° de identificação do objeto usa-se o id(nome do objeto)

5. função/parametros:

ter def inicialmente construtor () self, parâmetros tipo

associa parâmetro ao atributo do obs

def __int __ (self, parâmetro:tipo, parâmetro:tipo):

.........self.atributo = parâmetro

ex: def __init __ (self, nom:str, idad:int, matricula:str)

........self.nome = nom

........self.idade = idad

........self.mat = matricula

caso seja privado

........self.__nom = nome  (dois underscrol)

6. méetodos:

são funções dentro da própria classe

set - altera o valor do atributo (para público)

lembrar que por ser função inicia com def

def setNomeDestaClasse(self,nom):

método - self.atributo = parâmetro


- set none atributo (self, parâmetro definido anteriormente dentro da classe):

ex: def set NomeDoCachorro(self, nom):

         self.nome= nom

- get - 

7. para instanciar:

no principal

variável = NomeDaClasse (valor para cada tributo) 

ex: cachorro = Canino("Sanssão", "8", "vira lata")

obs - na classe está

class Canino:

          def __init __ (self, nome:str, idade:int, raca:str):

                    self.nome = nome

                    self.ida = idade

                    self.raca = raca










