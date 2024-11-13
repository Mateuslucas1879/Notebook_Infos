import sys
import os
import subprocess
import platform
import psutil
import socket
import os


def get_linux_model():
    try:
        result = subprocess.check_output("wmic csproduct get name",shell=True,test=True)
        return result.split("\n")[1].strip()
    except subprocess.CalledProcessError:
        return "Não foi possivel obter o modelo do notebook"

print("Modelo do notebook",get_linux_model())

