def func():
    global a    #局部变量提升为全局函数，定义不能赋初始值，调用该函数后该全局变量才存在
    a = 100
    print("a的值：{0}".format(a))

print("aaaa")

func()
print(a)


# x = input("cmd:")
# print(eval(x))

# help(eval)

l = [1,43,56,788888,1]

print(l)