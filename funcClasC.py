from funcClasP import Pix

class Cliente:
          def __init__(self, nome:str, cpf:str, saldo:float):
                    self.nome = nome
                    self.__cpf = cpf
                    self.__saldo = saldo
                    self.__extrato = []
          
          def set_cpf(self):
                    
                    """ Criptografando cpf:
                    atributo = cpf: str
                    met = recebe o "valor, cria um lista nova, percorre (len) pelos caracteres
                    letras recebe posição do valor ao percorrer o total
                    se posição for maior que a 3°, trocar valor por x, e parar quando for 9°
                    em diante.
                    Adiciona à lista
                    criar nova lista, final e concatenar ambas informações"""

                    cpf = self_.cpf
                    cpf_crip = []
                    for i in range(len(cpf)):
                              letra = cpf[i]
                              if i >3 and i<9: letra = "x"
                              cpf_crip.append(letra)
                    cpf_exib = ""
                    for letra in cpf:
                              cpf_exib += letra
                    
                    return cpf_exib
                              





