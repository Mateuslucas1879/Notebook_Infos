import sys
import os
import subprocess
import platform
import psutil
import socket
import os


def get_system_info():
    info = {
        "Sistema Operacional": platform.system(),
        "Versão do Sistema Operacional": platform.version(),
        "Nome do Computador": socket.gethostname(),
        "Endereço IP": socket.gethostbyname(socket.gethostname()),
        "Processador": platform.processor(),
        "Arquitetura": platform.architecture()[0],
        "Memória RAM Total (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Memória RAM Disponível (GB)": round(psutil.virtual_memory().available / (1024 ** 3), 2),
        "Uso da CPU (%)": psutil.cpu_percent(interval=1),
        "Número de Núcleos": psutil.cpu_count(logical=True),
        "Espaço Total em Disco (GB)": round(psutil.disk_usage('/').total / (1024 ** 3), 2),
        "Espaço Usado em Disco (GB)": round(psutil.disk_usage('/').used / (1024 ** 3), 2),
        "Espaço Livre em Disco (GB)": round(psutil.disk_usage('/').free / (1024 ** 3), 2),
    }
    return info

# Exibindo as informações
for key, value in get_system_info().items():
    print(f"{key}: {value}")


def get_linux_model():
    try:
        result = subprocess.check_output("systeminfo",shell=True,text=True)
        return result.split("\n")[1].strip()
    except subprocess.CalledProcessError:
        return "Não foi possivel obter o modelo do notebook"


print("Modelo do notebook: ", get_linux_model())
