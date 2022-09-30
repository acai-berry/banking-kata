def a_func():
    container=[]
    container.append(1)
    print(container)

a_func()
a_func()

def a_func2(container=[]):
    container.append(1)
    print(container)

a_func2()
a_func2()
a_func2()