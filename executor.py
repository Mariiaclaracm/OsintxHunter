#!/usr/bin/env python3
import sys
import subprocess

if sys.version_info.major < 3 or sys.version_info.minor < 10:
    print('\033[93m[!] Python 3.10+ é necessário. Encerrando.\033[0m')
    sys.exit(1)

print("[executor] theHarvester foi iniciado com sucesso")

# Monta o comando para rodar o theHarvester como módulo
cmd = [sys.executable, "-m", "theHarvester"] + sys.argv[1:]

try:
    subprocess.run(cmd, check=True)
except subprocess.CalledProcessError as e:
    print(f"[executor] Erro ao executar theHarvester: {e}")
    sys.exit(1)
