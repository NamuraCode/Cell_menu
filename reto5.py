import os
import math

print("Bienvenido al sistema de ubicación para zonas públicas WIFI\n")
sesion_iniciada=False
Coordenadas=[
    [0,0], 
    [0,0], 
    [0,0], 
]
ubicación_actual=False
información={}
zonas_wifi=[
    [6.632, -72.984, 285],
    [6.564, -73.061, 127],
    [6.531, -73.002,  15],
    [6.623, -72.978,  56],
]
zonas_cercanas=[{},{}]   
contrasena=59515
latitud_Maxima=6.690
latitud_Minima=6.532
longitud_Maxima=-72.872
longitud_Minima=-73.120

R=6372.795477598
velocidad_promedio_moto= 19.44
velocidad_promedio_pie= 0.483

def cambiar_contrasena():
    global contrasena
    contrasena_actual=input("ingrese su contraseña actual ")
    if contrasena_actual!=contrasena:
        print("Error")
        exit()
    elif contrasena_actual==contrasena:
        contrasena_nueva=input("ingrese su nueva contraseña ")
        if contrasena_nueva==contrasena:
            print("Error")
            exit()
    contrasena=contrasena_nueva

def ingresar_coordenadas():
    global Coordenadas
    try:
        latitud_trabajo=float(input("Ingrese la latitud de su trabajo "))
        if latitud_trabajo>latitud_Maxima or latitud_trabajo<latitud_Minima:
            print("Error coordenada")
            exit()
        Coordenadas[0][0]=latitud_trabajo
        longitud_trabajo=float(input("Ingrese la longitud de su trabajo "))
        if longitud_trabajo>longitud_Maxima or longitud_trabajo<longitud_Minima:
            print("Error coordenada")
            exit()
        Coordenadas[0][1]=longitud_trabajo

        latitud_casa=float(input("Ingrese la latitud de su casa "))
        if latitud_casa>latitud_Maxima or latitud_casa<latitud_Minima:
            print("Error coordenada")
            exit()
        Coordenadas[1][0]=latitud_casa

        longitud_casa=float(input("Ingrese la longitud de su casa "))
        if longitud_casa>longitud_Maxima or longitud_casa<longitud_Minima:
            print("Error coordenada")
            exit()
        Coordenadas[1][1]=longitud_casa

        latitud_parque=float(input("Ingrese latitud de su casa "))
        if latitud_parque>latitud_Maxima or latitud_parque<latitud_Minima:
            print("Error cooordenada")
            exit()
        Coordenadas[2][0]=latitud_parque

        longitud_parque=float(input("Ingrese la longitud del parque "))
        if longitud_parque>longitud_Maxima or longitud_parque<longitud_Minima:
            print("Error coordenada")
            exit()
        Coordenadas[2][1]=longitud_parque

    except ValueError:
        print("Error")
        exit()

def actualizar_coordenadas():
    try:
        posicion_mas_al_sur=0
        latitud_mas_al_sur=Coordenadas[0][0]
        posicion_mas_al_oriente=0
        longitud_mas_al_oriente=Coordenadas[0][1]
        for posicion, latlong in enumerate(Coordenadas):
            print(f"coordenada [latitud,longitud] {posicion+1} : [{latlong[0], latlong[1]}]") 
            if latitud_mas_al_sur>latlong[0]:
                posicion_mas_al_sur=posicion
                latitud_mas_al_sur=latlong[0]
            
            if longitud_mas_al_oriente<latlong[1]:
                posicion_mas_al_oriente=posicion
                longitud_mas_al_oriente=latlong[1]
        print(f"La coordenada {posicion_mas_al_sur+1} es la que esta más al sur")
        print(f"La coordenada {posicion_mas_al_oriente+1} es la que esta más al oriente")

        posicion_a_cambiar=input("Presione 1,2 o 3 para actualizar la respectiva coordenadas\npresione 0 para regresar al menu\n ")
        if posicion_a_cambiar not in ["0","1","2","3"]:
            print("Error actualización")
            exit()
        if posicion_a_cambiar!="0":
            posicion_final=int(posicion_a_cambiar)-1   
            latitud=float(input("Ingrese latitud "))      
            if latitud>latitud_Maxima or latitud<latitud_Minima:
                print("Error actualización")
                exit()
            else:
                Coordenadas[posicion_final][0]=latitud
                longitud=float(input("Ingrese longitud "))      
            if longitud>longitud_Maxima or longitud<longitud_Minima:
                print("Error actualización")
                exit()
            else:
                Coordenadas[posicion_final][1]=longitud
        
    except TypeError:
        print("Error actualización")
        exit()

