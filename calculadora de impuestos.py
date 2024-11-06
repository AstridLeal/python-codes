def calcular_impuesto(monto_total, porcentaje_impuesto):
  monto_impuesto = monto_total * porcentaje_impuesto
  monto_total_pagar = monto_total + monto_impuesto
  return monto_impuesto, monto_total_pagar

monto_total = float(input("Introduce el monto total de la compra: "))
porcentaje_impuesto = float(input("Introduce el porcentaje de impuesto: "))
porcentaje_impuesto = porcentaje_impuesto/100
monto_impuesto, monto_total_pagar = calcular_impuesto(monto_total, porcentaje_impuesto)

print(f"Subtotal: ${monto_total:.2f}")
print(f"Impuesto: {porcentaje_impuesto:.2%}")
print(f"Monto del impuesto: ${monto_impuesto:.2f}")
print(f"Monto total a pagar: ${monto_total_pagar:.2f}")
