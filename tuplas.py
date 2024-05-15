numbers = [1,4,5,6,7,8]
strings = ('Uno','Dos','Tres','Cuatro')

print(numbers)

print('2=>',numbers[2])

print(type(numbers))

print('3=>',strings[3])
print(type(strings))

print(strings.index('Dos'))

print(strings.count('Dos'))


###Tupla en una lista

list_tupla=list(numbers)
print(list_tupla)
print(type(list_tupla))

new_tupla=tuple(list_tupla)
print(new_tupla)
print(type(new_tupla))