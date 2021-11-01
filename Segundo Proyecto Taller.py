#Segundo Proyecto Programado
#Estudiantes: Carolina Rodriguez y Noemí Vargas
#Profesor: Jeff Schmidt


#----------------------------------------------------------------------------------------------------------------------------
#Librerías
import pygame
import sys
from tkinter import *
import random
import time

#Variables globales
global Musica, Puntaje1, Puntaje2, Puntaje3, Vida, Energia
Musica= True
sys.setrecursionlimit(10000)
Puntaje1 = 0
Puntaje2 = 0
Puntaje3 = 0
Vida = 3
Energia = 20


#Clase: Unica
#Atributos: canvas, imagen, foto, nacey, nacex, num
#Metodos: Rebote, Rebote2, desplazamiento, colision, move_active, activar_movimiento,
#          GuardadoTxt, Guardado, EscribirText

class Unica:
    def __init__(self, canvas, imagen, foto, nacex, nacey, num):
        global Energia,Vida,Musica
        self.canvas = canvas
        self.hero = imagen
        self.enemigo = foto
        self.bala = self.canvas.create_image(nacex, nacey,image=self.enemigo,anchor="nw")
        self.speedx = 0
        self.speedy = 8
        self.speedxx = 8
        self.speedyy = 8
        self.active = True
        self.contador = 0
        self.top = 0
        self.vida_jugador=Label(self.canvas,text=Vida)
        self.vida_jugador.place(x=40,y=440)
        self.Energia=Label(self.canvas,text=Energia)
        self.Energia.place(x=53,y=470)


        if num == 1:
            self.move_active()
        elif num == 2:
            self.activar_movimiento()
        time.sleep(0.5)
        
    #E: El evento de la tecla correspondiente
    #S: El movimiento del personaje
    #R: Solo acepta las teclas de dirección
    def desplazamiento(self,event):
        x1, y1, x2, y2 = self.canvas.bbox(self.hero)
        if event.keysym=='Right':
            if x2 <= 300:
                self.canvas.move(self.hero, 10, 0)
        if event.keysym=='Left':
            if x1 >= -0:
                self.canvas.move(self.hero,-10, 0)
        if event.keysym=='Down':
            if y2 <= 430:
                self.canvas.move(self.hero, 0, 10)
        if event.keysym=='Up':
            if y1 >= 0:
                self.canvas.move(self.hero, 0, -10)
                
                
     #E: -
     #S: El movimiento del meterorito del nivel 1
     #R: -           
    def Rebote(self):
        
        musica_colision= pygame.mixer.Sound("space_beep.wav")
        musica_Rebote= pygame.mixer.Sound("beep.wav")
        self.canvas.move(self.bala, self.speedx, self.speedy)
        super_amiga = self.canvas.bbox(self.hero)# Super heroe 
        pos = self.canvas.bbox(self.bala)# Meteorito 
        
        if pos is not None:
                if super_amiga[0] <= pos[2] and super_amiga[2] >= pos[0] and super_amiga[1] <= pos[3] and super_amiga[3] >= pos[1]: #limites
                   if Musica:
                       musica_colision.play()
                   self.colision()
                if pos[2] >= 300 or pos[0] <= 0:
                        self.speedx *= -1 #mov a la izquierda 
                if pos[3] >= 400 or pos[1] <= self.top:
                        if pos[3] >= 400: #mov hacia abajo 
                                if (self.contador == 3):
                                        self.canvas.delete(self.bala) # Rebote / eliminacion 
                                        return
                                self.speedy *= -1 # rebote más arriba 
                                self.top += 100 # limite del rebote
                                self.contador += 1 # Contador del rebote 
                                if pos[3] == 406: #Sonido de rebote/ limites
                                         if Musica:
                                             musica_Rebote.play()
                                if (self.contador == 3):
                                        self.canvas.delete(self.bala) #Eliminacion de la bala 
                        else:

                                self.speedy *= -1
    
    #E: -
    #S: El movimiento del meterorito del nivel 2 y 3
    #R: -     			
    def Rebote2(self):
        musica_colision= pygame.mixer.Sound("space_beep.wav") # Cargar música
        musica_Rebote= pygame.mixer.Sound("beep.wav")
        self.canvas.move(self.bala, self.speedxx, self.speedyy)
        super_amiga = self.canvas.bbox(self.hero)
        pos = self.canvas.bbox(self.bala)                   
        if pos is not None:
                if  super_amiga[0] <= pos[2] and super_amiga[2] >= pos[0] and super_amiga[1] <= pos[3] and super_amiga[3] >= pos[1]:
                   
                   if Musica:
                       musica_colision.play()
                   self.colision()
                if pos[2] >= 300 or pos[0] <= 0:
                        if pos[2] <= 307 or pos[0] == 0:
                                if Musica:
                                   musica_Rebote.play()
                        if pos[2]>= 300:
                                if (self.contador == 3):
                
                                    self.canvas.delete(self.bala)
                                    return
                                self.speedxx *= -1
                                self.contador += 1
                           
                                if (self.contador == 3):
                                    
                                    self.canvas.delete(self.bala)
            
                        else:
                                self.speedxx *= -1
                                
            
                        
                if pos[3] >= 400 or pos[1] <= self.top:
                        if pos[3] <= 406 or pos[1] == self.top:
                                if Musica:
                                         musica_Rebote.play()
                        if pos[3] >= 400:
                                if (self.contador == 3):
                                        self.canvas.delete(self.bala)
                                        return 
                                self.speedyy *= -1
                                self.contador += 1
                                if (self.contador ==3):
                                        self.canvas.delete(self.bala)
                        else:

                                self.speedyy *= -1


    #E: -
    #S: Actualiza los datos de la Vida y Energía según corresponda
    #R: - 
    def colision(self):
             global Vida, Energia
     
             if Vida!= 0 and Energia != 0:
               Energia -= 1
               self.canvas.delete(self.bala)
               
             if Energia == 0 and Vida != 0:
               Vida-=1
               Energia = 20
               self.canvas.delete(self.bala)
            
             if Vida == 0:
               self.canvas.delete(self.bala)
            
             self.vida_jugador.configure(text = Vida)
             self.Energia.configure(text = Energia)

    #E: -
    #S: Llama a la función que realiza el movimiento del meteorita del nivel 1
    #R: - 	    		    
    def move_active(self):
                    if self.active:
                        self.Rebote()
                        wprincipal.after(40, self.move_active)

                        
    #E: -
    #S: Llama a la función que realiza el movimiento del meteorita del nivel 2 y 3
    #R: -
    def activar_movimiento(self):
                    if self.active:
                        self.Rebote2()
                        wprincipal.after(60, self.activar_movimiento)

                        
    #E: Strings de persona y puntaje 
    #S: Modifica el txt de los mejores puntajes 
    #R: Solo acepta strings
    def GuardadoTxt(persona, puntos):             
        mejoresFile = open("Puntajes_txt.txt","r")
        listamejores = mejoresFile.readlines()
        mejoresFile.close()

        return Unica.Guardado (listamejores, "", persona,(puntos), 0)


    #E: Strings de persona ,puntaje , lista
    #S: Verifica los 5 mejores puntajes 
    #R: Solo acepta strings
    def Guardado(lista, res, persona,puntos, i):
        if i == 10:
            return Unica.EscribirText(res)
        
        else:
            listaTemp = lista[0].split(";")
            puntajeTemp = int(listaTemp[1])

            if puntajeTemp < puntos:
                res += persona + ";" + str(puntos) + "\n"
                return Unica.Guardado (lista,res,persona,0,i+1)
            else:
                return Unica.Guardado (lista[1:],res+lista[0],persona,puntos,i+1)


    #E: Strings de persona ,puntaje , lista
    #S: Rescribe los puntajes 
    #R: Solo acepta strings
    def EscribirText(listapuntajes):
        mejoresFile = open("Puntajes_txt.txt","w")
        mejoresFile.write(listapuntajes)
        mejoresFile.close()



