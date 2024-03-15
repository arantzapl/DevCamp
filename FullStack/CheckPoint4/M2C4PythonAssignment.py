from decimal import Decimal
import math

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

list_exer1 = [
    'listelement1',
    'listelement2',
    'listelement3'
    ]
tuple_exer1 = (
    'tuplelement1',
    'tuplelement2',
    'tuplelement3'
    )
float_exer1 = 4/9
inte_exer1 = 52
deci_exer1 = Decimal(4/9)
dict_exer1 = {
    'dict1': 'element1',
    'dict2': 'element2',
    'dict3': 'element3'
    }

print(list_exer1)
print(tuple_exer1)
print(float_exer1)
print(inte_exer1)
print(deci_exer1)
print(dict_exer1)

# Exercise 2: Round your float up.

float_exer2 = 24.6
print(math.ceil(float_exer2))

# Exercise 3: Get the square root of your float.

float_exer3 = 24.66

print(math.sqrt(float_exer3))

# Exercise 4: Select the first element from your dictionary.

dict_exer4 = {
    'dict1': 'element1',
    'dict2': 'element2',
    'dict3': 'element3',
    'dict4': 'element4',
    'dict5': 'element5'
    }

dict_exer4 = dict_exer4.items()

print(list(dict_exer4)[0])

# Exercise 5: Select the second element from your tuple.

tuple_exer5 = (
    'tuplelement1',
    'tuplelement2',
    'tuplelement3',
    'tuplelement4',
    'tuplelement5'
    )

print(tuple_exer5[1])

# Exercise 6: Add an element to the end of your list.

list_exer6 = [
    'listelement1',
    'listelement2',
    'listelement3'
    ]

list_exer6.extend(['listelement4'])

print(list_exer6)

# Exercise 7: Replace the first element in your list.

list_exer7 = [
  'listelement1',
  'listelement2',
  'listelement3'
  ]

print(list_exer7)

list_exer7[0] = 'listelement4'

print(list_exer7)

# Exercise 8: Sort your list alphabetically.

list_exer8 = [
    'listelement5',
    'listelement2',
    'listelement7',
    'listelement3',
    'listelement6',
    'listelement1',
    'listelement4'
    ]

list_exer8.sort()

print(list_exer8)

# Exercise 9: Use reassignment to add an element to your tuple.

tuple_exer9 = (
    'tuplelement1',
    'tuplelement2',
    'tuplelement3',
    'tuplelement4',
    'tuplelement5'
    )

print(tuple_exer9)

tuple_exer9 += ('tuplelement6', )

print(tuple_exer9)