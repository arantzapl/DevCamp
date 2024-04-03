class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def formatter(self):
    return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)
snapchat = Invoice('SnapChat', 200)

print(google.formatter())
print(snapchat.formatter())

# Exercise Guide

class Garage:
  def __init__(self, size):
    self.size = size

  def open_door(self):
    return "The door opens"
    
home = Garage(2)