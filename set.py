# coding:utf-8

set_a = set("abcde")
print set_a
# set(['a', 'c', 'b', 'e', 'd'])

set_b = set("bcd")

set(['c', 'b', 'd'])
print set_b
# set(['c', 'b', 'd'])

print set_a & set_b
# set(['c', 'b', 'd'])

print set_a | set_b
# set(['a', 'c', 'b', 'e', 'd'])

print set_a ^ set_b
# set(['a', 'e'])
