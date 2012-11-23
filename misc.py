# coding: utf-8

if None:
  print 'Noneは真'
else:
  print 'Noneは偽'


if False:
  print 'Falseは真'
else:
  print 'Falseは偽'

if 0:
  print '0は真'
else:
  print '0は偽'

if 0j:
  print '0jは真'
else:
  print '0jは偽'

if 0.0:
  print '0.0は真'
else:
  print '0.0は偽'


if '':
  print '空文字は真'
else:
  print '空文字は偽'

if []:
  print '[]は真'
else:
  print '[]は偽'


if ():
  print '()は真'
else:
  print '()は偽'


if {}:
  print '{}は真'
else:
  print '{}は偽'


if -1:
  print '-1は真'
else:
  print '-1は偽'

print int(1.5)
print round(3.141592, 3)
print round(1250, -2) #1300

print int('100')
print int('FF', 16) #基数を指定して変換
print float('1.0')

print str(1234)
print list('hoge')
print list('ほげ')

import sys
sys.stdout.write('改行')
sys.stdout.write('されない')

# 引数がリスト形式に入ってくる。sys.argv[0]はスクリプト自身
print sys.argv


# 三項演算子的な
r = '真' if 1 == 2  else '偽'
print r

# map
l = range(5)
print l
print map(str, l) #リストの各要素にstrを実行している。

print [str(x) for x in range(5)]


# filter
l = ['cat', 'doc', 'catalog']
print filter(lambda x: 'cat' in x, l) #catが含まれるものを返す関数xでフィルタしている。
print [x for x in l if 'o' in x] #oが含まれる物をフィルタしている

# タプル代入、リスト代入
c = (a,b) = (1,2)
print c
f = [d,e] = [3,4]
print f
f = [d,e] = (3,4)
print f

year, month, day = '2012/11/23'.split('/')
print year, month, day


# 例外 try except
try:
  print 'try!'
  raise Exception('エクセプション');

except Exception, e:
  print e
finally:
  print 'finaly!'