#Entradas: - 
#Salidas: Funcion que genera la ventana principal 
#Restriciones: -
def start():
    global wprincipal
    wprincipal = Tk()
    wprincipal.title("Comic's life")
    wprincipal.geometry("300x400")
    wprincipal.resizable(False, False) #

    menu()


#Entradas: - 
#Salidas: Funcion que genera el menu principal 
#Restriciones: -

def menu():#Funcion que es llamada desde  la pantalla inicial, se encarga de briar el menú principal
    global Name
    global Musica
    global Puntaje1,Puntaje2,Puntaje3

    #Creación del canvas
    Menu=Canvas(wprincipal,height = 400, width=300,bg="#4A69FF")
    
    #Imagenes
    Sonido_Encendido=PhotoImage(file="Sonido_on.png")
    Sonido_Apagado=PhotoImage(file="Sonido_off.png") 
    background_principal=PhotoImage(file="Fondo1.png")  
    background_menu=Menu.create_image(0,0,anchor="nw",image=background_principal)
    
    #Etiquetas
    Menu.create_text(150,15,text="Welcome to Comic's life", font=("courier",12),fill="Black")
    Menu.create_text(150,90,text="Insert your nickname",fill="Black")

    #entrada pantalla de menu
    Name = Entry(Menu) #definicion del entry

    #Música
    pygame.init()
    pygame.mixer.init()
    
    if Musica:
        musica_menu= pygame.mixer.music.load("Musica_menu.wav") # Cargar música
        musica_menu=pygame.mixer.music.set_volume(0.3)
        musica_menu=pygame.mixer.music.play(-1)
    else:
         musica_menu=pygame.mixer.music.stop()

    #Botones
    Button_Level1 =Button(Menu,text="Level 1",command=Level1)
    Button_Level2 = Button(Menu,text="Level 2", command = lambda : Level2(Puntaje2))
    Button_Level3 = Button(Menu,text="Level 3", command = lambda : Level3(Puntaje3))
    Button_Start =Button(Menu,text="Start",command=Level1)
    Button_Musica_off =Button(Menu,text="Music Off",width=25, height=20,image= Sonido_Apagado,command=Music_off)
    Button_Musica_on =Button(Menu,text="Music On",width=25, height=20,image= Sonido_Encendido,command=Music_on)
    Button_Score =Button(Menu,text="Score",command= lambda : porcentajes(Puntaje1,Puntaje2,Puntaje3))
    

    
    #Entradas: - 
    #Salidas: Funcion que genera el canvas de about y sus datos
    #Restriciones: -

    def extra_data():
        
        #Imagenes
        about_bg=PhotoImage(file="Fondo1.png")

        #Canvas
        Datos= Canvas(Menu,width=350, height=400)
          
        #Posiciones 
        Datos.place(x=0,y=0)
        Datos.create_image(0,0,image=about_bg,anchor="nw")

        #Etiquetas
        Datos.create_text(150,25,text="País de Producción: Costa Rica", font=("Helvatica",10),fill="blue")
        Datos.create_text(150,55,text="Universidad: Instituto Tecnológico de Costa Rica", font=("Helvatica",10),fill="blue")
        Datos.create_text(150,85,text="Carrera: Ingeniería en Computadores", font=("Helvatica",10),fill="blue")
        Datos.create_text(150,105,text="Asignatura: Taller de Programacion ", font=("Helvatica",10),fill="blue")
        Datos.create_text(150,135,text="Año que cursa: Primer año, Grupo: 1 ", font=("Helvatica",10),fill="blue")
        Datos.create_text(150,165,text="Profesor: Jeff Schmith", font=("Helvatica",10),fill="white")
        Datos.create_text(150,195,text="Version del programa: 3.9.2 ", font=("Helvatica",10),fill="white")
        Datos.create_text(150,225,text="Autores: Carolina Rodriguez, Noemí Vargas", font=("Helvatica",10),fill="white")
        Datos.create_text(150,255,text="Autores de modulos:StackOverflow ", font=("Helvatica",10),fill="white")


        #Entradas: - 
        #Salidas: Funcion que genera el canvas de intrucciones y sus datos
        #Restriciones: -
        def Instructions_F():

            #Imagenes
            Instructions_bg=PhotoImage(file="Fondo2.png")

            #Canvas
            Intructions_C=Canvas(Datos,width=350, height=400)

            #Posiciones
            Intructions_C.place(x=0,y=0)
            Intructions_C.create_image(0,0,image=Instructions_bg,anchor="nw")

            #Etiquetas
            Intructions_C.create_text(150,25,text="Instrucciones:", font=("Helvatica",10),fill="white")
            Intructions_C.create_text(150,130,text="Intenta sobrevivir el mayor tiempo posible sin que \nMs. Iron sea impactado por los rayos. \n\nPara sobrevivir tienes que usar \nlas teclas de dirección. \n\nHabrán sorpresas conforme avances en el juego. \n\n¡Mucha suerte! \n\n No olvides presionar el boton salir y seleccionar \n el nivel siguinte, al pasar de nivel.", font=("Helvatica",10),fill="white")

            
            #E:--
            #S:cerrar ventana 
            #R:---
            def salir():
                Intructions_C.destroy()
                Datos.destroy()

            #Botón y posicion
            Instruc_Regreso=Button(Intructions_C,text="Menú", command = salir)
            Instruc_Regreso.place(x=190,y=290)

            Datos.mainloop()
            
        #Botón y posicion    
        Instructions=Button(Datos,text="Instructions", command = Instructions_F)#Boton del instructivo
        Instructions.place(x=45,y=290)


        
        #E:--
        #S:cerrar ventana 
        #R:---
        def salir():
                 Datos.destroy()

        #Botón y posicion
        Extra_Regreso=Button(Datos,text="Menú", command = salir)
        Extra_Regreso.place(x=190,y=290)

        Datos.mainloop()

    #Botón que genera la pantalla de about
    Button_About =Button(Menu,text="About",command=extra_data)
 
    #Posiciones de los botones
    Button_Level1.place(x=48, y= 210)
    Button_Level2.place(x=125, y= 210)
    Button_Level3.place(x=195, y= 210)
    Button_About.place(x=90, y= 280)
    Button_Score.place(x=172, y= 280)
   
    Button_Start.place(x=130, y= 150)
    Button_Musica_off.place(x=266, y= 372)
    Button_Musica_on.place(x=5, y= 372)
    Menu.place(x=0,y=0)
    Name.place(x=90,y=100)#Posicion del Entry


  
    wprincipal.mainloop()
    



