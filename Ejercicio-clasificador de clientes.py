Ejercicio-clasificador de clientes
nombre = input("Ingrese el nombre del cliente: ")

compras = float(input("Ingrese el total de compras anuales (Q): "))

if compras >= 50000:
    categoria = "VIP"
elif compras >= 20000:
    categoria = "Premium"
   elif compras >= 5000:
       categoria = "Regular"
else:
     categoria = "Basico"

print("\n--- Clasificacion del Cliente ---")
print(f"Cliente: {nombre}")
print(f"Compras anuales: Q{compras}")
print(f"Categoria: {categoria}") 