from funcClasC import Cliente

class Pix:
          def __init__(self, remetente:Cliente, destinatario:Cliente, valor:float):
                    self.__remetente = remetente
                    self.__destinatario = destinatario
                    self.__valor = valor
          

          def transacao(valor, destinatario):
                  if depositar:
                    if self._remetente.saldo >= self._valor:
                              self._remetente.saldo -= self._valor
                              self.__destinatario.saldo += self.valor
                              