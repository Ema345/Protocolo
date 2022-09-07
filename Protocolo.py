print("Bienvenido a un programa para realizar protocolos, este programa no acepta sub numeros")
print('-------------------------------------------------')
longitud = int(input("¿Cuantos elementos desea que contenga su Protocolo?"))
protocolo = []
i = 0

    
while i < longitud:
    proto = input("Ingrese un requerimiento para su protocolo:  ")
    protocolo.append(proto)  
    i = i + 1

print("El listado del protocolo es: ")
#se imprime el contenido de la lista
for j in range (0,len(protocolo)):
    print(str(j+1), ".- " + protocolo[j])
        
        
opc = 0
    
    #-----------------------------------------
    
#inicia el while con los datos que ingresa el usuario
while True:
    print("Menú:")
    print ("------------------------------------------------------")
    print ("Seleccione la opción que quiera realizar: ")
    print ("1. Conocer el numero de requerimientos del protocolo")
    print ("2. Añadir un elemento")
    print ("3. Eliminar elemento por indice")
    print ("4. Salir del programa")
    print ("------------------------------------------------------")

    opc = int(input("Opcion: "))

    if opc == 1:
        longitudes = len(protocolo)
        print("La cantidad de requerimientos del protocolo es: " + str(longitudes))
        print("y son: ")
        for j in range (0,(len(protocolo))):
           print(str(j+1)+".- "+protocolo[j])
        
        
        
    elif opc == 2:
        print("El nuevo elemento que se agregará al final de los ya existentes")
        nuevo= input("Escribe el nuevo requerimiento que deseas agregar:  ")
        protocolo.append(nuevo)
        print(" ")
        for j in range (0,(len(protocolo))):
            print(str(j+1)+".- "+protocolo[j])      

    elif opc== 3:
        posicion=int (input("Escribe la posicion del elemento que deseas eiminar:  "))
        protocolo.pop(posicion-1)
        print("")
        for j in range (0,(len(protocolo))):
           print(str(j+1)+".- "+protocolo[j])
           

    elif opc == 4:
        #fin del while
        print("Hasta luego")
        break

