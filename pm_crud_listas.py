# CRUD Create Read Update Delete

# Create
numbers = [1,4,6,10]

# Read
print(numbers[3])

# Update
print(numbers)

numbers[-1] = 5
print(numbers)

numbers.append(20)
print(numbers)

# Insert 
numbers.insert(1,'UNO')
print(numbers)

numbers.insert(3,'Tres')
print(numbers)

## Desarrollar un gestor de Tareas

taks = ['Tarea 1', 'Tarea 2', 'Tarea 3']
newlist = numbers + taks
print(newlist)

newlist.remove('Tarea 1')
print(newlist)

newlist.pop()
print(newlist)

newlist.pop(0)
print(newlist)

newlist.reverse()
print(newlist)

numbers_2 = [1,67,8,6]
numbers_2.sort()
print(numbers_2)

list_string = ['unos', 'cinco', 'as', 'ze']
list_string.sort()
print(list_string)

