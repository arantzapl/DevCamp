def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')

# Exercise Guide

def greeting(person):
    return f'Hello, {person}'

print(greeting('Jordan'))