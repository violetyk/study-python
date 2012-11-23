# coding:utf-8

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.address = None

Ore = Person('俺', 15)
Ore.address = 'Japan'
Ore.fuga = 'fugafuga'

print Ore.name
print Ore.age
print Ore.address
print Ore.fuga
