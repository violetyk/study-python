# coding:utf-8

# 辞書の全てのキーと値をたどる | items(), keys(), values()メソッドの使い方

# 辞書の初期化
profile = { 'Hana':19, 'Toru':26, 'Katori':15, 'Sato':45}
print profile, '\n'


# 辞書のitems()メソッドで全てのキー(key), 値(value)をたどる
for k, v in profile.items():   # for/if文では文末のコロン「:」を忘れないように
  print k, v

# items()メソッドの戻り値
print 'items():', profile.items(), '\n'    # keyとvalueのタプルのリストを返している


# 辞書のkeys()メソッドで全てのキーをたどる
for k in profile.keys():
  print 'key:', k
# keys()メソッドの戻り値
print 'keys():', profile.keys(), '\n'      # keyリストを返している

# 辞書のvalues()メソッドで全ての値をたどる
for v in profile.values():
 print 'value:', v
# values()メソッドの戻り値
print 'values():', profile.values(), '\n'  # valueのリストを返している


fuga = [hoge for _, _, hoge in [(10,20,30), (21,22,23)]]
print fuga
# [30, 23]
