# coding:utf-8

def hoge():
  for x in 1, 2, 3, 4:
    # yieldは、その時点での値を返し、一時停止する
    yield x


x = hoge()

print x
print x.next()
print x.next()
print x.next()
print x.next()
# print x.next() #errorになる

