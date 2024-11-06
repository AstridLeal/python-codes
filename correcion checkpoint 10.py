productos = [
    {
        "sku": 1,
        "producto": "Coca Cola",
        "precio": 15
    },
    {
        "sku": 2,
        "producto": "Pepsi",
        "precio": 15
    }
]

def imprimir_productos(productos):
    for producto in productos:
        print(f"SKU: {producto['sku']} | Nombre: {producto['producto']} | Precio: ${producto['precio']}")
        
imprimir_productos(productos)     