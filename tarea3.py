class Libro:
   def __init__ (self, titulo, autor, genero, puntuacion):
      self.titulo = titulo
      self.autor = autor
      self.genero = genero
      self.puntuacion = puntuacion
      
lista_libros = []

def agregarLibros():
   titulo = input("Ingresar título: ")
   autor = input("Ingresar autor: ")
   genero = input("Ingresar género: ")
   puntuacion = float(input("Ingresar puntuación: "))
   
   nuevo_libro = Libro(titulo, autor, genero, puntuacion)
   
   lista_libros.append(nuevo_libro)

def buscarLibrosGenero():
   genero = input("¿Qué género busca? ")
   print("Libros del género ", genero, ":")
   for libro in lista_libros:
      if libro.genero == genero:
         print(libro.titulo)

def recomendarLibro():
   genero = input("Ingresar género de interés: ")
   max_puntuacion = 0
   libro_recomendado = None
   for libro in lista_libros:
      if libro.genero == genero and libro.puntuacion > max_puntuacion:
         max_puntuacion = libro.puntuacion
         libro_recomendado = libro
      if libro_recomendado:
         print("Libro recomendado:", libro_recomendado.titulo)
      else:
         print("No hay libros recomendados para ese género.")

while True:
    print("Opciones:")
    print("1. Agregar Libro")
    print("2. Buscar Libros por Género")
    print("3. Recomendar Libro")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
       agregarLibros()
   
    elif opcion == "2":
       buscarLibrosGenero()

    elif opcion == "3":
       recomendarLibro()

    elif opcion == "4":
        break

    else:
        print("Opción no válida. Intente de nuevo.")

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)
libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", 4.3)
libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)
libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)
libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)
libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)
libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)

