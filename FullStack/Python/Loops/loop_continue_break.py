usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
    if username == 'cersei':
        print(f'Sorry, {username}, you are not allowed')
        continue
    else:
        print(f'{username} is allowed')

for username in usernames:
    if username == 'cersei':
        print(f'{username} was found at index {usernames.index(username)}')
        break
    print(username)

# Exercise Guide
    
def loop_and_break():
    vegetables = ["onion", "broccoli", "apple", "spinach"]

    for vegetable in vegetables:
        if vegetable == 'apple':
            print(f'{vegetable} is not a vegetable')
            break
        print(vegetable)

    return vegetables

loop_and_break()