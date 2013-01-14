# coding:utf-8

# こう宣言しないとSyntaxError: Non-ASCII characterがでちゃう

# Hello, Python!
print 'hello'
print 'hello', 'pythoh'
print '''line1
line2
line3
'''

print u"aaa\nbbb" # unicode文字列
print r"aaa\nbbb" # raw文字列


# 変数に型を付けなくていい。jを付けると虚数
print '----------'
a = 1
a = 3.14
a = 1 + 1j
print a


# ++や--がない
print '----------'
i = 1
i += 1
print i
i -= 1
print i

# 四則演算
print '----------'

x = 3
y = 2

print x + y
print x - y
print x * y
print x / y
print x % y
print x ** y #xのy乗
x = 3.0 #どっちかが小数なら結果も小数
print x / y


# 論理演算
print '----------'
x = 0
y = -1

print x or y #xが偽ならy、そうでなければx
print x and y #xが偽ならx、そうでなければy
print not x # xが偽ならTrue、そうでなければFalse
print not y


# sprintfてきな
str_hoge = 'hoge'
str_fuga = 'fuga'
print '----------'
print '%s です' % str_hoge
print '%s %sです' % (str_hoge, str_fuga)
print '{1} {0} です'.format(str_hoge, str_fuga)


# 文字列操作
print '----------'
print 'hoge' + 'fuga'
print ','.join(['aaa', 'bbb', 'ccc'])

print 'aaa bbb ccc'.split()
print 'aaa,bbb,ccc'.split(',')

print len('hogehoge')
print len('ほげほげ')

print '0123456789'[:3]
print '0123456789'[3:6]
print '0123456789'[6:]

print 'abcd'.find('cd')
print 'abcd'.find('ef')


print '### リスト []：他の言語の配列。何でも入る。'
list1 = []
list2 = list()
list3 = [0,1,2]
list4 = list(list3) # copy
print list4
print range(3)
print range(3, 6)
print range(1, 9, 2) # 1 以上 9未満。2ごと
print range(1, 9, 3) # 1 以上 9未満。3ごと

# リスト参照
print '----------'
list3[1] = 3
print list3[1] # リストの参照
print list3
print len(list3)

# リスト操作
print '----------'
list5 = range(1, 5)
print list5
print list5.pop(0) # index 0 をpop
print list5.pop() # 末尾をpop
list5.insert(0, 6)
print list5
list5.append(7)
print list5

list5.extend([8,9]) # 末尾にリストを追加
print list5


# タプル ()：要素の追加変更削除ができない。関数から値を返したいときによく使う。
print '----------'
tuple1 = ()
tuple2 = tuple()
print tuple1, tuple2
tuple3 = (1)
tuple4 = (1,)
print tuple3, tuple4
tuple5 = (0, '1', 2, [3], -4)
print tuple5

print tuple5[3]
print len(tuple5)


# ディクショナリ {}：いわゆる連想配列。数値、文字、タプルなどが入る。
print '----------'
dic = {}
dic = {
  "a":1,
  "b":2,
}

dic["c"] = 3
print dic
print dic.keys()
print dic.values()
print 'b' in dic

del dic['b'] # 下記でも同じだった
# del(dic['b'])
print dic

