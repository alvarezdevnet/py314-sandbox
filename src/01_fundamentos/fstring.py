# Practica de ftrings

nombre = "Ana"
edad = 28
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)
ciudad = "Madrid"
mensaje_con_ciudad = f"{mensaje} Vivo en {ciudad}."
print(mensaje_con_ciudad)
# Formateo de números con fstrings
pi = 3.14159
mensaje_pi = f"El valor de pi es aproximadamente {pi:.2f}." # Limitar a 2 decimales
print(mensaje_pi)   
mensaje_pi = f"El valor de pi es aproximadamente {pi:.4f}." # Limitar a 4 decimales
print(mensaje_pi)  
# Practica de fstrings con expresiones
base = 5
altura = 10
area = f"El área de un triángulo con base {base} y altura {altura} es {0.5 * base * altura}."
print(area) 
# Formateo de números grandes
poblacion = 47450795
# Formateo con separadores de miles
print(f"Población: {poblacion:,}")
# Resultado: Población: 47,450,795
nombre = "Ana"
edad = 20
 
# Alinear a la derecha con ancho de 10 caracteres
print(f"{nombre:>10} tiene {edad} años")
# Resultado:        Ana tiene 20 años
 
# Alinear a la izquierda
print(f"{nombre:<10} tiene {edad} años")
# Resultado: Ana        tiene 20 años
 
# Centrar
print(f"{nombre:^10} tiene {edad} años")
# Resultado:    Ana     tiene {edad} años