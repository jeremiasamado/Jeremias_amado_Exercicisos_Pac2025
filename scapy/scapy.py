import argparse
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path = [p for p in sys.path if p not in ("", script_dir)]

from scapy.all import ARP, Ether, sniff, srp

parser = argparse.ArgumentParser()
parser.add_argument("--rede", required=True, help="Ex: 192.168.1.0/24")
parser.add_argument("--iface", required=True, help="Ex: eth0")
parser.add_argument("--monitor", action="store_true")
args = parser.parse_args()

print("fazer scan da rede:", args.rede)
arp = ARP(pdst=args.rede)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
pacote = ether / arp
respostas = srp(pacote, timeout=2, verbose=0)[0]

dispositivos = []
print("\ndispositivos que apareceram:")
for enviado, recebido in respostas:
    print(recebido.psrc, recebido.hwsrc)
    dispositivos.append((recebido.psrc, recebido.hwsrc))

print("\na apanhar 50 pacotes na interface", args.iface)
pacotes = sniff(iface=args.iface, count=50)
print("feito acabou a captura\n")

for i, p in enumerate(pacotes, start=1):
    print(str(i) + ".", p.summary())

ficheiro = open("resultados_scapy.txt", "w", encoding="utf-8")
ficheiro.write("rede: " + args.rede + "\n")
ficheiro.write("interface: " + args.iface + "\n\n")
ficheiro.write("dispositivos ativos --IP MAC--\n")
for ip, mac in dispositivos:
    ficheiro.write(ip + " " + mac + "\n")
ficheiro.write("\n---Pacotes capturados---\n")
for i, p in enumerate(pacotes, start=1):
    ficheiro.write(str(i) + ". " + p.summary() + "\n")
ficheiro.close()

print("\nguardou os resultados em resultados_scapy.txt")

if args.monitor:
    print("\nmonitorização ligada --Ctrl+C para parar--\n")
    sniff(iface=args.iface, prn=lambda p: print(p.summary()), store=False)
