class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        pais, lote, ano = self.obtener_datos_codigo()
        return f"Producto: {self.nombre}, Código: {self.codigo}, País de origen: {pais}, Número de lote: {lote}, Año: {ano}"

    def obtener_datos_codigo(self):
        partes_codigo = self.codigo.split('-')
        if len(partes_codigo) == 3:
            pais, lote, ano = partes_codigo
            return pais, lote, ano
        else:
            return "Desconocido", "Desconocido", "Desconocido"

if __name__ == "__main__":
    
    producto = Producto(nombre="Esparragos", codigo="PERU-00001-2024")

    
    print(producto)
