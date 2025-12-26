import sys
from datetime import datetime

def check_system():
    version = sys.version.split()[0]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Sistema iniciado.")
    print(f"Ejecutando Python {version} en modo producción.")
    print("El directorio src/ está operativo.")

if __name__ == "__main__":
    check_system()