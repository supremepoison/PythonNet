import gevent

def foo(a,b):
    print('Running foo',a)
    gevent.sleep(2)
    print('Running foo again',b)

def bar():
    print('Running bar')
    gevent.sleep(3)
    print('Running bar again')


f = gevent.spawn(foo,1,2)
g = gevent.spawn(bar)

gevent.joinall([f,g])
