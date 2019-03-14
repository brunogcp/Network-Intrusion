import sys
import dns.resolver

argumentos = sys.argv
try:
  dominio = argumentos[1]
  lista = argumentos[2]
except:
  print("Faltam argumentos no comando")
  sys.exit(1)

try:
  arquivo = open(lista)
  linhas = arquivo.read().splitlines()
except:
  print("Arquivo nao encontrado ou invalido")
  sys.exit(1)

for linha in linhas:
  subdominio = linha + '.' + dominio
  try:
    resposta = dns.resolver.query(subdominio, 'a')
    for resultado in resposta:
      print subdominio, resultado
  except:
    pass