#Entradas: - 
#Salidas: Provoca que el sonido se apague
#Restriciones: -
def Music_off():
    global Musica
    Musica = False
    musica_menu = pygame.mixer.music.stop()


#Entradas: - 
#Salidas: Provoca el sonido se encienda 
#Restriciones: -
def Music_on():
    global Musica
    Musica =True
    musica_menu = pygame.mixer.music.play()
      
    

#Entradas: - 
#Salidas: Funcion que genera el nivel 1 
#Restriciones: -
def Level1():
     global Musica,Name,Puntaje1,Vida,Energia
     z = random.randint(10,300)
     
     #Musica
     musica_menu= pygame.mixer.music.load("Musica_menu.wav")
     
     #Tiempo
     start_time = time.time()

     #Creación de la pantalla
     Level1w= Toplevel()
     Level1w.geometry("300x500")
     Level1w.title("Level 1")
     Level1w.resizable(False, False)

     #Canvas
     nivel1=Canvas(Level1w,width=300, height=500)

     #Imagenes
     miss =PhotoImage(file="Mr_wifi.png")
     enemigo = PhotoImage(file = "rayo.png")
     bgn1=PhotoImage(file="Fondo2.png")
     bg=nivel1.create_image(0,0,image=bgn1,anchor="nw")
     super_heroina = nivel1.create_image(120, 340,image=miss,anchor="nw")
     
     #Etiquetas
     nivel1.create_text(30,480,text="Energía:", font=("Helvatica",10),fill="Black")
     nivel1.create_text(23,450,text="Vidas:", font=("Helvatica",10),fill="Black")
     nivel1.create_text(100,450,text="Tiempo:", font=("Helvatica",10),fill="Black")
     nivel1.create_text(100,480,text="Puntaje:", font=("Helvatica",10),fill="Black")
     nivel1.create_text(200,450,text="NickName:", font=("Helvatica",10),fill="Red")
     nivel1.create_text(200,465,text=Name.get(), font=("Helvatica",10),fill="Red")
     tiempo=Label(nivel1,text=str(int(time.time()-start_time))+"s") #Label del tiempo
     Puntaje_jugador1=Label(nivel1,text=Puntaje1)
     vida_jugador1=Label(nivel1,text=Vida)
     
     #Música
     if Musica:
         Musica_N1=pygame.mixer.music.load("Musica_N1.wav") # Cargar música
         Musica_N1=pygame.mixer.music.set_volume(0.1)# Ajuste el volumen a 0.2
         Musica_N1=pygame.mixer.music.play(-1)

      
     
     #E:-
     #S:cerrar ventana y cancelar la canción
     #R:-
     def salir():
             global Musica
             Musica_N1=pygame.mixer.music.stop()
             Level1w.destroy()
     #Botón que llama a la función salir
     Boton_Salir=Button(nivel1,text="Salir",command=salir)

     #E:-
     #S: Genera el cronómetro y manda a llamar a la función para crear la instacia de la clase cada cierto tiempo
     #R:-
     def update():
         global Puntaje1
         if Vida == 0:
             nivel1.create_text(150,70,text="Haz sido derrotado", font=("courier",19),fill="red")
         if int(time.time()-start_time) == 60 and Vida != 0:
             nivel1.create_text(150,200,text="Has pasado de nivel", font=("courier",15),fill="yellow")
         if int(time.time()-start_time) <= 60 and int(time.time()-start_time) % 1 == 0 and Vida !=0:
             Puntaje1=int(time.time()-start_time)
             Puntaje_jugador1.config(text=Puntaje1)
         if int(time.time()-start_time) <= 60 and int(time.time()-start_time) % 4 == 0 :
             recursiva(nivel1, super_heroina, enemigo, Level1w) #Aquí se llama a la función que crea la instancia de la clase
             tiempo.config(text=str(int(time.time()-start_time))+"s")
         elif (time.time()-start_time) <= 60 and (time.time()-start_time) % 4 != 0 :
             tiempo.config(text=str(int(time.time()-start_time))+"s")
            
         tiempo.after(1,update)

         
     #Posiciones
     nivel1.place(x=0,y=0)
     tiempo.place(x=125,y=440)
     vida_jugador1.place(x=40,y=440)
     Puntaje_jugador1.place(x=125,y=470)
     Boton_Salir.place(x=260, y= 470)

     
     update()    
     Level1w.mainloop()


