text = 'Somos estudiantes de ciberseguridad'

print('Somos' in text)
print('JS' in text)

if 'estudiantes' in text:
    print ('si somos estudiantes')
else:
    print ('soy profesor')


num_caracteres = len(text)
print(num_caracteres)

print(text)
print(text.upper())
print(text.lower())
print(text.count('e'))

print(text.replace('estudiantes','profesor')) 


