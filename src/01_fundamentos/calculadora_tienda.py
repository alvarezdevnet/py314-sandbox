def aplicar_descuento(precio_original, porcentaje_descuento):
    """
    Calcula el precio final tras restar el descuento.
    Devuelve un float (dinero).
    """
    ahorro = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - ahorro
    return precio_final  # <--- ¡Aquí está la magia! Devolvemos el dato.

def calcular_impuesto(precio_limpio, tasa_impuesto):
    """
    Añade el impuesto al precio dado.
    """
    total = precio_limpio * (1 + tasa_impuesto)
    return total

# --- FLUJO DE TRABAJO (PIPELINE) ---

# 1. Tenemos unos zapatos de 100 euros
precio_base = 100

# 2. Estamos en rebajas: 20% de descuento
# Capturamos el retorno en una variable 'precio_rebajado'
precio_rebajado = aplicar_descuento(precio_base, 50)

# 3. Al pasar por caja, hay que sumar el IVA (21%)
# Usamos el dato que nos dio la función anterior
precio_final_pagar = calcular_impuesto(precio_rebajado, 0.21)

print(f"Precio Original: {precio_base} €")
print(f"Precio con Descuento: {precio_rebajado} €")
print(f"Total en Caja (con IVA): {precio_final_pagar:.2f} €")