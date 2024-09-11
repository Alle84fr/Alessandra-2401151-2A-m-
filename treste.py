


def form_cpf(c):

          """ Criptografar cpf fatiando
          
          atri - cpf na froma de texto
          
          meto - pegar os 3 primeiros "valores" e mater
          como o cpd tem 4 partes, separados por . e -, as
          do meio serão transformadas em x, pegaremos
          os dois últimos valores ( está negativo por estar voltando
          e deixaremos na forma origonal
          por fim , para impressão sair correta, )
          """

          part1 = c[:3] #pelo que entendi - o - dtês serão os três primeiors  valores da str
          part2 = "xxx"
          part4 = "xxx"
          part3 = c[-2:]  #pelo que entendi - o - dois serão os dois primeiors últimos valores da str

          ccc = f" {part1}.{part2}.{part4}-{part3}"

          print(ccc)



