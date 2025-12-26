print("--- SISTEMA DE CONTROL DE ACCESO ---")

# 1. INPUT
# input() siempre devuelve TEXTO (string).
# Para comparar con números (< 18), debemos convertirlo a ENTERO (int).
edad_usuario = int(input("Por favor, muestra tu DNI (Introduce tu edad): "))

# 2. LOGIC (El Cerebro)
if edad_usuario < 18:
    # Caso: Menor de edad
    print("ACCESO DENEGADO.")
    print(f"Te faltan {18 - edad_usuario} años para poder entrar.")

elif edad_usuario >= 65:
    # Caso: Jubilado (VIP)
    print("ACCESO VIP CONCEDIDO.")
    print("¡Bienvenido! Tienes una consumición gratis por veteranía.")

else:
    # Caso: Adulto estándar (entre 18 y 64)
    print("ADELANTE.")
    print("La entrada son 10 euros.")

print("------------------------------------")
print("Siguiente en la fila, por favor.")