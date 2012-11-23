# coding:utf-8

def my_func1(a, b):
  return a + b

def my_func2(a):
  a += 1
  return


print my_func1(1,2)
print my_func2(1) # returnがない場合にはNoneが返る。


# lambda式で無名関数
print '------'

hoge = lambda x, y: x + y
print hoge(2,3)


# ファイル入出力
f1 = open('data.txt')
f2 = open('copy.txt', 'w')

for line in f1:
  f2.write(line)

f1.close();
f2.close();


