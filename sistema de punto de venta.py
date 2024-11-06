productos = [
    {
        "sku": 1,
        "producto": "Coca Cola",
        "precio": 15
    },
    {
        "sku": 2,
        "producto": "Gansito",
        "precio": 20
    },
    {
        "sku": 3,
        "producto": "Paketaxo",
        "precio": 60
    },
]

def imprimir_productos(productos):
    for producto in productos:
        print(f"SKU: {producto['sku']} | Nombre: {producto['producto']} | Precio: ${producto['precio']}")

def mostrar_menu():
    for i in range(3):
        print("==============================================================================================")
    print("===========================Bienvenido a Abarrotes \"El Hybridge\"===============================")
    for i in range(3):
        print("==============================================================================================")
    print("\t\t Menú de opciones")
    print("1) Punto de venta")
    print("2) Mostrar productos")
    print("3) Agregar producto")
    print("4) Modificar producto")
    print("5) Eliminar producto")
    print("6) Salir")
    print("==============================================================================================")


def buscar_producto(productos, sku):
    for producto in productos:
        if producto['sku'] == sku:
            return producto
    return None

def punto_de_venta(productos):
    total = 0
    carrito = []
    print("Punto de venta")
    while True:
        imprimir_productos(productos)
        sku = int(input("Ingrese el SKU del producto que desea agregar al carrito (0 para terminar): "))
        if sku == 0:
            break
        cantidad = int(input(f"Ingrese la cantidad que desea agregar al carrito: "))
        producto = buscar_producto(productos, sku)
        if producto:
            subtotal = producto['precio'] * cantidad
            print(f"Agregado: {producto['producto']} | Cantidad: {cantidad} | Subtotal: ${subtotal}")
            total += subtotal
            carrito.append({"producto": producto, "cantidad": cantidad, "subtotal": subtotal})
        else:
            print("El SKU ingresado no corresponde a ningún producto.")
    print(f"Total a pagar: ${total}")
    return carrito

def agregar_producto(productos):
    sku = len(productos) + 1
    nombre = input("Ingrese el nombre del nuevo producto: ")
    precio = float(input("Ingrese el precio del nuevo producto: "))
    productos.append({"sku": sku, "producto": nombre, "precio": precio})
    print("Producto agregado exitosamente.")

def modificar_producto(productos):
    imprimir_productos(productos)
    sku = int(input("Ingrese el SKU del producto que desea modificar: "))
    producto = buscar_producto(productos, sku)
    if producto:
        print(f"Producto actual: {producto['producto']} | Precio actual: ${producto['precio']}")
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
        producto['producto'] = nuevo_nombre
        producto['precio'] = nuevo_precio
        print("Producto modificado exitosamente.")
    else:
        print("El SKU ingresado no corresponde a ningún producto.")

def eliminar_producto(productos):
    imprimir_productos(productos)
    sku = int(input("Ingrese el SKU del producto que desea eliminar: "))
    for producto in productos:
        if producto['sku'] == sku:
            productos.remove(producto)
            print("Producto eliminado exitosamente.")
            return
    print("El SKU ingresado no corresponde a ningún producto.")

opc = 0        
while opc != 6:
    mostrar_menu()
    opc = int(input("Opción: "))
    if opc == 1:
        punto_de_venta(productos)
    elif opc == 2:
        imprimir_productos(productos)
    elif opc == 3:
        agregar_producto(productos)
    elif opc == 4:
        modificar_producto(productos)
    elif opc == 5:
        eliminar_producto(productos)
