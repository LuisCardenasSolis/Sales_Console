import sys
import os
import re


def registro():
    codigo = input("Ingrese el codigo del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Precio Actual: "))
    unidades = int(input("Unidades Adqueridas: "))

    total = precio*unidades

    return codigo+" "+nombre+" "+str(precio)+" "+str(unidades)+" | Total: "+str(total)+"\n"

while True:
    
    print("""
     -----------------MENU------------------
    |    1. Registrar Ventas                |
    |    2. Imprimir Ventas                 |
    |    3. Buscar Ventas                   |
    |    4. Eliminar Ventas                 |
    |    5. Actualizar Ventas               |
    |    6. Imprimir monto total de Ventas  |
    |    7. Listado de Ventas               |
    |    8. Ordenar Ventas                  |
    |    9. Salir                           |
     ---------------------------------------
    """)
    opcion = int(input("Escoga una opcion:"))

    if opcion == 1:
        os.system('cls')
        row_data=registro()
        file = open("registro.txt", "a+")
        file.write(row_data)
        file.close()
        print("Datos agregados exitosamente")

        nuevo_registro=input("Desea insertar otro registro?(s/n)")

        while nuevo_registro == "s":
            os.system('cls')
            row_data=registro()
            file = open("registro.txt", "a+")
            file.write(row_data)
            file.close()
            print("Datos agregados exitosamente \n")
            print("")
            nuevo_registro = input("Desea insertar otro registro?(s/n): ")
           
    elif opcion == 2:
        os.system('cls')
        print("Codigo Nombre Precio Cantidad Total")
        open_file = open("registro.txt","r")
        for linea in open_file.readlines():
            print(linea)
        open_file.close()
        print("<---------------END----------------->")

    elif opcion == 3:
        os.system('cls')
        busqueda=input("Ingrese el codigo que quisiera encontrar: ")
        with open("registro.txt", "r") as file:
            for line in file:
                palabra = re.match(busqueda, line)
                if palabra:
                    print(line)

    elif opcion == 4:
        os.system('cls')
        dato_eliminar = input("Ingrese el codigo del dato que quisiera eliminar: ")

        f = open("registro.txt","r")
        lineas = f.readlines()
        f.close()

        with open("registro.txt", "r") as file:
            for line in file:
                palabra = re.match(dato_eliminar, line)

                if palabra:
                    valor=line
                    

        file = open("registro.txt", "w")
        for linea in lineas:
                
            if linea != valor:                
                file.write(linea)
        
        file.close()
        print("<---------------Datos Eliminados----------------->")

    elif opcion == 5:
        os.system('cls')
        r = input("codigo de la venta a actualizar: ")
        
        f = open("registro.txt","r")
        lineas = f.readlines()
        f.close()

        with open("registro.txt", "r") as file:
            for line in file:
                palabra = re.match(r, line)

                if palabra:
                    valor=line
                    print(line)
                    print("------------------------")
                    a=input("nuevo Codigo: ")
                    b=input("Nombre: ")
                    c=int(input("Precio: "))
                    d=int(input("Cantidad: "))
                    m=c*d
                    actualizado=a+" "+b+" "+str(c)+" "+str(d)+" | Total: "+str(m)+"\n"
        
        file = open("registro.txt", "w")
        for linea in lineas:  
            if linea != valor:                
                file.write(linea)

        file.close()

        fi = open("registro.txt", "a+")
        fi.write(actualizado)
        fi.close()
        


    elif opcion == 6:
        os.system('cls')
        #el monto total esta ahi asi que la mismo que la opcion 2 seeria, sino que recorta con una funcion
        # cadena = "Total: 123"
        # print cadena.lstrip("Total:")
        # en consola saldria: 123
        #terminalo , algo asi es la idea, busca una funcion asi
     
        open_file = open("registro.txt","r")
        for linea in open_file.readlines():
            lin = linea
            print(lin.lstrip("| "))
        open_file.close()
        print("<---------------END----------------->")
    elif opcion == 7:
        os.system('cls')
    elif opcion == 8:
        os.system('cls')


    elif opcion == 9:
        os.system('cls')
        sys.exit() 
    else:
        os.system('cls')
        print(">>>>>Reintente de nuevo<<<<<")
        print("<---------------END----------------->")
