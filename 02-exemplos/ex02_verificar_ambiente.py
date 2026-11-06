# Exemplo 02 — Verificar o ambiente
# Objetivo: confirmar que o Python está instalado e funcionando.
#
# Você ainda NÃO precisa entender este código: ele usa recursos que veremos
# nas próximas unidades. Basta executá-lo a partir da pasta raiz:
#
#     python 02-exemplos/ex02_verificar_ambiente.py
#
# e copiar a saída para a atividade 06.

import platform
import sys

versao = platform.python_version()
sistema = platform.system() or "desconhecido"

print("=== Verificação do ambiente ===")
print("Python:", versao)
print("Sistema:", sistema)

if sys.version_info >= (3, 8):
    print(f"Ambiente OK: Python {versao} em {sistema}")
else:
    print("ATENÇÃO: instale uma versão mais recente do Python 3.")
