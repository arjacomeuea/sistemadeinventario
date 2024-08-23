import os

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo_inventario="inventario.txt"):
        self.archivo_inventario = archivo_inventario
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        if os.path.exists(self.archivo_inventario):
            try:
                with open(self.archivo_inventario, "r") as archivo:
                    for linea in archivo:
                        if linea.strip():  # Ignorar líneas en blanco
                            codigo, nombre, cantidad, precio = linea.strip().split(",")
                            self.productos[codigo] = Producto(codigo, nombre, int(cantidad), float(precio))
            except FileNotFoundError:
                print(f"Error: No se encontró el archivo {self.archivo_inventario}.")
            except PermissionError:
                print(f"Error: No tienes permisos para leer el archivo {self.archivo_inventario}.")
            except Exception as e:
                print(f"Ocurrió un error inesperado al cargar el inventario: {e}")
        else:
            print(f"El archivo {self.archivo_inventario} no existe. Se creará al añadir productos.")

    def guardar_inventario(self):
        try:
            with open(self.archivo_inventario, "w") as archivo:
                for producto in self.productos.values():
                    archivo.write(str(producto) + "\n")
        except PermissionError:
            print(f"Error: No tienes permisos para escribir en el archivo {self.archivo_inventario}.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        if codigo in self.productos:
            print(f"Error: El producto con código {codigo} ya existe.")
        else:
            self.productos[codigo] = Producto(codigo, nombre, cantidad, precio)
            self.guardar_inventario()
            print(f"Producto '{nombre}' agregado exitosamente.")

    def actualizar_producto(self, codigo, cantidad=None, precio=None):
        if codigo in self.productos:
            producto = self.productos[codigo]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' actualizado exitosamente.")
        else:
            print(f"Error: No se encontró un producto con código {codigo}.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            nombre = self.productos[codigo].nombre
            del self.productos[codigo]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print(f"Error: No se encontró un producto con código {codigo}.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario:")
            for producto in self.productos.values():
                print(f"Código: {producto.codigo} | Nombre: {producto.nombre} | Cantidad: {producto.cantidad} | Precio: {producto.precio}")

def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            inventario.mostrar_inventario()
        elif opcion == "2":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(codigo, nombre, cantidad, precio)
        elif opcion == "3":
            codigo = input("Código del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no actualizar): ")
            precio = input("Nuevo precio (dejar en blanco para no actualizar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(codigo, cantidad, precio)
        elif opcion == "4":
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
