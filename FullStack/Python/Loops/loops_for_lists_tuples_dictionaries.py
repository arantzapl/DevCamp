players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
    print(player)


players = {
    '2b': 'Altuve',
    '3b': 'Bregman',
    'ss': 'Correa',
    'dh': 'Gattis'
}

for position, player in players.items():
    print("Position:", position)
    print("Player name:", player)



# Exercise Guide

def loop_over_list():
  my_list = ['Arantza', 'Alberto',   'Tere', 'Debora', 'Sergio']

  for name in my_list:
    print(name)

  return my_list

loop_over_list()