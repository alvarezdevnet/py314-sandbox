from datetime import datetime, timedelta  # <--- Importamos timedelta

nombre_astronauta = "Jose Alvarez"
edad_astronauta = 45
destino = "Marte"
combustible = 85
velocidad = 27000  # km/h

# --- CÁLCULO DE FECHAS DINÁMICO ---
# 1. Capturamos el momento actual
ahora = datetime.now()

# 2. Calculamos "mañana" sumando 1 día al momento actual
manana = ahora + timedelta(days=1)

# 3. Formateamos ambas fechas a texto (String) limpio: Año-Mes-Día
fecha_dia_1 = ahora.strftime("%Y-%m-%d")
fecha_dia_2 = manana.strftime("%Y-%m-%d")

# --- INICIO DEL LOG ---
print("Diario de un Astronauta\n")

print(f"Hola, soy {nombre_astronauta}, tengo {edad_astronauta} años y mi próximo destino es {destino}.")
print(f"Estoy navegando a {velocidad} km/h con {combustible}% de combustible restante hacia {destino}.")

print("--------------------")
print(f"Fecha: {fecha_dia_1}")  # <--- Variable dinámica

print("Hoy experimentamos con el cultivo de plantas en microgravedad.")
print("Mensaje personal: ¡Es increíble ver cómo crecen las lechugas aquí arriba!\n")

print(f"Fecha: {fecha_dia_2}")  # <--- Variable dinámica
print("Realizamos una caminata espacial para reparar un panel solar.")
print("Mensaje personal: Flotar en el espacio nunca deja de asombrarme.\n")