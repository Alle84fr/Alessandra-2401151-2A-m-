from funcClasP import Pix

class Cliente:
          def __init__(self, nome:str, cpf:str, saldo:float, extrato:[Pix]):
                    self.nome = nome
                    self.__cpf = cpf
                    self.__saldo = saldo
                    self.__extrato = []

          
          def get_cpf(self):

                    """ Criptografando cpf:
                    atributo = cpf: str
                    met = recebe o "valor, cria um lista nova, percorre (len) pelos caracteres
                    letras recebe posição do valor ao percorrer o total
                    se posição for maior que a 3°, trocar valor por x, e parar quando for 9°
                    em diante.
                    Adiciona à lista
                    criar nova lista, final e concatenar ambas informações"""

                    part1 = cpf[:3] #pelo que entendi - o - dtês serão os três primeiors  valores da str
                    part2 = "xxx"
                     part4 = "xxx"
                    part3 = cpf[-2:]  #pelo que entendi - o - dois serão os dois primeiors últimos valores da str

                    cpf_exib = f" {part1}.{part2}.{part4}-{part3}"
                    
                    return cpf_exib

          def get_saldo(self):

                    """ saldo
                    atri - saldo 
                    caso não tenha ocorrido modificação printar valor original
                    se oucorreu alguma transação mostrar o valor atualizado"""

                    if registrar_trans == 0: saldo = saldo
                    if registrar_trans != 0: saldo = novo_saldo

                    return saldo
          
          def get_extrato(self):
                    if self.registrar_trans == 0: self.registrar_trans = "Sem movimentação"
                    else: self.registrar_trans


          def depositar(self):
                    self.__saldo += valor 
                    novo_saldo = self.__saldo
                    self.registrar_trans

                    return novo_saldo
          
          def retirar(self):
                    if saldo >= valor: 
                              novo_saldo = self.__saldo -= valor
                              self.registrar_trans
                    else:
                              print(f"Saldo insuficiente para realizar transação")
                    
                    return novo_saldo
          
          def trans_pix(self, valor, destinatario):
                    pix = Pix(self, destinatario, valor):
                    pix.transacionar()

          def registrar_trans(self, transacao):
                    self.__extrato.append(transacao)

          

                              





