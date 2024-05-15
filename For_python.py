#Ciclos for

#for element in range(1,21):
#   print(element)

#list=[23,45,56,89,112]
#for element in list:
#    print(element)

#tupla=('45','56','67','90','UNOO')
#for element in tupla:
#    print(element)

#product={'nombre':'Tomates','precio':200,'inventario:':50}
#for key in product:
#    print(key,'=>',product[key])

#personas=[
#    {
#        'nombre':'Juan',
#        'edad':67
#    },
#    {
#        'nombre':'Pedro',
#        'edad':78
#    },
#    {
#        'nombre':'Ale',
#        'edad':12
#    }
#]
#for persona in personas:
#    print('nombres=>',persona['nombre'])
#    print('edad es=>',persona['edad'])

#ciclos matriz
matriz=[
    [1,3,4],
    [6,10,9],
    [8,7,6]
]
print(matriz[1][0])
for row in matriz:
    print(row)
    for column in row:
        print(column)