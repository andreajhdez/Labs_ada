#Se definen variables de cada tipo de primitivo
num_entero = 31
num_real = 12.31
tipo_cadena = "Hola me llamo Andrea Juliana"
tipo_bool = False

#Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
concat_variables = str(num_entero) + " " + str(num_real) + " " + tipo_cadena + " " + str(tipo_bool) 

# LIMITE ENTEROS Y FLOTANTES:
investiga = "En el caso de los números enteros o INT no tienen límite de tamaño en python 3. En python 3 se pueden manejar valores tan largos como lo permita la memoria disponible.\nLas variables tipo FLOAT, por el contrario no tienen presición infinita. Las variables tipo float tienen valores mínimos y máximos. La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308. En resumen, los valores FLOAT son representados como valores de doble presición (64 bits), el valor maximo aproximado de un float es 1.8x10308. Si algún numero excede este valor máximo, python arroja un error: string inf" 

#Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable.
#Según investigué en algunos videos, para hacer esto se puede utilizar la fórmula de gauss, la cual la programamos en el ejercicio que hicimos en clase. 
#Ingresamos variable n
n = input('Ingresa numero de variable n')
#Convierto variable a numero entero
nn= int(n)
#Realizo la operación solicitada
operacion = (nn*(nn+1))/2
#imprimo la operacion


#Se imprimen los resultados de las tareas anteriores
print(num_entero, num_real, tipo_cadena, tipo_bool, sep = '\n')
print()
print(concat_variables)
print()
print(investiga)
print()
print(operacion)
