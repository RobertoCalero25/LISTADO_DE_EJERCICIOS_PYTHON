class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}"

class Catalogo:
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        print(f"Producto {producto.nombre} agregado al catálogo.")

    def mostrar_catalogo(self):
        if not self.lista_productos:
            print("El catálogo está vacío.")
        else:
            print("Catálogo de productos:")
            for producto in self.lista_productos:
                print(producto)

if __name__ == "__main__":
    producto1 = Producto(codigo="001", nombre="Liquido de frenos", precio=30.00)
    producto2 = Producto(codigo="002", nombre="Refrigerante", precio=60.00)
    producto3 = Producto(codigo="003", nombre="Transmision", precio=140.00)

   
    catalogo = Catalogo()


    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)


    catalogo.mostrar_catalogo()