#E: canvas, las imagenes del superheroe y la bala y la pantalla Tk.
#S: crea la instancia de la clase y manda a llamar al método desplazamiento
#R:-
def recursiva(nivel1, super_heroina, enemigo, Level1w):
             nacex = random.randint(6,290)
             nacey = 0

             #Instancia de la clase
             Ataque_completo = Unica(nivel1, super_heroina, enemigo, nacex, nacey, 1)

             #E: event: Tecla a presionar 
             #S: Llama a el método de desplazamiento de la clase Wifi 
             #R: las teclas de direccion del teclado
             def elevador(event): # llama a el método de desplazamiento
                 Ataque_completo.desplazamiento(event)

             #Llamada al movimiento de heroina
             Level1w.bind("<KeyPress>", elevador)
             
             
#Entradas: -
#Salidas: Funcion que genera el nivel 2
#Restriciones: -    
def Level2(Puntaje1):
     global Name, Musica

     #Creación de la pantalla
     Level2w= Toplevel()
     Level2w.geometry("300x500")
     Level2w.title("Level 2")
     Level2w.resizable(False, False)

     #Canvas
     nivel2=Canvas(Level2w,width=300, height=500)
     
     #Imagenes
     miss2 =PhotoImage(file="Mr_wifi.png")
     enemigo2 = PhotoImage(file = "rayo.png")
     bgn2=PhotoImage(file="Fondo3.png")
     bg=nivel2.create_image(0,0,image=bgn2,anchor="nw")
     super_heroina2 = nivel2.create_image(120, 340,image=miss2,anchor="nw")

     #Tiempo
     start_time = time.time()

     
     #Etiquetas
     nivel2.create_text(30,480,text="Energía:", font=("Helvatica",10),fill="Black")
     nivel2.create_text(23,450,text="Vidas:", font=("Helvatica",10),fill="Black")
     nivel2.create_text(100,450,text="Tiempo:", font=("Helvatica",10),fill="Black")
     nivel2.create_text(100,480,text="Puntaje:", font=("Helvatica",10),fill="Black")
     nivel2.create_text(200,450,text="NickName:", font=("Helvatica",10),fill="Red")
     nivel2.create_text(200,465,text=Name.get(), font=("Helvatica",10),fill="Red")
     tiempo2=Label(nivel2,text=str(int(time.time()-start_time))+"s") #Label del tiempo
     Puntaje_jugador2=Label(nivel2,text=Puntaje1)
     Energia2=Label(nivel2,text=Energia)
     vida_jugador2=Label(nivel2,text=Vida)
     

     #Música
     if Musica:
         pygame.mixer.music.load("Musica_N2.wav") # Cargar música
         pygame.mixer.music.set_volume(0.3)# Ajuste el volumen a 0.2
         pygame.mixer.music.play(-1)

    #E:--
    #S:cerrar ventana y apagar la música
    #R:---
     def salir():
         global Musica
         Level2w.destroy()
         pygame.mixer.music.stop()

     #Botón que llama a la función salir
     Boton_Salir=Button(nivel2,text="Salir",command=salir)


     #E:-
     #S: Genera el cronómetro y manda a llamar a la función para crear la instacia de la clase cada cierto tiempo
     #R:-
     def update():
         global Puntaje2,Vida,Energia
         if Vida == 0:
             nivel2.create_text(150,200,text="Haz sido derrotado", font=("courier",19),fill="yellow")
             
         if int(time.time()-start_time) == 60 and Vida != 0:
             nivel2.create_text(150,200,text=" Has pasado de nivel", font=("courier",15),fill="yellow")

         
         if int(time.time()-start_time) <= 60 and int(time.time()-start_time) % 1 == 0 :
             Puntaje2= int((time.time()-start_time) + 3)
             Puntaje_jugador2.config(text=Puntaje2)
            
         if int(time.time()-start_time) <= 60 and int(time.time()-start_time) % 4 == 0 :
             recursiva2(nivel2, super_heroina2, enemigo2, Level2w) #Aquí llama a la función para crear la instancia de la clase
             tiempo2.config(text=str(int(time.time()-start_time))+"s")

         elif (time.time()-start_time) <= 60 and (time.time()-start_time) % 4 != 0 :
             tiempo2.config(text=str(int(time.time()-start_time))+"s")
          
         tiempo2.after(1,update)
     
     #Posiciones
     nivel2.place(x=0,y=0)
     Puntaje_jugador2.place(x=125,y=470)
     Energia2.place(x=53,y=470)
     vida_jugador2.place(x=40,y=440)
     tiempo2.place(x=130,y=440)
     Boton_Salir.place(x=260, y= 470)

     
     update()   
     Level2w.mainloop()


