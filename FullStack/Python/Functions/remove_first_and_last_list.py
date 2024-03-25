"""
remove_first_and_last(list_to_clean)

html = ['<h1>', 'Some content', </h1>]

remove_first_and_last(html)
=> ['Some content']

html_2 = ['<h1>', 'Some content', 'more', </h1>]

remove_first_and_last(html)
=> ['Some content', 'more']


one, *two, three = [1, 2, 3, 4, 5]
one = 1
two = [2, 3, 4]
three = 5

"""


def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content


html = ['<h1>', 'My content', '</h1>']

print(remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']

print(remove_first_and_last(other_content_to_clean))