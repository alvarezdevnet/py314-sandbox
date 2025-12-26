print("--- Analizador de Títulos de Libros ---")

# Solicitamos datos al usuario (Input)
titulo_usuario = input("Introduce el título de un libro: ")

# Procesamiento (Process)
longitud = len(titulo_usuario)

# Salida (Output)
print(f"El título '{titulo_usuario}' tiene {longitud} caracteres.")

# --- VERIFICACIÓN DE ESPACIOS ---
# Truco pro: ¿Cuántas letras reales tiene sin contar espacios?
# Usamos .replace(" ", "") para eliminar espacios temporalmente y medir.
longitud_sin_espacios = len(titulo_usuario.replace(" ", ""))

print(f"Letras reales (sin espacios): {longitud_sin_espacios}")