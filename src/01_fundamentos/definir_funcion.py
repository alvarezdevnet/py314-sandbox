def calcular_suma(a, b):
    """
    Toma dos argumentos numéricos y devuelve su suma.
    Al usar 'return', podemos guardar el resultado en una variable.
    """
    return a + b

def mostrar_saludo():
    """
    Simplemente imprime mensajes en pantalla.
    No devuelve ningún valor útil al programa (devuelve None implícitamente).
    """
    print("--- Ejecutando función de saludo ---")
    print("Hola desde el sistema de logs.")

# --- BLOQUE DE EJECUCIÓN ---
if __name__ == "__main__":
    
    # CASO 1: Función con Return (Útil para cálculos)
    resultado_operacion = calcular_suma(10, 20)
    print(f"El resultado almacenado es: {resultado_operacion}")

    # CASO 2: Función con Print (Solo efectos visuales)
    print("\nLlamando a la función de saludo:")
    variable_vacia = mostrar_saludo() 
    
    # La prueba de la verdad:
    print(f"\n¿Qué guardó la variable del saludo?: {variable_vacia}")
    # Verás que dice 'None'. Por eso print NO es return.