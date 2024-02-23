# hex()把一个整数转换为十六进制表示的字符串
n1=255
print(hex(n1))

# 定义一个函数的例子
def my_abs(x):
# 类型检查
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
    
print(my_abs(-99))
print(my_abs('A'))

# 定义一个什么也不做的空函数,用pass语句
def nop():
    pass
