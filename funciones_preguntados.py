import json

def cargar_archivo():
    '''
    Abre un archivo JSON y carga su contenido
    Retorna una lista de diccionarios que fue extraida del archivo
    '''
    with open ("Parcial 2/data_usuarios.json","r") as archivo: 
        datos = json.load(archivo)
        lista_jugador = datos['puntaje'] 
        
    return lista_jugador

def guardar_json(lista):
    '''
    Guarda los datos en el archivo JSON
    '''
    with open("Parcial 2/data_usuarios.json", "w") as archivo:
        json.dump({'puntaje': lista}, archivo, indent=4)


def guardar_jugadores (lista:list, nombre_jugador:str,score:int):
    '''
    Guarda/agrega los jugadores junto a sus scores en el archivo JSON
    '''
    lista.append({'nombre':nombre_jugador, 'score':score})
    return lista


def ordenar_scores (puntaje:list,score:str ,criterio: str):
    '''
    Ordena los jugadores por su score en orden ascendente o descendente segun el criterio pedido (en este caso ascendente)
    Recibe una lista de diccionarios y dos strings en donde score es la clave del diccionario por la cual se quiere ordenar y criterio el orden en que se lo pide
    '''
    for i in range(len(puntaje)-1):
        for j in range (i+1, len(puntaje)):
            if criterio == "ASC" and puntaje[i][score] > puntaje[j][score]: 
                auxiliar= puntaje[i] 
                puntaje[i]= puntaje[j] 
                puntaje[j] = auxiliar
            elif criterio == "DESC" and puntaje[i][score] < puntaje[j][score]: 
                auxiliar= puntaje[i] 
                puntaje[i]= puntaje[j] 
                puntaje[j] = auxiliar

