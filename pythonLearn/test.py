# a=100
# if a>=0:
#     print("True")
# else:
#     print("False")
# print('''Hello,
#       world''')

# a='ABC'
# b=a
# a='XYZ'
# print('b=',b,'a=',a)

# 格式化
# format
# f-string

classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))

#数组末尾追加
# a=classmates.append("Adam")
# print(classmates)

# a=classmates.insert(2,"Adam")
# print(classmates)

# a=classmates.pop()
# print(classmates)

# a=classmates.pop(1)
# print(classmates)

# tuple一旦初始化就不能修改,没有append等方法
# 定义tuple数组用()
# 
tuple1=(1,2,3,['2','3'])
print(tuple1)

# python中的switch case是case改成match xx:，只有match

# age=15

# match age:
#     case x if x<10:
#         print(f'<10:{x}')
#     case 10:
#         print()
#     case 11|12|13|14:
#         print()

# 循环
# 每个元素代入变量name，然后执行缩进块的语句
# names=['Michel','Bob','Tracy']
# for name in names:
#     print(name)

# range函数：生成一个整数序列

# 计算0-100的整数之和
# sum=0
# for x in range(101):
#     sum=sum+x
# print(sum)

# while循环
# sum=0
# n=99
# while n>0:
#     sum=sum+n
#     n=n-2
# print(sum)

# continue打印奇数
# n=0
# while n<10:
#     n=n+1
#     if n%2==0:
#         continue
#     print(n)
#     if n==7:
#         break

# dict在奇特语言中被称为map，使用键-值（key-value）存储，查找速度快
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 判断key中是否有value的两种方法
# dict的key必须是不可变对象
d={'amy':165,'bob':189}
print('Thomas' in d)
print(d.get('Tomas'))
print(d.get('Tomas',-1))

# 删除一个key的方法
d.pop('bob')
print(d)

# set和dict类似，也是一组key的集合，但不存储value
# 在set中，没有重复的key
# 无序和无重复元素
s=set([1,1,2,2,3,3,3,4])
print("s源数据=",s)

s.add(5)
print("s增加一个数据=",s)

s.remove(3)
print("s移除一个数据=",s)

# set可以做交集和并集
s1=set([1,2,3])
s2=set([2,3,4])
print("s交集数据=",s1&s2)
print("s并集数据=",s1|s2)

# 字符串str不可变，replace()方法作用在字符串对象上，没有改变原字符串对象，而是创建并返回一个新的字符串
a='ABC'
# 定义一个变量a，变量a指向字符串对象'ABC'

a='ABC'
b=a.replace('A','a')
print(b)
# replace()返回一个新的字符串'aBC'赋值给b，此时b指向新字符串'aBC'

# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，就保证了不可变对象本身永远是不可变的。

tupleTest=(1,2,[3,4])
a={'kkey11':tupleTest}
print(a['kkey11'])


