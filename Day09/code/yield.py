def fun():
    print('启动生成器')
    yield 1 
    print('生成器完成')
#生成器对象
g = fun()
#启动生成器
print(next(g))

#关闭生成器对象
g.close()