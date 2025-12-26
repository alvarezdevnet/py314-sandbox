# Definición de Variables
# Usamos strings para texto y enteros (int) para dinero.
nombre_entrante = "Sopa de calabaza"
precio_entrante = 13  # <--- Número puro, sin comillas

nombre_principal = "Filete de ternera con guarnición"
precio_principal = 28 # <--- Número puro

nombre_postre = "Tarta de queso"
precio_postre = 10    # <--- Número puro


total_cuenta = precio_entrante + precio_principal + precio_postre
tasa_iva = 0.21 # 21% de IVA
iva = total_cuenta * tasa_iva
total_con_iva = total_cuenta + iva

# Salida por Pantalla
print("Menú del Día - Restaurante Pepe\n")

print("-- Entrante --")
print(f"{nombre_entrante}: {precio_entrante} €")

print("\n-- Plato Principal --")
print(f"{nombre_principal}: {precio_principal} €")

print("\n-- Postre --")
print(f"{nombre_postre}: {precio_postre} €")

print("------------------------------")
print(f"Subtotal: {total_cuenta:.2f} €")     # Forzamos 2 decimales siempre
print(f"IVA ({int(tasa_iva*100)}%): {iva:.2f} €")  # Redondeo visual automático
print(f"TOTAL A PAGAR: {total_con_iva:.2f} €")    # Redondeo visual automático