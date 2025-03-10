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