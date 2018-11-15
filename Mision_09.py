#Sebastian Macias I - A01376492
#Uso de listas  para resolución de tareas


def extraerPares(lista): #Obtiene lso números pares de la lista

    listaPares = [] #Crea una lista vacía donde se alijarán los pares

    for dato in range(0, len(lista)): #Visica cada valor de la lista
        if lista[dato] % 2 == 0: #Si el residuo da 0, es par
            listaPares.append(lista[dato]) #Si es correcto, el valor se agrega a la nueva lista

    return listaPares   # Regresa la lista nueva


def extraerMayoresPrevio(lista):  #Compara los valores para analizar el mayor por pareja

    listaMayorPrevio = []   #Crea  una lista nueva donde se guardarán los archivos

    for num in range(1, len(lista)):   #checa los valores de la lista otorgada
        if lista[num] > lista[num-1]: #Verifica que el valor anterior sea menor al que se checa
            listaMayorPrevio.append(lista[num]) #si es así, se agrega a la lista nueva

    return listaMayorPrevio   #La lista regresa


def intercambiarParejas(lista):

    listaNumIntercambados=[]

    for k in range(1, len(lista), 2): #Si el numero del elemento es par se agrega a la lista
        listaNumIntercambados.append(lista[k])     #se agrega a la lista nueva
        listaNumIntercambados.append(lista[k-1])   # se agrega el número anterior a la lista
    if len(lista) % 2 != 0:   #Checa si la lista i la lista es impar
        ultimo = len(lista)-1
        listaNumIntercambados.append(lista[ultimo])   #Se agrega el último valor a la lista nueva

    return listaNumIntercambados #Regresa la nueva lista


def intercambiarMM(lista):

    x = 0

    for k in range(0, len(lista)): #rango de posiciones en la lista
        if lista[k] == max(lista):  # Te da la posición del número mayor
            x = lista[k]
            lista[k] = min(lista)  # Te da la posición del número menor
    for k2 in range(0, len(lista)):
        if lista[k2] == min(lista):
            lista[k2] = x  # Cambiar la posicion
            break

    return lista  #Regresa la lista modificada


def promediarCentro(lista):

    ValorMax = 0
    ValorMin = 0
    listaModificable = []    #Creo una nueva lista para modificar
    listaModificable = lista       #Igualo los valores de la lista original a la nueva

    for k in range(0, len(listaModificable)):  #Visita cada casilla
        if lista[k] == max(listaModificable):    #Busca el valor mayor en la lista
            ValorMax = k     #Guarda el valor de la posición del número más grande
        if lista[k] == min(listaModificable):
            ValorMin = k       #Guarda el valor de la posición del número más chico

    if len(listaModificable) > 2:#El valor mayor y menor se iguala a cero y se elimina de la lista
        lista[ValorMax] = 0     #Igualo el valor a 0
        lista[ValorMin] = 0     #Igualo el valor a 0
        lista.remove(0)         #Elimino los valores
        promedio = sum(listaModificable) // len(listaModificable) #Saca el promedio. suma los valores de la nueva lista y lso divide entre su longitud
        return promedio   #Regresa el promedio
    else:
            return "0"     #Si no hay elementos para promediar o la longitud es menor o  igual a 2, regresa 0


def calcularEstadistica(lista):
    listaNueva = []   #Se crea una lista vacia
    if len(lista) >= 2: # se confirma que la lista tiene como mínimo 2 valores
        promedio = sum(lista)/len(lista)  #Se saca la media
        for x in range(0, len(lista)):   #Se usa un iterador para almacenar las sumas en una lista
            listaNueva.append((lista[x] - promedio)**2)  #Se agregan los valores a la lista
        desviacion = (sum(listaNueva) / (len(listaNueva) - 1))**(1/2)  #Se hace la formula de desviacíon estandar.
        return (promedio, desviacion)  #Se regresa la dupla
    if len(lista) == 1:  #Si la lista tiene un valor se saca el promedio
        promedio = sum(lista) / len(lista)
        return (promedio, 0)
    else:
        return (0,0) # si no se cumple ningúna condición, se regresa la dupla en ceros


def calcularSuma(lista):
    listaNueva = []
    for k in range(0, len(lista)): #Se hace un ciclo for por ver lso elementos de la lista
        if lista[k] == 13: #Verifica si existe el 13 dentro de la lista
            listaNueva.append(k) #Almaciena la posición
    if len(listaNueva) >= 1:
        for p in range(0, len(listaNueva)):#Si la lista creada encontro el 13 elimina sus valores proximos.
            #Pone los valores de 13 y los de a lado en cero para que no se cuenten en la suma
            lista[listaNueva[p]] = 0
            lista[listaNueva[p]-1] = 0
            lista[listaNueva[p]+1] = 0
        return sum(lista) #Regresa la lista ya con suma

    if len(listaNueva) == 0:#Si nunca hubo 13 entonces regresa la suma de la lista
        return sum(lista)
