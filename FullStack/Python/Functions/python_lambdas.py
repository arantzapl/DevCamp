full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))


# Exercise Guide

def lambda_practice():
    greeting = lambda name: f'Hi, {name}'
    return greeting
  
greeting = lambda_practice()
print(greeting("Jordan"))