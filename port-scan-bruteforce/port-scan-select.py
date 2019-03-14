import sys
import socket

argumentos = sys.argv
try:
  dominio = argumentos[1]
  portas = argumentos[2]
except:
  print("Faltam argumentos no comando")
  sys.exit(1)

try:
  arquivo = open(portas)
  linhas = arquivo.read().splitlines()
except:
  print("Arquivo nao encontrado ou invalido")
  sys.exit(1)

for linha in linhas:
  cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  cliente.settimeout(0.5)
  codigo = cliente.connect_ex((dominio, int(linha)))
  if codigo == 0:
    print linha, "OPEN"