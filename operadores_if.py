if True:
    print('se ejecuta una accion')


if False:
    print('nunca se ejecutara ')


## Adivinar el significado de mascotas segun tu personalidad

mascotas = input('Tu mascota preferida es: ')

## perro, gato, tortuga

if mascotas == 'perro':
    print('Eres una persona amigable')
elif mascotas == 'gato':
    print ('Eres una persona hogareña')
elif mascotas == 'tortuga':
    print('Eres una persona constante')
else:
    print('No podemos definir tu personalidad')


## Si el stock de una bodega es el correcto 

stock = int(input('Digita el stock: '))

if stock>100 and stock<=1000:
    print('El stock es correcto')
else:
    print ('el stock es incorrecto')



## Un numero es par o impar

numero = int(input('Ingresar un numero '))
resultado = numero % 2
if(resultado==0):
    print(resultado)
    print('Es par')
else:
    print(resultado)
    print('es impar')



