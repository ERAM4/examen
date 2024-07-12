import random

import csv




Trabajadores = [ "Juan Pérez",  "María Garcia", "Carlos Lopéz ","Ana martínez", "Pedro Rodríguez", "Laura Hernández","Miguel Sanchez","Isabel Gómez","Francisco Díaz ", "Elena Fernández"]

sueldodelostrabajadores=[]

with open("sueldos_examen.csv","w",encoding="utf-8") as archivo:
    
    archivo.write("Nombre,   ,Sueldo   ,Descuento   ,AFP ,Sueldo liquido\n")
    



def clasificarlossueldos():
    
    ordenar = sorted(sueldodelostrabajadores, key=lambda x: x["sueldo"])
    
    for nom in ordenar:
        
        print(f'{nom["nombre"]}: {nom["sueldo"]}')

def asignarlossueldosaleatorios():
    
    for n in range(len(Trabajadores)):
        
        sueldodelostrabajadores.append({"nombre":Trabajadores[n],"sueldo":random.randint(300000,2500000)})

def paraverlasestadisticas():
    
    product = 1
    
    ttal = 0
    
    ordenar = sorted(sueldodelostrabajadores, key=lambda x: x["sueldo"])
    
    print("1.- Sueldo más alto")
    
    print("2.- Sueldo más bajo ")
    
    print("3.- Promedio de los sueldos")
    
    print("4.- Media geometrica")
    
    print("5.- Salir")
    
    
    while True:
        try:
            
            mnu=int(input("Ingresa una opcion\n> "))
            
            
        except ValueError:
            
            print("solo los valores estipulados en el menu")
            
            
        else:
            match mnu:
                
                case 1:
                    
                    print(max(ordenar,key=lambda x: x["sueldo"]))
                    
                case 2:
                    
                    print(min(ordenar,key=lambda x: x["sueldo"]))
                    
                case 3:
                    
                    for suldo in sueldodelostrabajadores:
                        
                        ttal=suldo["sueldo"]
                        
                    print(f"el promedio de los sueldos es : {ttal/len(Trabajadores)}")
                    
                case 4:
                    x = len(Trabajadores)
                    
                    for suldo in sueldodelostrabajadores:
                        
                        product *= suldo["sueldo"]
                        
                    resultado=product ** (1 / x)
                    
                    print(f"la media geometrica es : {resultado.__trunc__()}")
                    
                 
                case 5:
                    
                    break
                
    return

def reportdelossueldos():
    
    for suldos in sueldodelostrabajadores:
        
        dsct=0.07*suldos["sueldo"]
        
        AFP=0.12*suldos["sueldo"]
        
        suldoliquido=suldos["sueldo"]-dsct-AFP
        
        with open("sueldos_examen.csv","a",encoding="utf-8") as archivo:
            
            archivo.write(f"{suldos["nombre"]} ,{suldos["sueldo"]} ,{dsct}, {AFP}, {suldoliquido}\n")
            


while True:
    
    print("1.- Asignar sueldos aleatorios")
    
    print("2.- Clasificar Sueldos")
    
    print("3.- Ver estadisticas")
    
    print("4.- Reporte de sueldos")
    
    print("5.- Salir del Programa")
    
    try:
        mnuu=int(input("Ingrese una opcion\n> "))
        
    except ValueError:
        
            print("Ingresa solo los numeros vistos en pantalla para continuar\n>")
            
    else:
        
        match mnuu:
            
            case 1:
                
                asignarlossueldosaleatorios()
                
            case 2:
                
                clasificarlossueldos()
                
            case 3:

                paraverlasestadisticas()
                
            case 4:
                
                 reportdelossueldos()
                
            case 5:
                
                print("Finalizando Programa...\nDesarrollado por Carlos Vergara\nRUT 12.345.678-9")
                
                break
            
                exit