#E: canvas, las imagenes del superheroe y la bala y la pantalla Tk.
#S: crea la instancia de la clase y manda a llamar al método desplazamiento
#R:-
def recursiva2(nivel2, super_heroina2, enemigo2, Level2w):
         #Instancias de la clase
         Ataque_completo_2 = Unica(nivel2, super_heroina2, enemigo2, 0, random.randint(6,390), 2)
         Ataque_completo_2_2 = Unica(nivel2, super_heroina2, enemigo2, 250, 0, 2)
         
         #E: event: Tecla a presionar 
         #S: llama a el método de desplazamiento de la clase Wifi 
         #R: las teclas de direccion del teclado
         def elevador2(event): # llama a el método de desplazamiento
             Ataque_completo_2.desplazamiento(event)

         #Llamada al movimiento de heroina
         Level2w.bind("<KeyPress>", elevador2)


#Entradas: - 
#Salidas: Funcion que genera el nivel 3
#Restriciones: -
def Level3(Puntaje3):
     global Name,Musica,Vida,Energia
     
     #Creación de la pantalla
     Level3w= Toplevel()
     Level3w.geometry("300x500")
     Level3w.title("Level 3")
     Level3w.resizable(False, False)

     #Canvas
     nivel3=Canvas(Level3w,width=300, height=500)

     #Imagenes
     miss3=PhotoImage(file="Mr_wifi.png")
     enemigo3 = PhotoImage(file = "rayo.png")
     bgn3=PhotoImage(file="Fondo4.png")
     bg=nivel3.create_image(0,0,image=bgn3,anchor="nw")
     super_heroina3 = nivel3.create_image(120, 340,image=miss3,anchor="nw")

     #Tiempo
     start_time = time.time()

     #Etiquetas
     nivel3.create_text(30,480,text="Energía:", font=("Helvatica",10),fill="Black")
     nivel3.create_text(23,450,text="Vidas:", font=("Helvatica",10),fill="Black")
     nivel3.create_text(100,450,text="Tiempo:", font=("Helvatica",10),fill="Black")
     nivel3.create_text(100,480,text="Puntaje:", font=("Helvatica",10),fill="Black")
     nivel3.create_text(200,450,text="NickName:", font=("Helvatica",10),fill="Red")
     nivel3.create_text(200,465,text=Name.get(), font=("Helvatica",10),fill="Red")
     tiempo3=Label(nivel3,text=str(int(time.time()-start_time))+"s") #Label del tiempo
     Puntaje_jugador3=Label(nivel3,text=Puntaje1)
     Energia3=Label(nivel3,text=Energia)
     vida_jugador=Label(nivel3,text=Vida)
     

     #Música
     if Musica:
         pygame.mixer.music.load("Musica_N3.wav") # Cargar música
         pygame.mixer.music.set_volume(0.3)# Ajuste el volumen a 0.2
         pygame.mixer.music.play(-1)
         

     #E:--
     #S:cerrar ventana y apaga la música 
     #R:---
     def salir():
         Level3w.destroy()
         pygame.mixer.music.stop()
         
     #Botón que llama a la función salir  
     Boton_Salir=Button(nivel3,text="Salir",command=salir)


     
     #E:-
     #S: Genera el cronómetro y crea la instacia de la clase cada cierto tiempo
     #R:-
     def update():
         global Puntaje3
         nacex = random.randint(6,290)  
         nacey = 0
         
         if Vida == 0:
             nivel3.create_text(150,200,text="Haz sido derrotado", font=("courier",19),fill="yellow")
         if int(time.time()-start_time) == 60 and Vida != 0:
             nivel3.create_text(150,200,text="Has pasado de nivel", font=("courier",16),fill="yellow")
         if int(time.time()-start_time) <= 60 and int(time.time()-start_time) % 1 == 0 :
               Puntaje3=int((time.time()-start_time) + 5)
               Puntaje_jugador3.config(text=Puntaje3)
         if int(time.time()-start_time) <= 60 and int(time.time()-start_time) % 2 == 0 :
             Ataque_bouncing_2_2 = Unica(nivel3, super_heroina3, enemigo3, random.randint(5,300), random.randint(70,300), 2) #Aquí se crea la instancia de la clase

             #E: event: Tecla a presionar 
             #S: llama a el método de desplazamiento de la clase Wifi 
             #R: las teclas de direccion del teclado 
             def elevador3(event): # llama a el método de desplazamiento de la clase Unica
                 Ataque_bouncing_2_2.desplazamiento(event)

             #Llamada al movimiento de heroina
             Level3w.bind("<KeyPress>", elevador3)

             #Actualización del label del tiempo
             tiempo3.config(text=str(int(time.time()-start_time))+"s")
             
         tiempo3.after(1,update)
         
     #Posiciones
     nivel3.place(x=0,y=0)
     tiempo3.place(x=125,y=440)
     Puntaje_jugador3.place(x=125,y=470)
     Energia3.place(x=53,y=470)
     vida_jugador.place(x=40,y=440)
     Boton_Salir.place(x=260, y= 470)

     
     update()    
     Level3w.mainloop()