def calcular_distancia(lat1, lon1, lat2, lon2):
    lat1=math.radians(lat1)
    lon1=math.radians(lon1)
    lat2=math.radians(lat2)
    lon2=math.radians(lon2)

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    sin2_lat = math.sin(delta_lat / 2) ** 2
    sin2_lon = math.sin(delta_lon / 2) ** 2

    raiz_cuadrada = math.sqrt(sin2_lat + math.cos(lat1) * math.cos(lat2) * sin2_lon)
    distacia = 2 * R * math.asin(raiz_cuadrada)

    return round(distacia) 

Usuario=input("Nombre de usuario: ")

if Usuario!="51595":
    print("Error")

else:
    contraseña=input("contrasena: ")

    if contraseña!="59515":
        print("Error")

    else:
        C=int(595)
        C_2=int((5+5)-1//1)
        C_3=input("Capchat " +(str(C)+ " + " +str(C_2)) +(" = "))

        if C_3!="604":
            print("Error")
            
        else:
            sesion_iniciada=True
            print("Sesión iniciada")

Menu=[
    "Cambiar contraseña", 
    "Ingresar coordenadas actuales", 
    "Ubicar zona wifi más cercana", 
    "Guardar archivo con ubicación cercana",
    "Actualizar registros de zonas wifi desde archivo", 
    "Elegir opción de menú favorita", 
    "Cerrar sesión",
]    
opcion_validas=["1","2","3","4","5","6","7"]
opciones_favoritas=["1","2","3","4","5"]

while sesion_iniciada:
    Opcion_correcta=False
    for i, j in enumerate(Menu):
        print(i+1,j)
    for opcion_usuario in range(3): 
        opcion_usuario=input("Elija una opción: ")  
        if opcion_usuario not in opcion_validas:
            print("Error")
            sesion_iniciada=False
        if opcion_usuario in opcion_validas:
            Opcion_correcta=True    
        if opcion_usuario== "1":
            cambiar_contrasena()
            break
        elif opcion_usuario== "2":
            if Coordenadas[0][0]==0:
                ingresar_coordenadas()
                break
            else:
                actualizar_coordenadas()

        elif opcion_usuario== "3":
            try:
                if Coordenadas[0][0]==0:
                    print("Error sin registro de coordenadas")
                    sesion_iniciada=False
                    break
                else:
                    for posicion, latlong in enumerate(Coordenadas):
                        print(f"coordenada [latitud,longitud] {posicion+1} : [{latlong[0], latlong[1]}]") 
                    ubicación_actual = int(input(f"Por favor elija su ubicacióno actual (1, 2 ó 3) para calcular la distancia a los puntos de conexión\n"))
                    opcion_ubicación_a = [1,2,3]
                    if ubicación_actual not in opcion_ubicación_a:
                        print("Error ubicación")
                        sesion_iniciada=False
                        break
                    if ubicación_actual in opcion_ubicación_a:
                        latitud_inicial, longitud_inicial = Coordenadas[ubicación_actual-1][0], Coordenadas[ubicación_actual-1][1]
                        for zona in zonas_wifi:
                            latitud_final, longitud_final = zona[0], zona[1]
                            distacia = calcular_distancia(latitud_inicial, longitud_inicial, latitud_final, longitud_final)
                            diccionario_distancia = {"distancia":distacia, "usuarios":zona[2], "coordenadas":(zona[0],zona[1])}
                            if not zonas_cercanas[0]:
                                zonas_cercanas[0] = diccionario_distancia
                            else:
                                if distacia < zonas_cercanas[0]["distancia"]:
                                    zonas_cercanas[1] = zonas_cercanas[0]
                                    zonas_cercanas[0] = diccionario_distancia
                                elif not zonas_cercanas[1] or distacia < zonas_cercanas[1]["distancia"]:
                                    zonas_cercanas[1] = diccionario_distancia

                        if zonas_cercanas[1]["usuarios"] < zonas_cercanas[0]["usuarios"]:
                            zonas_cercanas[0], zonas_cercanas[1] = zonas_cercanas[1], zonas_cercanas[0]
                        print("Zonas wifi cercanas con menos usuarios")
                        print(f"La zona wifi 1: ubicada en ['{zonas_cercanas[0]['coordenadas'][0]}','{zonas_cercanas[0]['coordenadas'][1]}'] a {zonas_cercanas[0]['distancia']} metros , tiene en promedio {zonas_cercanas[0]['usuarios']} ")
                        print(f"La zona wifi 2: ubicada en ['{zonas_cercanas[1]['coordenadas'][0]}','{zonas_cercanas[1]['coordenadas'][1]}'] a {zonas_cercanas[1]['distancia']} metros , tiene en promedio {zonas_cercanas[1]['usuarios']} ")
                        opciones_validas_indicaciones=[1,2] 
                        indicaciones=int(input("Elija 1 o 2 para recibir indicaciones de llegada "))
                        if indicaciones not in opciones_validas_indicaciones:
                            print("Error zona wifi")
                            sesion_iniciada=False
                            break
                        if indicaciones in opciones_validas_indicaciones:
                            distancia_a_zonas = zonas_cercanas[indicaciones-1]['distancia']
                            tiempo_a_pie = distancia_a_zonas / velocidad_promedio_pie
                            tiempo_a_moto = distancia_a_zonas / velocidad_promedio_moto
                            tiempo_promedio=[tiempo_a_moto,tiempo_a_pie]
                            sur=-0.1
                            occidente=-180.0
                            if zonas_cercanas[indicaciones-1]['coordenadas'][0] > sur and zonas_cercanas[indicaciones-1]['coordenadas'][1] > occidente:
                                print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
                                print(f"tiempo estimado a pie '{tiempo_a_pie}' y en moto '{tiempo_a_moto}'")
                            elif zonas_cercanas[indicaciones-1]['coordenadas'][0] < sur and zonas_cercanas[indicaciones-1]['coordenadas'][1] < occidente:
                                print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el sur")
                                print(f"tiempo estimado a pie '{tiempo_a_pie}' y en moto '{tiempo_a_moto}'")
                        salir=input("Presione 0 para salir ")
                        if salir=="0":
                            break
            except:
                print('Error ubicación')
                sesion_iniciada=False
                break
        elif opcion_usuario== "4":
            if Coordenadas[0][0]==0:
                print("Error de alistamiento")
                sesion_iniciada=False
                break
            if ubicación_actual==False:
                print("Error de alistamiento")
                sesion_iniciada=False
                break
            else:
                medio_de_transporte=["moto","pie"]
                información['actual']=Coordenadas[ubicación_actual-1][0],Coordenadas[ubicación_actual-1][1]
                información['zonawifi1']=[zonas_cercanas[indicaciones-1]['coordenadas'][0],zonas_cercanas[indicaciones-1]['coordenadas'][1],zonas_cercanas[indicaciones-1]['usuarios']]
                información['recorrido']=[zonas_cercanas[indicaciones-1]['distancia'],medio_de_transporte[indicaciones-1],tiempo_promedio[indicaciones-1]]
                print(información)
                opcion_exportar=input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principa\n")
                opcion_exportar_correcta=['1','0']
                if opcion_exportar not in opcion_exportar_correcta:
                    print('Error')
                    sesion_iniciada=False
                    break 
                elif opcion_exportar==opcion_exportar_correcta[0]:
                    archivo=open('Archivo.txt','w') 
                    información=archivo.write(str(información))
                    archivo.close
                    print('Exportando archivo')
                    sesion_iniciada=False
                    break
                elif opcion_exportar==opcion_exportar_correcta[1]:
                    break
        elif opcion_usuario== "5":
            zonas_wifi.clear()
            with open('ZonasWifi.txt', 'r') as f:
                zonas_wifi=[linea.split("\n") for linea in f]
                f.close()
            print(zonas_wifi)
            opcion_actualizar=input('Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal\n') 
            if opcion_actualizar=='0':
                break
        if opcion_usuario== "6":
            opcion_favorita=input("Elija opción favorita: ")
            if opcion_favorita not in opciones_favoritas:
                print("Error")
                sesion_iniciada=False
                break
            if opcion_favorita in opciones_favoritas:
                adivinanza=input("Para confirmar por favor responda: Uno con cero son diez y con uno menos es: ")
                if adivinanza != "9":
                    print("Error")
                    break           
                else:
                    adivinanza2=input("Para confirmar por favor responda: Cuéntate las manos o cuéntate los pies y en seguida sabrás qué es: ")
                    if adivinanza2 != "5":
                        print("Error") 
                        break  
                    if  adivinanza2=="5":                   
                        Opcion_Eliminar=Menu.pop(int(opcion_favorita)-1)
                        Menu.insert(0,Opcion_Eliminar)
                        from os import system
                        system("cls") 
                        break        
        if opcion_usuario== "7":   
            print("Hasta pronto") 
            sesion_iniciada=False    
            break