def es_no_vacio(dato):
    return len(dato.strip()) > 0

def es_clasificacion_valida(clasificacion):
    return clasificacion.upper() in ['E', 'T', 'M']

def es_entero_positivo(valor):
    try:
        return int(valor) > 0
    except ValueError:
        return False

def es_entero_no_negativo(valor):
    try:
        return int(valor) >= 0
    except ValueError:
        return False

def buscar_codigo(codigo, juegos):
    return codigo.upper() in [c.upper() for c in juegos.keys()]

def stock_plataforma(plataforma, juegos, inventario):
    total = 0
    for cod, datos in juegos.items():
        if datos[1].lower() == plataforma.lower():
            total += inventario[cod][1]
    print(f"El total de stock disponible es: {total}")

def busqueda_precio(p_min, p_max, juegos, inventario):
    encontrados = []
    for cod, inv in inventario.items():
        precio, stock = inv
        if p_min <= precio <= p_max and stock > 0:
            titulo = juegos[cod][0]
            encontrados.append(f"{titulo}--{cod}")
    
    if not encontrados:
        print("No hay juegos en ese rango de precios.")
    else:
        encontrados.sort()
        print(f"Los juegos encontrados son: {encontrados}")

def actualizar_precio(codigo, nuevo_precio, inventario):
    if buscar_codigo(codigo, inventario):
        for c in inventario.keys():
            if c.upper() == codigo.upper():
                inventario[c][0] = nuevo_precio
                return True
    return False

def agregar_juego(c, t, p, g, cl, m, e, pr, st, juegos, inventario):
    if buscar_codigo(c, juegos):
        return False
    juegos[c.upper()] = [t, p, g, cl.upper(), m, e]
    inventario[c.upper()] = [pr, st]
    return True

def eliminar_juego(codigo, juegos, inventario):
    if buscar_codigo(codigo, juegos):
        for c in list(juegos.keys()):
            if c.upper() == codigo.upper():
                del juegos[c]
                del inventario[c]
                return True
    return False

def leer_opcion():
    try:
        op = int(input("Ingrese opción: "))
        if 1 <= op <= 6:
            return op
    except ValueError:
        pass
    print("Debe seleccionar una opción válida")
    return None

def main():
    juegos = {
        'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
        'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'Bright Works'],
        'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames']
    }
    inventario = {
        'G001': [9990, 7],
        'G002': [19990, 0],
        'G003': [42990, 3]
    }

    while True:
        print("\n==== MENÚ PRINCIPAL ====")
        print("1. Stock por plataforma\n2. Búsqueda de juegos por rango de precio\n3. Actualizar precio de juego\n4. Agregar juego\n5. Eliminar juego\n6. Salir")
        opcion = leer_opcion()

        if opcion == 1:
            plat = input("Ingrese plataforma a consultar: ")
            stock_plataforma(plat, juegos, inventario)
        
        elif opcion == 2:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                busqueda_precio(p_min, p_max, juegos, inventario)
            except ValueError:
                print("Debe ingresar valores enteros")
        
        elif opcion == 3:
            while True:
                cod = input("Ingrese código del juego: ")
                precio = int(input("Ingrese nuevo precio: "))
                if actualizar_precio(cod, precio, inventario):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                if input("¿Desea actualizar otro precio (s/n)?: ").lower() != 's':
                    break
        
        elif opcion == 4:
            cod = input("Código: ")
            if not buscar_codigo(cod, juegos):
                titulo = input("Título: ")
                plat = input("Plataforma: ")
                gen = input("Género: ")
                clas = input("Clasificación (E, T, M): ")
                mult = input("¿Es multiplayer? (s/n): ").lower() == 's'
                edit = input("Editor: ")
                precio = int(input("Precio: "))
                stock = int(input("Stock: "))
                if agregar_juego(cod, titulo, plat, gen, clas, mult, edit, precio, stock, juegos, inventario):
                    print("Juego agregado")
            else:
                print("El código ya existe")
        
        elif opcion == 5:
            cod = input("Ingrese código a eliminar: ")
            if eliminar_juego(cod, juegos, inventario):
                print("Juego eliminado")
            else:
                print("El código no existe")
        
        elif opcion == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()


 
