#!/usr/bin/env bash
set -e

echo " --atualizar os pacotes--"
sudo apt update

echo "-- instalar python, pip, git e cenas da captura--"
sudo apt install -y python3 python3-pip python3-venv git libpcap-dev tcpdump wireshark

echo " -- criar ambiente virtual e meter o scapy -- "
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install scapy

echo " pronto."
echo "exemplo para correr na maquina:"
echo "sudo .venv/bin/python scapy.py --rede !<rede>! --iface !<iface>!"
