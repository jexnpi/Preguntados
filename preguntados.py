import pygame
from datos_preguntados import lista
from funciones_preguntados import *

pygame.init() #Se inicializa pygame
screen = pygame.display.set_mode([700, 700]) #Se crea una ventana
pygame.display.set_caption("Preguntados!")

#IMAGENES
#MENU
imagen_fondo = pygame.image.load("Parcial 2/imagenes/fondo.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (700, 700))
imagen_menu = pygame.image.load("Parcial 2/imagenes/personaje4.png")
imagen_menu = pygame.transform.scale(imagen_menu, (380,300))
#SCORE
imagen_fondo_puntaje = pygame.image.load("Parcial 2/imagenes/fondo_4.png")
imagen_personaje_puntaje = pygame.image.load("Parcial 2/imagenes/personaje3.png")
#PREGUNTAS
imagen_fondo_preguntas = pygame.image.load("Parcial 2/imagenes/fondo_5.png")
imagen_fondo_preguntas = pygame.transform.scale(imagen_fondo_preguntas, (700, 700))
#FINAL
imagen_final = pygame.image.load("Parcial 2/imagenes/personajes.png")


#BOTONES
#BOTONES MENU
boton_jugar = pygame.Rect(260, 200, 225,70)
boton_puntaje = pygame.Rect(400,100,225,70)
boton_salir = pygame.Rect(125,100,225,70)
#BOTONES PUNTAJE
boton_salir_menu_2 = pygame.Rect(580,630,100,40)
#BOTONES PREGUNTAS
boton_preguntas = pygame.Rect(85,30,240,70)
boton_reiniciar = pygame.Rect(405,30,240,70)
boton_salir_menu_3 = pygame.Rect(580,630,100,40)
boton_opcion_a = pygame.Rect(280,312,350,60)
boton_opcion_b = pygame.Rect(280,412,350,60)
boton_opcion_c = pygame.Rect(280,512,350,60)
#BOTONES USUARIO
boton_ingreso_usuario = pygame.Rect(180,615,350,60)
#BOTONES FINAL
boton_salir_menu = pygame.Rect(580,630,100,40)
#BOTON VOLUMEN
boton_volumen = pygame.Rect(35, 660, 80,30)

#FONTS
font = pygame.font.SysFont("Arial Narrow", 50)
font_2 = pygame.font.SysFont("Arial Narrow", 40)
font_3 = pygame.font.SysFont("Arial Narrow", 25)
fuente = pygame.font.SysFont("Arial Narrow", 60)
fuente_2 = pygame.font.SysFont("Arial Narrow", 30)
fuente_3 = pygame.font.SysFont("Arial Narrow", 20)
#TEXTO MENU
text_jugar = font.render("COMENZAR!", True, (255, 255, 255))
text_puntaje = font.render("Puntajes", True, (255, 255, 255))
text_salir = font.render("Salir", True, (255, 255, 255))
#TEXTO PUNTAJE
fuente_top_1 = pygame.font.SysFont("Arial Narrow", 70)
fuente_top_2 = pygame.font.SysFont("Arial Narrow", 50)
fuente_top_3 = pygame.font.SysFont("Arial Narrow", 30)
text_salir_menu_2 = fuente_2.render("Menu", True, (255, 255, 255))
#TEXTO PREGUNTAS
text_preguntas_2 = fuente.render("Preguntas", True, (255, 255, 255))
text_reiniciar_2 = fuente.render("Reiniciar", True, (255, 255, 255))
text_salir_menu_3 = fuente_2.render("Menu", True, (255, 255, 255))
texto_pregunta= font_3.render("", True, (255, 255, 255))
respuesta_a = font_2.render("", True, (255, 255, 255))
respuesta_b = font_2.render("", True, (255, 255, 255))
respuesta_c = font_2.render("", True, (255, 255, 255))
#TEXTO FINAL
text_agradecimiento = fuente.render("Gracias por jugar!", True, (255, 255, 255))
text_salir_menu = fuente_2.render("Menu", True, (255, 255, 255))
#TEXTO SONIDO
text_volumen = fuente_3.render("Sound: On", True, (255, 255, 255))


#SONIDOS
sonido_menu= pygame.mixer.Sound("Parcial 2/sonidos/sonido_menu.mp3")
sonido_preguntas = pygame.mixer.Sound("Parcial 2/sonidos/sonido_preguntas.mp3")
sonido_final = pygame.mixer.Sound("Parcial 2/sonidos/sonido_final.mp3")
sonido_puntaje = pygame.mixer.Sound("Parcial 2/sonidos/sonido_puntaje.mp3")
sonido_incorrecto = pygame.mixer.Sound("Parcial 2/sonidos/sonido_incorrecto.mp3")
sonido_correcto = pygame.mixer.Sound("Parcial 2/sonidos/sonido_correcto.mp3")
sonido_menu.set_volume (0.05)
sonido_preguntas.set_volume(0.05)
sonido_final.set_volume (0.03)
sonido_puntaje.set_volume (0.05)
sonido_incorrecto.set_volume(0.1)
sonido_correcto.set_volume(0.02)


esta_jugando = False
es_puntaje = False
juego_terminado = False
respuesta_incorrecta = False
es_menu = True
sonido = True
nombre_jugador = ""
ingresar_nombre = False
running = True
lista_jugador = cargar_archivo()
pregunta_indice = 0
intentos = 0
score = 0
sonido_menu.play(5)
while running:
   # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse down: {event.pos}") #Para imprimir posicion
            
            #MENU
            if es_menu == True:
#=====================================BOTON COMENZAR=============================================
                if boton_jugar.collidepoint(event.pos):
                    sonido_preguntas.play(5)
                    sonido_menu.stop()
                    esta_jugando = True
                    es_menu = False
                    pregunta_indice = 0
                    score = 0
                    respuesta_incorrecta = False
                    intentos = 0
                    pregunta = lista[pregunta_indice]
                    texto_pregunta = font_3.render(pregunta['pregunta'], True, (255, 255, 255))
                    respuesta_a = font_2.render(pregunta['a'], True, (255, 255, 255))
                    respuesta_b = font_2.render(pregunta['b'], True, (255, 255, 255))
                    respuesta_c = font_2.render(pregunta['c'], True, (255, 255, 255))

#===================================BOTON PUNTAJE==================================================
                if boton_puntaje.collidepoint(event.pos):
                    sonido_puntaje.play(5)
                    sonido_menu.stop()
                    es_puntaje = True
                    es_menu = False
                    print("Apreto puntaje")
                    ordenar_scores(lista_jugador,'score','DESC')

                    if len(lista_jugador) >= 3:
                        top_1 =lista_jugador[0]['nombre']
                        score_1 = lista_jugador[0]['score']
                        top_2 = lista_jugador[1]['nombre']
                        score_2 = lista_jugador[1]['score']
                        top_3 = lista_jugador[2]['nombre']
                        score_3 = lista_jugador[2]['score']
                        text_top1 = fuente_top_1.render(f"{top_1} - {score_1}", True, (255,255,255),(236, 213, 16))
                        text_top2 = fuente_top_2.render(f"{top_2} - {score_2}", True, (255,255,255),(191, 185, 202))
                        text_top3 = fuente_top_3.render(f"{top_3} - {score_3}", True, (255,255,255),(176, 97, 34 ))
                    elif len(lista_jugador) == 2:
                        top_1 =lista_jugador[0]['nombre']
                        score_1 = lista_jugador[0]['score']
                        top_2 = lista_jugador[1]['nombre']
                        score_2 = lista_jugador[1]['score']
                        text_top1 = fuente_top_1.render(f"{top_1} - {score_1}", True, (255,255,255), (236, 213, 16))
                        text_top2 = fuente_top_2.render(f"{top_2} - {score_2}", True, (255,255,255), (191, 185, 202))
                        text_top3 = fuente_top_3.render(f"", True, (255,255,255), (176, 97, 34 ))
                    elif len(lista_jugador) == 1:
                        top_1 =lista_jugador[0]['nombre']
                        score_1 = lista_jugador[0]['score']
                        text_top1 = fuente_top_1.render(f"{top_1} - {score_1}", True, (255,255,255), (236, 213, 16))
                        text_top2 = fuente_top_2.render(f"", True, (255,255,255),(191, 185, 202))
                        text_top3 = fuente_top_3.render(f"", True, (255,255,255), (176, 97, 34 ))
                    else:
                        text_top1 = fuente_top_1.render(f"", True, (255,255,255), (236, 213, 16))
                        text_top2 = fuente_top_2.render(f"", True, (255,255,255),(191, 185, 202))
                        text_top3 = fuente_top_3.render(f"", True, (255,255,255), (176, 97, 34 ))

#==============================BOTON SALIR DEL JUEGO================================================
                if boton_salir.collidepoint(event.pos):
                    running = False

#===============================BOTON SONIDO=======================================================
                if sonido == True:
                    if boton_volumen.collidepoint(event.pos):
                        text_volumen = fuente_3.render("Sound: Off", True, (255, 255, 255))
                        sonido_menu.set_volume (0)
                        sonido_preguntas.set_volume(0)
                        sonido_final.set_volume (0)
                        sonido_puntaje.set_volume (0)
                        sonido_incorrecto.set_volume(0)
                        sonido_correcto.set_volume(0)
                        sonido = False

                elif sonido == False:
                    if boton_volumen.collidepoint(event.pos):
                        text_volumen = fuente_3.render("Sound: On", True, (255, 255, 255))
                        sonido_menu.set_volume (0.05)
                        sonido_preguntas.set_volume(0.05)
                        sonido_final.set_volume (0.03)
                        sonido_puntaje.set_volume (0.05)
                        sonido_incorrecto.set_volume(0.1)
                        sonido_correcto.set_volume(0.02)
                        sonido = True
        
#==============================BOTONES DE LAS RESPUESTAS=========================================
            #APRETAR RESPUESTA A
            elif esta_jugando == True:
                if boton_opcion_a.collidepoint(event.pos):
                    print("Apreto la opcion a")
            
                    #CORRECTA A
                    if pregunta['correcta'] == 'a':
                        sonido_correcto.play()
                        print("Correcta a")
                        score += 10
            
                        if pregunta_indice < len(lista)-1:
                            pregunta_indice += 1
                            intentos = 0
                            pregunta = lista[pregunta_indice] 
                            texto_pregunta= font_3.render(pregunta['pregunta'], True, (255, 255, 255))
                            respuesta_a = font_2.render(pregunta['a'], True, (255, 255, 255))
                            respuesta_b = font_2.render(pregunta['b'], True, (255, 255, 255))
                            respuesta_c = font_2.render(pregunta['c'], True, (255, 255, 255))

                        else:
                            esta_jugando = False
                            juego_terminado = True
                            ingresar_nombre = True
                            sonido_preguntas.stop()
                            sonido_final.play()
                            print ("Fin")

                    #INCORRECTA A
                    else:
                        print("Respuesta incorrecta")
                        sonido_incorrecto.play()
                        respuesta_incorrecta = True
                        respuesta_a = font_2.render(pregunta['a'], True, (255, 206, 18))
                        intentos += 1
                        print(intentos)
                        if intentos == 2:
                            if pregunta_indice < len(lista)-1:
                                intentos = 0
                                pregunta_indice += 1
                                pregunta = lista[pregunta_indice]
                                texto_pregunta= font_3.render(pregunta['pregunta'], True, (255, 255, 255))
                                respuesta_a = font_2.render(pregunta['a'], True, (255, 255, 255))
                                respuesta_b = font_2.render(pregunta['b'], True, (255, 255, 255))
                                respuesta_c = font_2.render(pregunta['c'], True, (255, 255, 255))

                            else:
                                esta_jugando = False
                                juego_terminado = True
                                ingresar_nombre = True
                                sonido_preguntas.stop()
                                sonido_final.play()
                                print("Fin del juego")


                #APRETAR RESPUESTA B
                elif boton_opcion_b.collidepoint(event.pos):
                    print("Apreto la opcion b")

                    #CORRECTA B
                    if pregunta['correcta'] == 'b':
                        sonido_correcto.play()
                        print("Correcta b")
                        score += 10

                        if pregunta_indice < len(lista) - 1:
                            pregunta_indice += 1
                            intentos = 0
                            pregunta = lista[pregunta_indice]
                            texto_pregunta= font_3.render(pregunta['pregunta'], True, (255, 255, 255))
                            respuesta_a = font_2.render(pregunta['a'], True, (255, 255, 255))
                            respuesta_b = font_2.render(pregunta['b'], True, (255, 255, 255))
                            respuesta_c = font_2.render(pregunta['c'], True, (255, 255, 255))

                        else:
                            esta_jugando = False
                            juego_terminado = True
                            ingresar_nombre = True
                            sonido_preguntas.stop()
                            sonido_final.play()
                            print ("Fin")

                    #INCORRECTA B
                    else:
                        print("Respuesta incorrecta")
                        sonido_incorrecto.play()
                        respuesta_incorrecta = True
                        respuesta_b = font_2.render(pregunta['b'], True, (253, 18, 255))
                        intentos += 1
                        print(intentos)
                        if intentos == 2:
                            if pregunta_indice < len(lista)-1:
                                intentos = 0
                                pregunta_indice += 1
                                pregunta = lista[pregunta_indice]
                                texto_pregunta= font_3.render(pregunta['pregunta'], True, (255, 255, 255))
                                respuesta_a = font_2.render(pregunta['a'], True, (255, 255, 255))
                                respuesta_b = font_2.render(pregunta['b'], True, (255, 255, 255))
                                respuesta_c = font_2.render(pregunta['c'], True, (255, 255, 255))

                            else:
                                esta_jugando = False
                                juego_terminado = True
                                ingresar_nombre = True
                                sonido_preguntas.stop()
                                sonido_final.play()
                                print("Fin del juego")

                #APRETAR RESPUESTA C
                if boton_opcion_c.collidepoint(event.pos):
                    print("Apreto la opcion c")
                    
                    #CORRECTA C
                    if pregunta['correcta'] == 'c':
                        sonido_correcto.play()
                        score += 10
                        print("Correcta c")
                        
                        if pregunta_indice < len(lista) - 1:
                            pregunta_indice += 1
                            intentos = 0
                            pregunta = lista[pregunta_indice]
                            texto_pregunta= font_3.render(pregunta['pregunta'], True, (255, 255, 255))
                            respuesta_a = font_2.render(pregunta['a'], True, (255, 255, 255))
                            respuesta_b = font_2.render(pregunta['b'], True, (255, 255, 255))
                            respuesta_c = font_2.render(pregunta['c'], True, (255, 255, 255))

                        else:
                            esta_jugando = False
                            juego_terminado = True
                            ingresar_nombre = True
                            sonido_preguntas.stop()
                            sonido_final.play()
                            print("Fin del juego")
                    
                    #INCORRECTA C
                    else:
                        print("Respuesta incorrecta")
                        sonido_incorrecto.play()
                        respuesta_incorrecta = True
                        respuesta_c = font_2.render(pregunta['c'], True, (18, 255, 218))
                        intentos += 1
                        print(intentos)
                        if intentos == 2:
                            if pregunta_indice < len(lista)-1:
                                intentos = 0
                                pregunta_indice += 1
                                pregunta = lista[pregunta_indice]
                                texto_pregunta= font_3.render(pregunta['pregunta'], True, (255, 255, 255))
                                respuesta_a = font_2.render(pregunta['a'], True, (255, 255, 255))
                                respuesta_b = font_2.render(pregunta['b'], True, (255, 255, 255))
                                respuesta_c = font_2.render(pregunta['c'], True, (255, 255, 255))
                                
                            else:
                                esta_jugando = False
                                juego_terminado = True
                                ingresar_nombre = True
                                sonido_preguntas.stop()
                                sonido_final.play()
                                print("Fin del juego")

                #BOTON SALIR DE PREGUNTAS
                elif boton_salir_menu_3.collidepoint(event.pos):
                    sonido_preguntas.stop()
                    sonido_menu.play()
                    esta_jugando = False
                    es_menu = True
                    print("Apreto salir a menu")
            
                #BOTON PASAR A SIGUIENTE PREGUNTA
                elif boton_preguntas.collidepoint(event.pos):
                    if pregunta_indice < len(lista)-1:
                        intentos = 0
                        pregunta_indice += 1
                        pregunta = lista[pregunta_indice]
                        texto_pregunta= font_3.render(pregunta['pregunta'], True, (255, 255, 255))
                        respuesta_a = font_2.render(pregunta['a'], True, (255, 255, 255))
                        respuesta_b = font_2.render(pregunta['b'], True, (255, 255, 255))
                        respuesta_c = font_2.render(pregunta['c'], True, (255, 255, 255))

                    else:
                        print ("Fin")
                        sonido_preguntas.stop()
                        sonido_final.play()
                        esta_jugando = False
                        juego_terminado = True
                        ingresar_nombre = True

                #BOTON REINICIAR
                elif boton_reiniciar.collidepoint(event.pos):
                    print("Apreto reiniciar")
                    pregunta_indice = 0
                    score = 0
                    intentos = 0
                    esta_jugando = True
                    juego_terminado = False
                    ingresar_nombre = False
                    pregunta = lista[pregunta_indice]
                    texto_pregunta= font_3.render(pregunta['pregunta'], True, (255, 255, 255))
                    respuesta_a = font_2.render(pregunta['a'], True, (255, 255, 255))
                    respuesta_b = font_2.render(pregunta['b'], True, (255, 255, 255))
                    respuesta_c = font_2.render(pregunta['c'], True, (255, 255, 255))

#===============================BOTON SALIR DE PUNTAJE============================================
            if boton_salir_menu_2.collidepoint(event.pos):
                sonido_puntaje.stop()
                sonido_menu.play(5)
                es_puntaje = False
                es_menu = True

#===============================PANTALLA FINAL===================================================
            if juego_terminado == True:
                if boton_salir_menu.collidepoint(event.pos):
                    sonido_final.stop()
                    juego_terminado = False
                    es_menu = True
                    print("Apreto salir a menu")
                if boton_ingreso_usuario.collidepoint(event.pos):
                    ingresar_nombre = True

#==============================INGRESO USUARIO =================================================
        if event.type == pygame.KEYDOWN and ingresar_nombre == True:
            if event.key == pygame.K_BACKSPACE: #Borra el ultimo caracter ingresado
                nombre_jugador = nombre_jugador[:-1]
            elif event.key == pygame.K_RETURN: #Ingresa el nombre con enter
                sonido_final.stop()
                sonido_menu.play(5)
                lista_jugador = guardar_jugadores(lista_jugador,nombre_jugador,score)
                guardar_json (lista_jugador)
                ingresar_nombre = False
                es_menu = True
                juego_terminado = False
                print(f"Nombre: {nombre_jugador} con puntaje {score}")
                nombre_jugador = ""
            else:
                nombre_jugador += event.unicode #Captura los caracteres que son ingresados por teclado

    #MENU
    if es_menu == True:
        screen.blit(imagen_fondo,(0,0))
        screen.blit(imagen_menu,(170,360))
        pygame.draw.rect(screen, (217, 27, 27), boton_jugar, border_radius=13)
        pygame.draw.rect(screen, (217, 27, 27), boton_puntaje, border_radius=13)
        pygame.draw.rect(screen, (217, 27, 27), boton_salir, border_radius=15)
        screen.blit(text_jugar, (265, 223))
        screen.blit(text_puntaje, (440, 120))    
        screen.blit(text_salir, (190, 120))
        pygame.draw.rect(screen, (27, 52, 234), boton_volumen, border_radius=20)
        screen.blit(text_volumen, (42, 668))

    #PREGUNTAS
    elif esta_jugando == True:
        screen.blit(imagen_fondo_preguntas, (0,0))
        pygame.draw.rect(screen, (173, 9, 211), boton_preguntas, border_radius=13)
        pygame.draw.rect(screen, (173, 9, 211), boton_reiniciar, border_radius=13)
        pygame.draw.rect(screen, (202, 0, 0), boton_salir_menu_3, border_radius=20)
        pygame.draw.rect(screen, (255, 206, 18), boton_opcion_a, border_radius=5)
        pygame.draw.rect(screen, (253, 18, 255), boton_opcion_b, border_radius=5)
        pygame.draw.rect(screen, (18, 255, 218), boton_opcion_c, border_radius=5)
        pygame.draw.rect(screen, (0,13,212), (85,175,560,70) , border_radius=5) 
        screen.blit(text_preguntas_2, (105,45))
        screen.blit(text_reiniciar_2, (440,45))    
        screen.blit(text_salir_menu_3, (603,640))       
        screen.blit(texto_pregunta, (100, 200))
        screen.blit(respuesta_a, (290, 330))
        screen.blit(respuesta_b, (290, 430))
        screen.blit(respuesta_c, (290, 530))
        text_score = font_3.render (f"Score: {score}", True, (255, 255, 255) )
        screen.blit(text_score, (5,5))
        if respuesta_incorrecta == True:
            screen.blit(respuesta_a, (290, 330))
            screen.blit(respuesta_b, (290, 430))
            screen.blit(respuesta_c, (290, 530))

    #PUNTAJE
    elif es_puntaje == True: 
        screen.blit(imagen_fondo_puntaje,(0,0))
        screen.blit(imagen_personaje_puntaje,(460,492))
        pygame.draw.rect(screen, (202, 0, 0), boton_salir_menu_2, border_radius=20)
        screen.blit(text_salir_menu_2, (603,640))
        screen.blit(text_top1, (240,245))
        screen.blit(text_top2, (100,385))
        screen.blit(text_top3, (450,420))

    #FIN   
    elif juego_terminado == True:
        screen.fill((237,53,12))
        screen.blit(imagen_final, (90,100))
        pygame.draw.rect(screen, (0, 0, 0), boton_ingreso_usuario, border_radius=20)
        pygame.draw.rect(screen, (202, 0, 0), boton_salir_menu_3, border_radius=20)
        screen.blit(text_salir_menu, (603,640))
        screen.blit(text_agradecimiento, (190,60))
        text_score_final = fuente_2.render(f"Tu score es: {score}", True,(255, 255, 255))
        screen.blit(text_score_final,(280,580))
        ingresar_nombre = True
        text_ingresar_nombre = font_3.render ("Ingrese su nombre: ", True, (255, 255, 255) )
        text_nombre = font_2.render (nombre_jugador,True,(255, 255, 255))
        screen.blit(text_ingresar_nombre, (200, 624))
        screen.blit(text_nombre, (275, 645))

    pygame.display.flip()# Muestra los cambios en  la pantalla

pygame.quit() # Fin

