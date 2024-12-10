'''
Función de la Pregunta 1
'''

def desplazar(c, d):
   alfabeto = "abcdefghijklmnopqrstuvwxyz"
   i = 0
   while i<len(alfabeto) and alfabeto[i]!=c:
      i += 1
   if i<len(alfabeto):
      j = (i+d)%len(alfabeto)
      return alfabeto[j]
   return c

'''
codigo pregunta 1
'''
# nuevo = ""
# desp = 1
# for letra in "acy":
#     nuevo = nuevo + desplazar(letra, desp)
#     desp +=1
# 
# print(nuevo)
# El valor de j es llamado #1 = b , #2 = e y #3 = b
'''
Pregunta 2
Escriba el código de la función codificar
'''

def codificar(texto):
      i=0
      pal=""
      frase=""
      for var in texto:
         if var != "#":
            pal+=var
            i+=1
            if var == ";":
               pal=""
         else:
             i+=1
             desp=texto[i]
             desp=int(desp)
             for let in pal:
                 frase+=desplazar(let,desp)
             frase+=" "
      return frase

'''
Llamadas a la función codificar para verificar que está correcta
'''
print(codificar("edad#1"))
print(codificar("hola#3;mundo#2"))


"Pregunta 3"
"Descomente y complete el siguiente programa"

continuar = True
while continuar:
   palabra = input("Ingrese una palabra: ")
   if palabra.lower()=="fin":
      continuar = False
   else:
      nuevo=""
      desp=int(input("ingrese desplazamiento: "))
      for let in palabra:
            nuevo+=desplazar(let,desp)
      print(nuevo)  
