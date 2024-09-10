def infor():

          """ Introduz nome e cpf do cliente"""

          cli = dict(
          
                    nome= input("Nome: "),
                    cpf= input("Cpf: "),
                    saldo= float(input("Saldo: "))
          )
          return cli

