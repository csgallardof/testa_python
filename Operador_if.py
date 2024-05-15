#if True:
 #   print('Se ejecuta una acción')
    
#if False:
 #   print('Nunca se va a ejecutar')

## Adivinar el significado de las mascotas

#mascotas=input('Tu mascota preferida es: ')

## perro, gato, tortuga

#if mascotas=='perro':
 #   print('Eres una persona amigable.')
#elif mascotas=='gato':
 #   print('Eres una persona hogareña.')
#elif mascotas=='tortuga':
 #   print('Eres una persona constante.')
#else:
 #   print('No podemos definir tú personalidad.')

## Si el stock de una bodega es el correcto

#stock=int(input('Digita el stock: '))
#if stock>100 and stock<=1000:
 #   print('El stock es correcto')
#else:
 #   print('El stock es incorrecto')

    ##Un número es par o impaar
numero=int(input('Ingresar un número: '))
resultado = numero%2
if(resultado==0):
    print(resultado)
    print('Es par')
else:
    print('Es impar')
