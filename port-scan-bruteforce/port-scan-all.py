import sys
import socket

my_list = []
numero_Portas = 10000

argumentos = sys.argv
try:
  dominio = argumentos[1]
except:
  print("Faltam argumentos no comando")
  sys.exit(1)

for porta in range(numero_Portas):
  percentual = 100.00 / numero_Portas
  porta_percentual = percentual * porta
  cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  cliente.settimeout(0.2)
  codigo = cliente.connect_ex((dominio, int(porta)))
  protocolo = socket.getservbyport
  if codigo == 0:
    print "\n", porta, "OPEN", protocolo
    my_list.append(porta)
  else:
    print '\r>> Scanning Port', porta,'You have finished %d%%' % porta_percentual, 
  sys.stdout.flush()

print "\n"

for lista in my_list:
  print "Porta: ", lista , " OPEN"