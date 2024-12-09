##Programa que imprime un cuadrado de un numero ingresado mientras sea positivo
def Cuadrado(n):
    while n>0:
        resultado=n**2
        return resultado
Numero=int(input("¿Que numero desea elevar al cuadrado?:"))
if Numero>0:
        print("El numero",Numero,"elevado al cuadrado es:\n",Cuadrado(Numero))
else:
        print("Ingrese solo numeros postivos")
##Programa para calcular formulas si un numero es o no es par 

def Calcular(n):
        if n%2 != 0:
            resultado=((3*n)+1)
            
            print("El numero impar multiplicado por 3 y sumado con 1 da: ",resultado )
            
        else:
            resultado_2=n/2
            
            print("El numero par dividido entre dos da: ",resultado_2)
numero_2=int(input("Ingrese un numero:"))
Calcular(numero_2)
##Programa para calcular año de superacion en un periodo de x años
Porcentaje_a=2/100
Porcentaje_b=3/100

A=25
B=18.9
x=15
for i in range (1,x):
 i+=1
Interes=A*Porcentaje_a*i
Interesb=B*Porcentaje_b*i
if Interesb>Interes:
     print("B va a superar la poblacion de A,en",i,"años","con un numero de:",Interesb,"Habitantes superiores a A" )
else:
    print("En un periodo de ",x,"años B no ha superado a A")

