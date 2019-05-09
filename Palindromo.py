#Proyecto  	: Python 
#Consultor 	: Edwin Reyes
#Taller		: Generar programa que permita identificar si una palabra es palindroma
print (".............................................................................")
print ("Proyecto  	: Python \n\
Consultor 	: Edwin Reyes\n\
Taller		: Generar programa que permita identificar si una palabra es palindroma")
print (".............................................................................")
print ("")
print ("Palindromo: Palabra que se lee igual de derecha a izquierda o izquierda a derecha")
print ("")
V_Palabra = input("Ingrese una palabra: ")
V_Palaba_Rever = V_Palabra[::-1]
if V_Palabra == V_Palaba_Rever:
    print("La palabra **"+V_Palabra+"** ingresada si es palindromo!!")
else:
    print("La palabra **"+V_Palabra+"**  ingresada no es palindromo!!")
	
print (".............................................................................")