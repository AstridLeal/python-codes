productos = [
    {
        "sku": 1,
        "nombre": "Coca Cola",
        "precio": 15
    },
    {
        "sku": 2,
        "nombre": "Gansito",
        "precio": 20
    },
    {
        "sku": 3,
        "nombre": "Paketaxo",
        "precio": 60
    },
]

def buscar_producto(sku):
    for producto in productos:
        if producto['sku'] == sku:
            return producto
    return None

sku_buscado = int(input("Introduce un número de SKU: "))
producto_encontrado = buscar_producto(sku_buscado)
if producto_encontrado:
    print(f"Se encontró el producto con SKU {sku_buscado}: {producto_encontrado['nombre']}")
else:
    print(f"No se encontró ningún producto con SKU {sku_buscado}")