#Programa que genere contraseñas aleatorias de un largo de 12 caracteres.

import string
import random

def crear_archivo_contrasenas():
    
    # Se declara el largo de cada contraseña.
    largo_contrasena = 12
    
    with open('claves_generadas.txt','w') as text_file:
        for i in range(15):
            # Se declaran los caracteres que generarán las contraseñas.
            lista_caracteres = list(string.ascii_letters + string.digits + "!@#$%^&*()")

            random.shuffle(lista_caracteres)

            password = []
            
            for j in range(largo_contrasena):
                password.append(random.choice(lista_caracteres))
            
           
             if i < 14:
                
                text_file.write("".join(password)+'\n')
             else:
            
                text_file.write("".join(password))
                
def leer_archivo_contrasenas():
    
    # Se lee el archivo y se extraen las contraseñas generadas anteriormente y se retornan.
    with open('claves_generadas.txt','r') as text_file:
        contrasenas = text_file.read().split('\n')
        return contrasenas

def mostrar_contrasenas_archivo(contrasenas_generadas):

    #Recorre la lista de contraseñas generadas obtenidas y se muestran por pantalla.
    for indice,contrasena in enumerate(contrasenas_generadas):
        print('Contraseña '+str(indice+1)+': '+contrasena)

def main():

    crear_archivo_contrasenas()

    contrasenas_generadas = leer_archivo_contrasenas()
    
    mostrar_contrasenas_archivo(contrasenas_generadas)
    
if __name__ == "__main__":
    main()