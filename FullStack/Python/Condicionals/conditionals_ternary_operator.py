role = 'guest'

auth = 'can access' if role == 'admin' else 'cannot access'

if role == 'admin':
  auth = 'can access'
else:
  auth = 'cannot access'

print(auth)

# Exercise Guide

language = "python"

language_check = True if language == 'python' else False