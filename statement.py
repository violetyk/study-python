# coding:utf-8

str = 'python'


if str == 'PYTHON':
  print 'PYTHON!'
elif str == 'python':
  print 'python!'
else:
  print 'False!'

# 同じ深さのインデントが同じブロックになる
print '-----'
i = 0
while i < 5:
  i += 1
  print i
print i


# 無限ループ
# while i:
  # print '.'


# for 文
print '-----'
k = 0
for k in xrange(5):
  print k

# rangeは最初にリストをつくって返す関数。
# xrangeは呼ばれる度に数を返すジェネレータ。
# なので、範囲が大きいときにはxrangeの方がいいらしい。


