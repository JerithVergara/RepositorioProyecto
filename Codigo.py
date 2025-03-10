cantidad = int(input("Por favor ingrese la cantidad de piezas a comprar "))
valor_unitario = float(input("Por favor ingrese el valor unitario de cada pieza "))
total = (cantidad*valor_unitario)

if total>500000:
    inversion = (total*0.55)
    prestamo = (total*0.30)
    credito = (total*0.15)
else:
    inversion = (total*0.70)
    prestamo = 0
    credito = (total*0.30)

interes = (credito*0.20)
totalcredito = (credito+interes)

print(f"Resultados de los calculos:")
print(f"Esta es la cantidad de las piezas a comprar: {cantidad}")
print(f"Este es el precio unitario de cada pieza: ${valor_unitario:.2f}")
print(f"El monto total de la compra es de: ${total:.2f}")
print(f"La inversión de la empresa es de: ${inversion:.2f}")
print(f"El préstamo al banco es de: ${prestamo:.2f}")
print(f"El crédito al fabricante con interés es de: ${totalcredito:.2f}")