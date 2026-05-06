import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path = [p for p in sys.path if p not in ("", script_dir)]

from scapy.all import IP, ICMP, sr1

print("teste scapy ok")

resposta = sr1(IP(dst="8.8.8.8") / ICMP(), timeout=2, verbose=0)

print(resposta)