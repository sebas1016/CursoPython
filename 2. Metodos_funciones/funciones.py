#Son para tener codigo que se va usar muchas veces y de esta formar ahorrar codigo
#Es una buena practica de programación
def suma(num1,num2):
    resultado = num1 + num2
    print(resultado)

suma(2,3)

#Ejemplo de funcion para aplicar logica
#Chequear número pares en una lista
list_numeros = [1,3,5]
def check_num_par_list(lista):
    for num in lista:
        if num % 2 == 0:
            print('True')
            return True
        else:
            pass
    print('False')
    return False
check_num_par_list(list_numeros)

#*args es una forma de poner un parametros indefinidos en una funcion / funciona como tupla

def func(*args):
    return print(sum(args)*3)

func(2,3,4)

#**kwargs funciona como un diccionario
def func_2(**kwargs):
    if 'fruit' in kwargs:
        print("Mi fruta escogida es {}".format(kwargs['fruit']))
    else:
        print("No hay fruits")
        
func_2(fruit='manzana', veggeta = 'lechuga')

#Se puede fucionar ambos *args y **kwargs
def func3(*args, **kwargs):
    print(args)
    print(kwargs)
    print('Me gustaria {} {}'.format(args[0], kwargs['comida']))
    
func3(2,3,4,4, comida='hamburguesa',animal='dog')