#E: Los puntajes obtenidos en los tres niveles
#S: Manda a llamar a la función para guardar al jugador y sus puntos, ademas de generar el formato de escritura de la ventana.
#R:-    
def porcentajes(Puntaje1,Puntaje2,Puntaje3): #genera la ventana de los puntajes

    #Creación de la ventana
    porcent= Toplevel()
    porcent.geometry("300x400")
    porcent.title("Best Scores")
    puntos = Puntaje1+Puntaje2+Puntaje3

    #Canva
    Score=Canvas(porcent,width=300, height=400)
    Score.place(x=0,y=0)

    #Imagenes    
    Puntajes=PhotoImage(file="Puntajes.png")       
    Punta_bg=Score.create_image(0,0,image=Puntajes,anchor="nw")

    #Etiqueta
    Score.create_text(150,50,text="Scores", font=("Helvatica",30),fill="Black")


    #E:--
    #S:cerrar ventana 
    #R:---
    def salir():
         porcent.destroy()
         
    #Botón que llama a la función salir    
    Salir = Button(Score,text="Menu",command= salir)
    Salir.place(x=255, y=370)

    #Llamada al método de la clase
    Unica.GuardadoTxt(Name.get(), puntos)  

    #Lee el documento .txt
    mejoresFile = open("Puntajes_txt.txt","r")
    listamejores = mejoresFile.readlines()
    mejoresFile.close()

    #Lista de jugadores
    listaTemp = listamejores[0].split(";")

    Score.create_text(160,120,text=listaTemp[0] + " " +listaTemp[1], font=("courier",20),fill="Black")

    listaTemp = listamejores[1].split(";")

    Score.create_text(160,150,text=listaTemp[0] + " " +listaTemp[1], font=("courier",20),fill="Black")

    listaTemp = listamejores[2].split(";")

    Score.create_text(160,180,text=listaTemp[0] + " " +listaTemp[1], font=("courier",20),fill="Black")

    listaTemp = listamejores[3].split(";")


    Score.create_text(160,210,text=listaTemp[0] + " " +listaTemp[1], font=("courier",20),fill="Black")

    listaTemp = listamejores[4].split(";")


    Score.create_text(160,230,text=listaTemp[0] + " " +listaTemp[1], font=("courier",20),fill="Black")

    listaTemp = listamejores[5].split(";")

    Score.create_text(160,260,text=listaTemp[0] + " " +listaTemp[1], font=("courier",20),fill="Black")

    listaTemp = listamejores[6].split(";")

    Score.create_text(160,290,text=listaTemp[0] + " " +listaTemp[1], font=("courier",20),fill="Black")

    listaTemp = listamejores[7].split(";")

    Score.create_text(160,320,text=listaTemp[0] + " " +listaTemp[1], font=("courier",20),fill="Black")

    listaTemp = listamejores[8].split(";")

    Score.create_text(160,350,text=listaTemp[0] + " " +listaTemp[1], font=("courier",20),fill="Black")

    listaTemp = listamejores[9].split(";")

    Score.create_text(160,380,text=listaTemp[0] + " " +listaTemp[1], font=("courier",20),fill="Black")

    
    Score.mainloop()

  

start()
