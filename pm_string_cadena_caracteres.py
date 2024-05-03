text = 'Somos estudiantes de Ciberseguridad'

print('Somos' in text)
print('JS' in text)

if 'estudiantes' in text:
    print('Si somos estudiantes')
else:
    print('Soy profesor')

if 'amigos' in text:
    print('Si somos estudiantes')
else:
    print('Soy profesor')

num_caracteres = len(text)
print(num_caracteres)

print(text) 
print(text.upper())
print(text.lower())

print(text.count('o'))
print(text.count('a'))
print(text.count('e'))
print(text.count('i'))
print(text.count('d'))

print(text.replace('estudiantes', 'profesores'))