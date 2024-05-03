# and

print('--------AND--------')
print('True and True=> ', True and True)
print('True and False=> ', True and False)
print('False and True=> ', False and True)
print('False and False=> ', False and False)

print(10>6 and 6<5)
print(10==10 and 6==6)

# or

print('--------OR--------')
print('True or True=> ', True or True)
print('True or False=> ', True or False)
print('False or True=> ', False or True)
print('False or False=> ', False or False)

print(10>6 or 6<5)
print(10==10 or 6==6)
print(6>=6 or 9<=20)
print(24>45 or 2>7)


role = input('Digita tu rol: ')
print(role=='admin' or role=='vendedor')

role = input('Digita tu rol: ')
print(role=='admin' and role=='vendedor')

role = input('Digita tu rol: ')
print(role=='admin' and role=='admin')

role = input('Digita tu rol: ')
print(role=='admin' and role!='vendedor')

