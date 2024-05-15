#CRUD Create Read Update Delete

numbers=[1,4,6,10]

#Read
print(numbers[3])

#Update
numbers[-1]=5
print(numbers)

#Append
numbers.append(32)
print(numbers)

#insert
numbers.insert(1,'UNO')
print(numbers)

numbers.insert(3,'TRES0')
print(numbers)

## Desarrollar un gestor de Tareas

task=['Tarea 1','Tarea 2','Tarea 3']
newlist=numbers+task
print(newlist)

newlist.remove('Tarea 1')
print(newlist)

#borra el último dato
newlist.pop()
print(newlist)

#borra el primer dato
newlist.pop(0)
print(newlist)

#vuelta a la lista
newlist.reverse()
print(newlist)

#cambio pos[1] por pos [3]
numbers_2=[1,67,8,6]
numbers_2.sort()
print(numbers_2)

list_string=['unos','cinco','as','ze']
list_string.sort()
print(list_string)
