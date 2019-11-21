
# *args 和 **kwargs使用


```python
def test_var_args(f_arg, *argv): 
    print("first normal arg:", f_arg) 
    for arg in argv: 
        print("another arg through *argv:", arg) 
test_var_args('yasoob', 'python', 'eggs', 'test')
```

    first normal arg: yasoob
    another arg through *argv: python
    another arg through *argv: eggs
    another arg through *argv: test



```python
def greet_me(**kwargs): 
    for key, value in kwargs.items(): 
        print("{0} == {1}".format(key, value))
greet_me(name="yasoob",a='b')
```

    name == yasoob
    a == b



```python
def test_args_kwargs(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3)
```


```python
test_args_kwargs(*("two", 3, 5))
```

    arg1: two
    arg2: 3
    arg3: 5



```python
test_args_kwargs(*["two", 3, 5])
```

    arg1: two
    arg2: 3
    arg3: 5



```python
test_args_kwargs(**{"arg3": 3, "arg2": "two", "arg1": 5})
```

    arg1: 5
    arg2: two
    arg3: 3


# 调试 Debugging
> - https://docs.python.org/3/library/pdb.html
> - 在命令⾏使⽤Python debugger运⾏⼀个脚本， 举个例⼦： $ python -m pdb my_script.py

下面的脚本运⾏后，你会在运⾏时马上进⼊debugger模式。
现在是时候了解下 debugger模式下的⼀些命令了。 
命令列表：
- c: 继续执⾏ 
- w: 显⽰当前正在执⾏的代码⾏的上下⽂信息 
- a: 打印当前函数的参数列表 
- s: 执⾏当前代码⾏，并停在第⼀个能停的地⽅（相当于单步进⼊） 
- n: 继续执⾏到当前函数的下⼀⾏，或者当前⾏直接返回（单步跳过） 
- q(uit) Quit from the debugger. The program being executed is aborted.
- display [expression] Display the value of the expression if it changed, each time execution stops in the current frame.
- j(ump) lineno Set the next line that will be executed. 
- h(elp) [command]

**单步跳过（next）和单步进⼊（step）的区别**
- **单步进⼊会进⼊当前⾏调⽤的函数内 部并停在⾥⾯**
- **单步跳过会（⼏乎）全速执⾏完当前⾏调⽤的函数，并停在当前函数的 下⼀⾏**


```python
import pdb 
def make_bread(): 
    pdb.set_trace() 
    return "I don't have time" 

def test_args_kwargs(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    pdb.set_trace() 
    print("arg3:", arg3)
print(test_args_kwargs("two", 3, 5))
```

    arg1: two
    arg2: 3
    > <ipython-input-7-de373a91321d>(10)test_args_kwargs()
    -> print("arg3:", arg3)
    (Pdb) q



    ---------------------------------------------------------------------------

    BdbQuit                                   Traceback (most recent call last)

    <ipython-input-7-de373a91321d> in <module>
          9     pdb.set_trace()
         10     print("arg3:", arg3)
    ---> 11 print(test_args_kwargs("two", 3, 5))
    

    <ipython-input-7-de373a91321d> in test_args_kwargs(arg1, arg2, arg3)
          8     print("arg2:", arg2)
          9     pdb.set_trace()
    ---> 10     print("arg3:", arg3)
         11 print(test_args_kwargs("two", 3, 5))


    <ipython-input-7-de373a91321d> in test_args_kwargs(arg1, arg2, arg3)
          8     print("arg2:", arg2)
          9     pdb.set_trace()
    ---> 10     print("arg3:", arg3)
         11 print(test_args_kwargs("two", 3, 5))


    ~/anaconda3/lib/python3.7/bdb.py in trace_dispatch(self, frame, event, arg)
         86             return # None
         87         if event == 'line':
    ---> 88             return self.dispatch_line(frame)
         89         if event == 'call':
         90             return self.dispatch_call(frame, arg)


    ~/anaconda3/lib/python3.7/bdb.py in dispatch_line(self, frame)
        111         if self.stop_here(frame) or self.break_here(frame):
        112             self.user_line(frame)
    --> 113             if self.quitting: raise BdbQuit
        114         return self.trace_dispatch
        115 


    BdbQuit: 


# Generator 生成器
## 基本概念
### 可迭代对象 Iterable

Python中任意的对象，只要它定义了可以返回⼀个迭代器的`__iter__`⽅法，或者定义了 可以⽀持下标索引的`__getitem__`⽅法，那么它就是⼀个可迭代对象。简单说，可迭代对象就是能提供迭代器的任意对象。

### 迭代器 iteration

任意对象，只要定义了`next`(Python2) 或者`__next__`⽅法，它就是⼀个迭代器

### 迭代
⽤简单的话讲，它就是从某个地⽅（⽐如⼀个列表）取出⼀个元素的过程。当我们使⽤⼀ 个循环来遍历某个东西时，这个过程本⾝就叫迭代

### ⽣成器(Generators) 
⽣成器也是⼀种迭代器，但是你**只能对其迭代⼀次**。这是因为它们并**没有把所有的值存在内存中，⽽是在运⾏时⽣成值**。你通过遍历来使⽤它们，要么⽤⼀个“for”循环，要么将它们传递给任意可以进⾏迭代的函数和结构。

⼤多数时候⽣成器是以函数来实现的。然⽽， 它们并不返回⼀个值，⽽是yield(暂且译作“⽣出”)⼀个值


**⽣成器最佳应⽤场景是**：
你不想同⼀时间将所有计算出来的⼤ 量结果集分配到内存当中，特别是结果集⾥还包含循环


```python
def generator_function(): 
    for i in range(5): 
        yield i 

for item in generator_function(): 
    print(item)
```

    0
    1
    2
    3
    4


下⾯是⼀个计算斐波那契数列的⽣成器： # generator version 


```python
def fibon(n): 
    a = b = 1 
    for i in range(n): 
        yield a 
        a, b = b, a + b 
for x in fibon(5): 
    print(x)
```

    1
    1
    2
    3
    5


string是一个可迭代对象 Iterable，但不是一个迭代器iteration


```python
my_string = "Yasoob" 
my_iter = iter(my_string) 
for c in my_iter:
    print(c)
```

    Y
    a
    s
    o
    o
    b


# Map，Filter 和 Reduce

**注意**：如果map和filter对你来说看起来并不优雅的话，那么你可以看看另外⼀章：列 表/字典/元组推导式。

## Map
Map会将⼀个函数映射到⼀个输⼊列表的所有元素上。

这是它的规范： 

```python 
map(function_to_apply, list_of_inputs) 
```

⼤多数时候，我们要把列表中所有元素⼀个个地传递给⼀个函数，并收集输出
> - 在python2中map直接返回列表，但在python3中返回迭代器 # 因此为了兼容python3, 需要list转换⼀下
> - ⼤多数时候，使⽤匿名函数(lambdas)来配合map,


```python
items = [1, 2, 3, 4, 5]
list(map(lambda x: x**2, items))
```




    [1, 4, 9, 16, 25]




```python
[x**2 for x in items]
```




    [1, 4, 9, 16, 25]




```python
def multiply(x): 
    return (x*x) 

def add(x): 
    return (x+x) 

funcs = [multiply, add] 

for i in range(5): 
    value = map(lambda x: x(i), funcs) 
    print(list(value))
```

    [0, 0]
    [1, 2]
    [4, 4]
    [9, 6]
    [16, 8]


## Filter 
filter过滤列表中的元素，并且返回⼀个由所有符合要求的元素所构成的列 表，

符合要求即函数映射到该元素时返回值为True


```python
number_list = range(-5, 5) 
print(list(filter(lambda x: x < 0, number_list)))
```

    [-5, -4, -3, -2, -1]



```python
[x for x in number_list if x < 0]
```




    [-5, -4, -3, -2, -1]




```python
for i in (x for x in number_list if x < 0):
    print(i)
```

    -5
    -4
    -3
    -2
    -1


## Reduce
当需要对⼀个列表进⾏⼀些计算并返回结果时，Reduce 是个⾮常有⽤的函数


```python
from functools import reduce 
reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
```




    24



# set(集合)数据结构


```python
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n'] 
duplicates = [] 
for value in some_list: 
    if some_list.count(value) > 1: 
        if value not in duplicates: 
            duplicates.append(value) 
print(duplicates)
```

    ['b', 'n']


更简单更优雅的解决⽅案，那就是使⽤集合(sets)


```python
duplicates = set([x for x in some_list if some_list.count(x) > 1]) 
print(duplicates)
```

    {'n', 'b'}


## 交集
注意：valid可以是list,set类型


```python
valid = ['yellow', 'red', 'blue', 'green', 'black'] 
input_set = set(['red', 'brown']) 
print(input_set.intersection(valid))
```

    {'red'}


## 差集


```python
valid = ['yellow', 'red', 'blue', 'green', 'black']
input_set = set(['red', 'brown']) 
print(input_set.difference(valid))
```

    {'brown'}


## ⽤符号来创建集合


```python
a_set = {'red', 'blue', 'green'} 
print(type(a_set))
```

    <class 'set'>


# 三元运算符
```python
用法1：
#如果条件为真，返回真 否则返回假 
condition_is_true if condition else condition_is_false

用法2： 最好尽量避免使⽤元组条件表达式
#(返回假，返回真)[真或假] 
#之所以能正常⼯作，是因为在Python中，True等于1，⽽False等于0，这就相当于在元组 中使⽤0和1来选取数据
(if_test_is_false, if_test_is_true)[test]
```


```python
is_fat = True 
state = "fat" if is_fat else "not fat"
state
```




    'fat'




```python
fat = True 
fitness = ("skinny", "fat")[fat] 
print("Ali is ", fitness)
```

    Ali is  fat


# 装饰器
装饰器(Decorators)是Python的⼀个重要部分。简单地说：他们是修改其他函数的功能的函数。他们有助于让我们的代码更简短

## ⼀切皆对象
在python中，函数是一个对象，可以将⼀个函数赋值给⼀个变量

## 在函数中定义函数
可以创建嵌套的函数


```python
def hi(name="yasoob"): 
    print("now you are inside the hi() function") 
    def greet(): 
        return "now you are in the greet() function" 
    def welcome(): 
        return "now you are in the welcome() function" 
    print(greet()) 
    print(welcome()) 
    print("now you are back in the hi() function")
    
hi()
```

    now you are inside the hi() function
    now you are in the greet() function
    now you are in the welcome() function
    now you are back in the hi() function


## 从函数中返回函数


```python
def hi(name="yasoob"): 
    def greet(): 
        return "now you are in the greet() function" 
    def welcome(): 
        return "now you are in the welcome() function" 
    if name == "yasoob": 
        return greet 
    else:
        return welcome
    
a = hi()
print(a())
```

    now you are in the greet() function



```python
a = hi(name = "ali")
print(a())
```

    now you are in the welcome() function


## 将函数作为参数传给另⼀个函数


```python
def hi(): 
    return "hi yasoob!" 
def doSomethingBeforeHi(func): 
    print("I am doing some boring work before executing hi()") 
    print(func()) 
doSomethingBeforeHi(hi)
```

    I am doing some boring work before executing hi()
    hi yasoob!


## 装饰器


```python
def a_new_decorator(a_func): 
    def wrapTheFunction(): 
        print("I am doing some boring work before executing a_func()")
        a_func() 
        print("I am doing some boring work after executing a_func()" )
    return wrapTheFunction 
              
def a_function_requiring_decoration(): 
    print("I am the function which needs some decoration to remove my foul smell" )
    

a_function_requiring_decoration()
```

    I am the function which needs some decoration to remove my foul smell



```python
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
```

    I am doing some boring work before executing a_func()
    I am the function which needs some decoration to remove my foul smell
    I am doing some boring work after executing a_func()



```python
@a_new_decorator 
def a_function_requiring_decoration(): 
    """Hey you! Decorate me!""" 
    print("I am the function which needs some decoration to " "remove my foul smell") 
    
a_function_requiring_decoration()
```

    I am doing some boring work before executing a_func()
    I am the function which needs some decoration to remove my foul smell
    I am doing some boring work after executing a_func()



```python
print(a_function_requiring_decoration.__name__)
```

    wrapTheFunction


**解决函数的名字和注释⽂档(docstring)被装饰重写的问题**

注意：@wraps接受⼀个函数来进⾏装饰，并加⼊了复制函数名称、注释⽂档、参数列表 等等的功能。这可以让我们在装饰器⾥⾯访问在装饰之前的函数的属性


```python
from functools import wraps
def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction(): 
        print("I am doing some boring work before executing a_func()")
        a_func() 
        print("I am doing some boring work after executing a_func()" )
    return wrapTheFunction 

@a_new_decorator 
def a_function_requiring_decoration(): 
    """Hey you! Decorate me!""" 
    print("I am the function which needs some decoration to " "remove my foul smell") 
    
print(a_function_requiring_decoration.__name__)
```

    a_function_requiring_decoration


## 装饰器编写模板


```python
from functools import wraps 
def decorator_name(f): 
    @wraps(f) 
    def decorated(*args, **kwargs): 
        if not can_run: 
            return "Function will not run" 
        return f(*args, **kwargs) 
    return decorated 

@decorator_name 
def func(): 
    return("Function is running") 
can_run = True 
print(func())
```

    Function is running



```python
can_run = False 
print(func())
```

    Function will not run


## 装饰器使用场景

### 授权(Authorization)
装饰器能有助于检查某个⼈是否被授权去使⽤⼀个web应⽤的端点(endpoint)。它们被⼤量 使⽤于Flask和Django web框架中。这⾥是⼀个例⼦来使⽤基于装饰器的授权


```python
from functools import wraps 
def requires_auth(f):
    @wraps(f) 
    def decorated(*args, **kwargs): 
        auth = request.authorization 
        if not auth or not check_auth(auth.username, auth.password): 
            authenticate() 
        return f(*args, **kwargs) 
    return decorated
```

### ⽇志(Logging)
⽇志是装饰器运⽤的另⼀个亮点


```python
from functools import wraps 

def logit(func): 
    @wraps(func) 
    def with_logging(*args, **kwargs): 
        print(func.__name__ + " was called") 
        return func(*args, **kwargs) 
    return with_logging 

@logit 
def addition_func(x): 
    """Do some math.""" 
    return x + x 

result = addition_func(4)
result
```

    addition_func was called





    8



## 带参数的装饰器

### 在函数中嵌⼊装饰器


```python
from functools import wraps 

def logit(logfile='out.log'): 
    def logging_decorator(func): 
        @wraps(func) 
        def wrapped_function(*args, **kwargs): 
            log_string = func.__name__ + " was called" 
            print(log_string) 
            # 打开logfile，并写⼊内容 
            with open(logfile, 'a') as opened_file: 
                # 现在将⽇志打到指定的logfile 
                opened_file.write(log_string + '\n') 
            return func(*args, **kwargs) 
        return wrapped_function 
    return logging_decorator

@logit() 
def myfunc1(): 
    pass

myfunc1()
```

    myfunc1 was called



```python
@logit(logfile='func2.log') 
def myfunc2(): 
    pass

myfunc2()
```

    myfunc2 was called


现在⼀个叫做 func2.log 的⽂件出现了，⾥⾯的内容就是上⾯的字符串

### 装饰器类


```python
from functools import wraps 

class logit_c(object): 
    def __init__(self, logfile='out.log'): 
        self.logfile = logfile
        
    def __call__(self, func): 
        @wraps(func) 
        def wrapped_function(*args, **kwargs): 
            log_string = func.__name__ + " was called" 
            print(log_string) 
            # 打开logfile并写⼊ 
            with open(self.logfile, 'a') as opened_file: 
                # 现在将⽇志打到指定的⽂件 
                opened_file.write(log_string + '\n') 
            # 现在，发送⼀个通知 
            self.notify() 
            return func(*args, **kwargs) 
        return wrapped_function
        
    def __get__(self,instance,cls):
        print('xxx')
        if instance is None:
            return self
        else:
            return types.MethodType(self,instance)
        
    def notify(self): 
        # logit只打⽇志，不做别的,针对异常可以发邮件通知 
        pass
    
@logit_c(logfile='out3.log') 
def myfunc3():
    pass

myfunc3()
```

    myfunc3 was called



```python
class email_logit(logit_c): 
    ''' 
    ⼀个logit的实现版本，可以在函数调⽤时发送email给管理员 
    '''
    def __init__(self, email='admin@myproject.com',*args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)
        
    def notify(self): 
        # 发送⼀封email到self.email # 这⾥就不做实现了 
        pass
    
@email_logit(logfile='out4.log') 
def myfunc4():
    pass

myfunc4()
```

    myfunc4 was called


# Global和Return
> - Global 全局变量，即使在函数内部定义，在函数以外的区域都能访问，但它引⼊了多余的变量到全局作⽤域，**不建议使用**
> - Return 将函数内部定义的局部变量 值赋给了调⽤函数的变量


```python
def add(value1, value2):
    return value1 + value2

result = add(3, 5)
result
```




    8




```python
def add(value1,value2):
    global result
    result = value1 + value2

add(3,5)
print(result)
```

    8



```python
def profile():
    name = "Danny"
    age = 30
    return name, age

name,age=profile()
print(name,age)
```

    Danny 30


# 可变(mutable)与不可变(immutable)的数据类型

## 什么是不可变类型？
存储空间保存的数据不允许被修改，这种数据就是不可变类型。

常见的不可变类型有:
> - 数字类型 int, bool, float, complex, long(2.x)
> - 字符串 str
> - 元组 tuple

## 什么是可变类型？
存储空间保存的数据允许被修改，这种数据就是可变类型。

常见的可变类型有:

> - 列表 list
> - 字典 dict
> - 集合 set

***需要注意***，可变类型通过方便改变数据才是修改内存中的数据，使用赋值`=`号并不是修改内存中的数据，而是开辟出一块新的空间来存放新的数据


```python
def add_to(element, target=None): 
    if target is None: 
        target = [] 
    target.append(element) 
    return target
add_to(42)
```




    [42]




```python
add_to(42)
```




    [42]



通过方法来修改的字典或者列表，其内存地址是不变了，也说明了字典列表是可变的


```python
demo_list = [1, 2, 3]
print("定义列表后的内存地址 %d,%s" % (id(demo_list),str(demo_list)))
demo_list.append(999)
demo_list.pop(0)
demo_list.remove(2)
demo_list[0] = 10
print("修改数据后的内存地址 %d,%s" % (id(demo_list),str(demo_list)))

demo_dict = {"name": "小明"}
print("定义字典后的内存地址 %d,%s" % (id(demo_dict),str(demo_dict)))
demo_dict["age"] = 18
demo_dict.pop("name")
demo_dict["name"] = "老王"
print("修改数据后的内存地址 %d,%s" % (id(demo_dict),str(demo_dict)))
```

    定义列表后的内存地址 139668719525832,[1, 2, 3]
    修改数据后的内存地址 139668719525832,[10, 999]
    定义字典后的内存地址 139668718533584,{'name': '小明'}
    修改数据后的内存地址 139668718533584,{'age': 18, 'name': '老王'}


**说明** `=`赋值运算符是重新为变量指向一个新的内存地址，而不是修改原来内存的数据，注意与上例区别好。


```python
a = 1
print(id(a))
a = "hello"
print(id(a))
a = [1, 2, 3]
print(id(a))
a = [3, 2, 1]
print(id(a))
```

    139669362193440
    139668719842560
    139668718468744
    139668771800456


## 字典的key与哈希
字典的键必须是不可变类型数据，而值则可以是任意类型的数据。

这是因为不可变类型的数据才会有哈希值，而字典的键必须要有对应的哈希值。

Python中有一个内置函数hash(o)可以接受一个不可变类型数据作为参数，返回一个整数，这个整数可以看成是该数据的特征码，
因此，相同的数据内容得到相同的整数，而不同的数据内容则得到不同的整数。

另外
> - **由于列表是不可哈希类型的，因此决定了它的有序性，可重复性。**
> - **由于字典、集合是可哈希类型的，因此具有不可重复，无序性。**

# __slots__魔法

在Python中，每个类都有实例属性。默认情况下Python⽤⼀个字典来保存⼀个对象的实例属性。

这⾮常有⽤，因为它允许我们在运⾏时去设置任意的新属性。

然⽽，对于有着已知属性的⼩类来说，它可能是个瓶颈。**这个字典浪费了很多内存。 Python不能在对象创建时直接分配⼀个固定量的内存来保存所有的属性**。

因此如果你创建许多对象（我指的是成千上万个），它会消耗掉很多内存。 
不过还是有⼀个⽅法来规避这个问题。这个⽅法需要**使⽤`__slots__`来告诉Python不要使 ⽤字典，⽽且只给⼀个固定集合的属性分配空间**。

**[ipython_memory_usage](https://github.com/ianozsvald/ipython_memory_usage)**的安装，用法参见官网


```python
class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
```


```python
class MyClassWithSlots(object): 
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
```


```python
import ipython_memory_usage.ipython_memory_usage as imu
import sys
```


```python
imu.start_watching_memory()
```

    In [53] used 0.0117 MiB RAM in 0.11s, peaked 0.00 MiB above current, total RAM usage 67.91 MiB



```python
num = 1024*256
x = [MyClassWithSlots(1,1) for i in range(num)]
sys.getsizeof(x)
```




    2115952



    In [54] used 15.9805 MiB RAM in 0.31s, peaked 0.00 MiB above current, total RAM usage 83.89 MiB



```python
num = 1024*256
x = [MyClass(1,1) for i in range(num)]
sys.getsizeof(x)
```




    2115952



    In [55] used 29.8945 MiB RAM in 0.44s, peaked 4.05 MiB above current, total RAM usage 113.79 MiB



```python
imu.stop_watching_memory()
```

# virtualenv 虚拟的独⽴(隔离)的Python环境

   [virtualenvs 文档](https://virtualenv.pypa.io/en/latest/userguide/)

```bash
 #安装virtualevn
  pip install virtualenv
 
 #创建一个虚拟环境  ⽤--system-site-packages 让虚拟环境使用全局系统模块
  virtualenv --system-site-packages myenv
 #激活虚拟环境
  cd myenv
  source bin/activate
  
 #退出虚拟环境
  deactivate
  
```

# 容器 Collections

Python附带⼀个模块，它包含许多容器数据类型，名字叫作collections

## defaultdict
与```dict```类型不同，你不需要检查**key**是否存在

```python
class collections.defaultdict([default_factory[, ...]])
'''
Returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method and adds one writable instance variable. The remaining functionality is the same as for the dict class and is not documented here.
'''
```


```python
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)
```

    defaultdict(<class 'list'>, {'Yasoob': ['Yellow', 'Red'], 'Ali': ['Blue', 'Black'], 'Arham': ['Green'], 'Ahmed': ['Silver']})


当你在一个字典中对一个键进行嵌套赋值时，如果这个键不存在，会触发```keyError```异常


```python
some_dict = {}
some_dict['colours']['favourite'] = "yellow"
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-58-6221372f06f1> in <module>
          1 some_dict = {}
    ----> 2 some_dict['colours']['favourite'] = "yellow"
    

    KeyError: 'colours'


使用```defaultdict```的解决使用```dict```触发```KeyError```的问题


```python
import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"

import json
print(json.dumps(some_dict))
```

    {"colours": {"favourite": "yellow"}}



```python
import collections
def tree2():
    return collections.defaultdict(tree)
some_dict = tree2()
some_dict['colours']['favourite'] = "yellow"

import json
print(json.dumps(some_dict))
```

    {"colours": {"favourite": "yellow"}}


指定其它function_factory


```python
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
list(d.items())
```




    [('m', 1), ('i', 4), ('s', 4), ('p', 2)]



## counter
Counter是一个计数器，它可以帮助我们针对某项数据进行计数。比如它可以用来计算每个人喜欢多少种颜色：


```python
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)
```

    Counter({'Yasoob': 2, 'Ali': 2, 'Arham': 1, 'Ahmed': 1})



```python
Counter([2,3,4,7,2,4,8,7])
```




    Counter({2: 2, 3: 1, 4: 2, 7: 2, 8: 1})



利用它统计一个文件，相同内容的行数


```python
with open('out4.log', 'rb') as f:
    line_count = Counter(f)
print(line_count)
```

    Counter({b'myfunc3 was called\n': 5, b'myfunc4 was called\n': 3})


## deque
deque提供了一个双端队列，你可以从头/尾两端添加或删除元素。要想使用它，首先我们要从```collections```中导入```deque```模块：


```python
from collections import deque
d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
print(d[0])
print(d[-1])


d = deque(range(5))
print(len(d))
d.popleft()
d.pop()
print(d)

#可以限制这个列表的⼤⼩,现在当你插入30条数据时，最左边一端的数据将从队列中删除。
d = deque(maxlen=30)

d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)
```

    3
    1
    3
    5
    deque([1, 2, 3])
    deque([0, 1, 2, 3, 4, 5, 6, 7, 8])


## namedtuple

⼀个元组是⼀个不可变的列表，你可以存储⼀个数据的序列，它和命名元组 (namedtuples)⾮常像，

但有⼏个关键的不同。 主要相似点是都不像列表，你不能修改元组中的数据。为了获取元组中的数据，你需要使 ⽤整数作为索引：

那namedtuples是什么呢？它把元组变成⼀个针对简单任务的容器。你不必使⽤整数索引来访问⼀个namedtuples的数据。

你可以像字典(dict)⼀样访问namedtuples， 但namedtuples是不可变的

**```namedtuple```的每个实例没有对象字典**，所以它们很轻量，与普通的元组比，并不需要更多的内存。这使得它们比字典更快。


```python
man = ('Ali', 30) 
print(man[0])
```

    Ali



```python
from collections import namedtuple

Animal = namedtuple('Animal', ('name','age','type'))
perry = Animal(name="perry", age=31, type="cat")

print(perry)
print(perry.name,perry.age,perry[1])

print(perry._asdict())
```

    Animal(name='perry', age=31, type='cat')
    perry 31 31
    OrderedDict([('name', 'perry'), ('age', 31), ('type', 'cat')])


要记住它是一个元组，属性值在```namedtuple```中是不可变的，所以下面的代码不能工作


```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
perry.age = 42
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-69-4e145e02a442> in <module>
          3 Animal = namedtuple('Animal', 'name age type')
          4 perry = Animal(name="perry", age=31, type="cat")
    ----> 5 perry.age = 42
    

    AttributeError: can't set attribute


## enum.Enum

枚举对象，它属于```enum```模块，存在于Python 3.4以上版本中（同时作为一个独立的PyPI包```enum34```供老版本使用）。Enums(枚举类型)基本上是一种组织各种东西的方式。


```python
from enum import Enum

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # 依次类推

    # 但我们并不想关心同一物种的年龄，所以我们可以使用一个别名
    kitten = 1  # (译者注：幼小的猫咪)
    puppy = 2   # (译者注：幼小的狗狗)

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)
```


```python
charlie.type == tom.type
```




    True




```python
print(charlie.type,tom.type)
```

    Species.cat Species.cat



```python
print(Species(1),Species['cat'],Species.cat)
```

    Species.cat Species.cat Species.cat


# 枚举 Enumerate


```python
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
```

    1 apple
    2 banana
    3 grapes
    4 pear



```python
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
```

    [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]


# 对象⾃省

⾃省(introspection)，在计算机编程领域⾥，是指在运⾏时来判断⼀个对象的类型的能⼒。 它是Python的强项之⼀。Python中所有⼀切都是⼀个对象

## dir

是⽤于⾃省的最重要的函数之⼀。它返回⼀个列表，列出了⼀个对象所拥有的属性和⽅ 法


```python
my_list = [1, 2, 3]
dir(my_list)
```




    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__delitem__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__gt__',
     '__hash__',
     '__iadd__',
     '__imul__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__reversed__',
     '__rmul__',
     '__setattr__',
     '__setitem__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'append',
     'clear',
     'copy',
     'count',
     'extend',
     'index',
     'insert',
     'pop',
     'remove',
     'reverse',
     'sort']



## type和id

> - type函数返回⼀个对象的类型
> - id()函数返回任意不同种类对象的唯⼀ID


```python
print(type(''),type({}),type([]),type(dict))
```

    <class 'str'> <class 'dict'> <class 'list'> <class 'type'>



```python
name = "Yasoob" 
print(id(name))
```

    139668718335288


## inspect模块

inspect模块也提供了许多有⽤的函数，来获取活跃对象的信息。⽐⽅说，你可以查看⼀ 个对象的成员，只需运⾏


```python
import inspect 
print(inspect.getmembers(str))
```

    [('__add__', <slot wrapper '__add__' of 'str' objects>), ('__class__', <class 'type'>), ('__contains__', <slot wrapper '__contains__' of 'str' objects>), ('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), ('__dir__', <method '__dir__' of 'object' objects>), ('__doc__', "str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."), ('__eq__', <slot wrapper '__eq__' of 'str' objects>), ('__format__', <method '__format__' of 'str' objects>), ('__ge__', <slot wrapper '__ge__' of 'str' objects>), ('__getattribute__', <slot wrapper '__getattribute__' of 'str' objects>), ('__getitem__', <slot wrapper '__getitem__' of 'str' objects>), ('__getnewargs__', <method '__getnewargs__' of 'str' objects>), ('__gt__', <slot wrapper '__gt__' of 'str' objects>), ('__hash__', <slot wrapper '__hash__' of 'str' objects>), ('__init__', <slot wrapper '__init__' of 'object' objects>), ('__init_subclass__', <built-in method __init_subclass__ of type object at 0x7f074eb60220>), ('__iter__', <slot wrapper '__iter__' of 'str' objects>), ('__le__', <slot wrapper '__le__' of 'str' objects>), ('__len__', <slot wrapper '__len__' of 'str' objects>), ('__lt__', <slot wrapper '__lt__' of 'str' objects>), ('__mod__', <slot wrapper '__mod__' of 'str' objects>), ('__mul__', <slot wrapper '__mul__' of 'str' objects>), ('__ne__', <slot wrapper '__ne__' of 'str' objects>), ('__new__', <built-in method __new__ of type object at 0x7f074eb60220>), ('__reduce__', <method '__reduce__' of 'object' objects>), ('__reduce_ex__', <method '__reduce_ex__' of 'object' objects>), ('__repr__', <slot wrapper '__repr__' of 'str' objects>), ('__rmod__', <slot wrapper '__rmod__' of 'str' objects>), ('__rmul__', <slot wrapper '__rmul__' of 'str' objects>), ('__setattr__', <slot wrapper '__setattr__' of 'object' objects>), ('__sizeof__', <method '__sizeof__' of 'str' objects>), ('__str__', <slot wrapper '__str__' of 'str' objects>), ('__subclasshook__', <built-in method __subclasshook__ of type object at 0x7f074eb60220>), ('capitalize', <method 'capitalize' of 'str' objects>), ('casefold', <method 'casefold' of 'str' objects>), ('center', <method 'center' of 'str' objects>), ('count', <method 'count' of 'str' objects>), ('encode', <method 'encode' of 'str' objects>), ('endswith', <method 'endswith' of 'str' objects>), ('expandtabs', <method 'expandtabs' of 'str' objects>), ('find', <method 'find' of 'str' objects>), ('format', <method 'format' of 'str' objects>), ('format_map', <method 'format_map' of 'str' objects>), ('index', <method 'index' of 'str' objects>), ('isalnum', <method 'isalnum' of 'str' objects>), ('isalpha', <method 'isalpha' of 'str' objects>), ('isascii', <method 'isascii' of 'str' objects>), ('isdecimal', <method 'isdecimal' of 'str' objects>), ('isdigit', <method 'isdigit' of 'str' objects>), ('isidentifier', <method 'isidentifier' of 'str' objects>), ('islower', <method 'islower' of 'str' objects>), ('isnumeric', <method 'isnumeric' of 'str' objects>), ('isprintable', <method 'isprintable' of 'str' objects>), ('isspace', <method 'isspace' of 'str' objects>), ('istitle', <method 'istitle' of 'str' objects>), ('isupper', <method 'isupper' of 'str' objects>), ('join', <method 'join' of 'str' objects>), ('ljust', <method 'ljust' of 'str' objects>), ('lower', <method 'lower' of 'str' objects>), ('lstrip', <method 'lstrip' of 'str' objects>), ('maketrans', <built-in method maketrans of type object at 0x7f074eb60220>), ('partition', <method 'partition' of 'str' objects>), ('replace', <method 'replace' of 'str' objects>), ('rfind', <method 'rfind' of 'str' objects>), ('rindex', <method 'rindex' of 'str' objects>), ('rjust', <method 'rjust' of 'str' objects>), ('rpartition', <method 'rpartition' of 'str' objects>), ('rsplit', <method 'rsplit' of 'str' objects>), ('rstrip', <method 'rstrip' of 'str' objects>), ('split', <method 'split' of 'str' objects>), ('splitlines', <method 'splitlines' of 'str' objects>), ('startswith', <method 'startswith' of 'str' objects>), ('strip', <method 'strip' of 'str' objects>), ('swapcase', <method 'swapcase' of 'str' objects>), ('title', <method 'title' of 'str' objects>), ('translate', <method 'translate' of 'str' objects>), ('upper', <method 'upper' of 'str' objects>), ('zfill', <method 'zfill' of 'str' objects>)]


# 各种推导式(comprehensions)

推导式（又称解析式）是Python的⼀种独有特性。 

推导式是可以从⼀个数据序列构建另⼀个新的数据序列的结构体。 

共有三种推导，在 Python2和3中都有⽀持： 
> - 列表(list)推导式 
> - 字典(dict)推导式 
> - 集合(set)推导式

## 列表推导式（list comprehensions）

参考： https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html#dictionary-comprehensions

列表推导式（又称列表解析式）提供了⼀种简明扼要的⽅法来创建列表。 

它的结构是在⼀个中括号⾥包含⼀个表达式，然后是⼀个for语句，然后是0个或多个for 或者if语句。

那个表达式可以是任意的，意思是你可以在列表中放⼊任意类型的对象。

返 回结果将是⼀个新的列表，在这个以if和for语句为上下⽂的表达式运⾏完成之后产⽣
```python
variable = [out_exp for out_exp in input_list if out_exp == 2]
```


```python
[i for i in range(30) if i % 3 is 0]
```




    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]




```python
[x**2 for x in range(10)]
```




    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




```python
['{}-{}'.format(x,y) for x in range(0,2) for y in range(11,13)]
```




    ['0-11', '0-12', '1-11', '1-12']



## 字典推导式（dict comprehensions）
字典推导和列表推导的使⽤⽅法是类似的


```python
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}
print(mcase)
```

    {'a': 10, 'b': 34, 'A': 7, 'Z': 3}



```python
dict1 = {key:value for key,value in  [('name','zhangsan'),('age',22),('phone',110)]}
print(dict1)
```

    {'name': 'zhangsan', 'age': 22, 'phone': 110}



```python
import random
stuInfo = {'westos'+ str(i):random.randint(60,100) for i in range(20)}
print({name:score for name,score in stuInfo.items() if score > 90})
```

    {'westos9': 91, 'westos13': 95, 'westos16': 91}


## 集合推导式（set comprehensions）
它们跟列表推导式也是类似的。 唯⼀的区别在于它们使⽤⼤括号{}

**注意：将列表转化为集合，在集合的每个元素上操作**


```python
squared = {x**2 for x in [1, 1, 2]}
print(squared)
```

    {1, 4}


## 生成器表达器

⽣成器表达式和列表推导式的语法基本上是一样的. 只是把[]替换成()


```python
a=(i**2 for i in [1,1,2,3,4,4,8])
print(list(a))
```

    [1, 1, 4, 9, 16, 16, 64]



```python
a=(i**2 for i in [1,1,2,3,4,4,8])
print(set(a))
```

    {64, 1, 4, 9, 16}



```python
lst = [11,22,33,44]
a=({i:lst[i] for i in range(len(lst)) if i < 2})
a
```




    {0: 11, 1: 22}



# 异常


```python
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
```

    An IOError occurred. No such file or directory


## 多个异常处理

### 所有可能发生的异常放到一个元组里


```python
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))
```

    An error occurred. No such file or directory


### 对每个单独的异常在单独的except语句块中处理

如果异常没有被第⼀个except语句块处理，那么它也许被下⼀个语句 块处理，或者根本不会被处理


```python
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e
```

    An error occurred.



    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-92-9f3c58970d73> in <module>
          6 except IOError as e:
          7     print("An error occurred.")
    ----> 8     raise e
    

    <ipython-input-92-9f3c58970d73> in <module>
          1 try:
    ----> 2     file = open('test.txt', 'rb')
          3 except EOFError as e:
          4     print("An EOF error occurred.")
          5     raise e


    FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'


### 捕获所有异常


```python
try:
    file = open('test.txt', 'rb')
except Exception:
    # 打印一些异常日志，如果你想要的话
    raise
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-93-5bb88d76d9e5> in <module>
          1 try:
    ----> 2     file = open('test.txt', 'rb')
          3 except Exception:
          4     # 打印一些异常日志，如果你想要的话
          5     raise


    FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'


## finally从句

包裹到finally从 句中的代码不管异常是否触发都将会被执⾏。这可以被⽤来在脚本执⾏之后做清理⼯作


```python
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")
```

    An IOError occurred. No such file or directory
    This would be printed whether or not an exception occurred!


## try/else从句

else从句只会在没有异常的情况下执⾏，⽽且它会在finally语句之前执⾏


```python
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # 这里的代码只会在try语句里没有触发异常时运行,
    # 但是这里的异常将 *不会* 被捕获
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')
```

    I am sure no exception is going to occur!
    This would only run if no exception occurs. And an error here would NOT be caught.
    This would be printed in every case.


# lambda表达式

lambda表达式是⼀⾏函数。 

它们在其他语⾔中也被称为匿名函数。如果你不想在程序中对⼀个函数使⽤两次，你也许 会想⽤lambda表达式，它们和普通的函数完全⼀样


```python
add = lambda x, y: x + y
print(add(3, 5))
```

    8


## 列表排序


```python
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
a
```




    [(13, -3), (4, 1), (1, 2), (9, 10)]



## 列表并行排序


```python
data = zip([2,1,3], [8,5,6])
data=sorted(data)
list1, list2 = map(lambda t: list(t), zip(*data))
print(list1,list2)
```

    [1, 2, 3] [5, 8, 6]



```python
str1 = 'abcd'
str2 = '1234'
list_new = zip(str1, str2)
print(dict(list_new))
```

    {'a': '1', 'b': '2', 'c': '3', 'd': '4'}



```python
a=[1,2,3]
b=[4,5,6]
zipped=zip(a,b)
dict(zipped)
```




    {1: 4, 2: 5, 3: 6}




```python
list(zip(*zip(range(1, 8), range(21, 28))))
```




    [(1, 2, 3, 4, 5, 6, 7), (21, 22, 23, 24, 25, 26, 27)]



# ⼀⾏式的Python命令
[Powerful Python One-Liners](https://wiki.python.org/moin/Powerful%20Python%20One-Liners)

## 简易Web Server

过通过⽹络快速共享⽂件
```python
    # Python 2 
    python -m SimpleHTTPServer 
    # Python 3 
    python -m http.server
```

## 漂亮的打印

```bash
    #格式化json数据
    python -m json.tool
   cat file.json | python -m json.tool
```


```python
from pprint import pprint 
my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
pprint(my_dict)
```

    {'age': 'undefined', 'name': 'Yasoob', 'personality': 'awesome'}



```python
import pprint;
pprint.pprint(list(zip(('Byte', 'KByte', 'MByte', 'GByte', 'TByte'), (1 << 10*i for i in range(5)))))
```

    [('Byte', 1),
     ('KByte', 1024),
     ('MByte', 1048576),
     ('GByte', 1073741824),
     ('TByte', 1099511627776)]



```python
print('\n'.join("%i Byte = %i Bit = largest number: %i" % (j, j*8, 256**j-1) for j in (1 << i for i in range(8))))
```

    1 Byte = 8 Bit = largest number: 255
    2 Byte = 16 Bit = largest number: 65535
    4 Byte = 32 Bit = largest number: 4294967295
    8 Byte = 64 Bit = largest number: 18446744073709551615
    16 Byte = 128 Bit = largest number: 340282366920938463463374607431768211455
    32 Byte = 256 Bit = largest number: 115792089237316195423570985008687907853269984665640564039457584007913129639935
    64 Byte = 512 Bit = largest number: 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095
    128 Byte = 1024 Bit = largest number: 179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137215


## 脚本性能分析
这可能在定位你的脚本中的性能瓶颈时，会非常奏效：
```bash
    python -m cProfile my_script.py 
    #备注：cProfile是⼀个⽐profile更快的实现，因为它是⽤c写的
```

## csv转json
```bash
python -c "import csv,json;print(json.dumps(list(csv.reader(open('csv_file.csv')))))"
```

## 列表辗平


```python
#只支持二维数据
from itertools import chain
a_list = [[1, 2], [3, 4], [5,[7,8], 6]]
print(list(chain.from_iterable(a_list)))
print(list(chain(*a_list)))
```

    [1, 2, 3, 4, 5, [7, 8], 6]
    [1, 2, 3, 4, 5, [7, 8], 6]


## 一行式的构造器
避免类初始化时大量重复的赋值语句


```python
class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
a=A(1,2,3,4,5,6)
a.b
```




    2



# For - Else
else从句会在循环正常结束 时执⾏。这意味着，循环没有遇到任何break


```python
for n in range(2, 40):
    for x in range(2, n):
        if n % x == 0:
#             print(n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```

    2 is a prime number
    3 is a prime number
    5 is a prime number
    7 is a prime number
    11 is a prime number
    13 is a prime number
    17 is a prime number
    19 is a prime number
    23 is a prime number
    29 is a prime number
    31 is a prime number
    37 is a prime number


# open函数

```open```的第一个参数是文件名。第二个(```mode``` 打开模式)决定了这个文件如何被打开。

- 如果你想读取文件，传入```r```
- 如果你想读取并写入文件，传入```r+```
- 如果你想覆盖写入文件，传入```w```
- 如果你想在文件末尾附加内容，传入```a```


```python
import io

with open('logo.png', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata))
    
with open('summary.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line)
```

    This is a random file (2910 bytes long)
    


# 兼容Python2+3

[Porting Python 2 Code to Python 3](https://docs.python.org/3/howto/pyporting.html)

## Future模块导⼊
第⼀种也是最重要的⽅法，就是导⼊__future__模块。它可以帮你在Python2中导⼊ Python3的功能

上下⽂管理器是Python2.6+引⼊的新特性，如果你想在Python2.5中使⽤它可以这样做： 
``` python
from __future__ import with_statement
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
```

在Python3中print已经变为⼀个函数。如果你想在Python2中使⽤它可以通过 __future__导⼊：
```python
from __future__ import print_function 
print(print)
```

## 模块重命名
将模块导⼊代码包装在try/except语句中。这样做是因为在Python 2中并没 有urllib.request模块。这将引起⼀个ImportError异常。⽽在Python2中 urllib.request的功能则是由urllib2提供的。所以,当试图在Python2中导⼊urllib.request模块的时候，⼀旦捕获到ImportError将通过导 ⼊urllib2模块来代替它


```python
try:
    import urllib.request as urllib_request # for Python 3 
except ImportError:
    import urllib2 as urllib_request # for Python 2
```

## 过期的Python2内置功能

是Python2中有12个内置功能在Python3中已经被移除了。要确保 在Python2代码中不要出现这些功能来保证对Python3的兼容。

这有⼀个强制让你放弃12内 置功能的⽅法：

```python
from future.builtins.disabled import * 
apply()

# Output: NameError: obsolete Python 2 builtin apply is disabled
```

# 协程

## 简单输出斐波那契數列前 N 个数


```python
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        print(b) 
        a, b = b, a + b 
        n = n + 1
fab(5)
```

    1
    1
    2
    3
    5



```python
class Fab(object): 
    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 
        
    def __iter__(self): 
        return self 
    
    def __next__(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()
        
for n in Fab(5):
    print(n)
```

    1
    1
    2
    3
    5



```python
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 
for n in fab(5):
    print(n)
```

    1
    1
    2
    3
    5


发送的值会被yield接收。

为什么要运⾏next()⽅法呢？
这样做正是为了启动⼀个 协程。就像协程中包含的⽣成器并不是⽴刻执⾏，⽽是通过next()⽅法来响应send()⽅法。
因此，你必须通过next()⽅法来执⾏yield表达式。 

可以通过调⽤close()⽅法来关闭⼀个协程


```python
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line) 
            
search = grep('coroutine')
next(search)
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutine instead!")
search.send("I love tomorrow instead!")
search.send("I love coroutine too!")
search.close()
```

    Searching for coroutine
    I love coroutine instead!
    I love coroutine too!


# 函数缓存 (Function caching)

函数缓存允许我们将⼀个函数对于给定参数的返回值缓存起来。

当⼀个I/O密集的函数被频繁使⽤相同的参数调⽤的时候，函数缓存可以节约时间。 

在Python 3.2版本以前我们只有写⼀个⾃定义的实现。在Python 3.2以后版本，有 个lru_cache的装饰器，允许我们将⼀个函数的返回值快速地缓存或取消缓存


## 3.2版本后实现斐波那契计算器


```python
from functools import lru_cache 
@lru_cache(maxsize=32) 
def fib(n): 
    if n < 2: 
        return n 
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])
```

    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


maxsize参数是告诉lru_cache，最多缓存最近多少个返回值
返回值清空缓存


```python
fib.cache_clear()
```

## python 2系统版本实现斐波那契计算器


```python
from functools import wraps 
def memoize(function,maxsize=32): 
    memo = {} 
    @wraps(function) 
    def wrapper(*args): 
        if args in memo: 
            return memo[args] 
        else:
            rv = function(*args) 
            memo[args] = rv 
            return rv 
    return wrapper

@memoize 
def fibonacci(n,maxsize=32): 
    if n < 2: 
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2) 

fibonacci(21)
```




    10946



# 上下⽂管理器(Context managers)

使⽤上下⽂管理器最⼴泛的案例就是with语句

上下⽂管理器的⼀个常见⽤例，是资源的加锁和解锁，以及关闭已打开的⽂件


```python
with open('aa.txt', 'w') as opened_file:
    opened_file.write('Hola!')
    
file = open('aa.txt', 'w')
try:
    file.write('Hola!')
finally:
    file.close()
```

## 基于类的实现

⼀个上下⽂管理器的类，最起码要定义```__enter__```和```__exit__```⽅法

```__exit__```函数接受三个参数。这些参数对于每个上下文管理器类中的```__exit__```方法都是必须的。

在底层都发生了什么。

1. ```with```语句先暂存了```File```类的```__exit__```方法
2. 然后它调用```File```类的```__enter__```方法
3. ```__enter__```方法打开文件并返回给```with```语句
4. 文件句柄被传递给```opened_file```参数
5. 使用```.write()```来写文件
6. ```with```语句调用之前暂存的```__exit__```方法
7. ```__exit__```方法关闭了文件


```python
class File(object):
    def __init__(self, file_name, method):
        print('init object')
        self.file_obj = open(file_name, method)
    def __enter__(self):
        print('enter operate object')
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print('exit')
        self.file_obj.close()
        
with File('aa.txt', 'w') as opened_file:
    print('write content to file')
    opened_file.write('Hola!')
```

    init object
    enter operate object
    write content to file
    exit


## 处理异常

```__exit__```方法的这三个参数：```type```, ```value```和```traceback```。  
在第3步和第6步之间，如果发生异常，Python会将异常的```type```,```value```和```traceback```传递给```__exit__```方法

让```__exit__```方法来决定如何关闭文件以及是否需要其他步骤

1. 它把异常的```type```,```value```和```traceback```传递给```__exit__```方法
2. 它让```__exit__```方法来处理异常
3. 如果```__exit__```返回的是True，那么这个异常就被优雅地处理了。
4. 如果```__exit__```返回的是True以外的任何东西，那么这个异常将被```with```语句抛出


```python
class File(object):
    def __init__(self, file_name, method):
        print('init object')
        self.file_obj = open(file_name, method)
    def __enter__(self):
        print('enter operate object')
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print('exit')
        print("Exception has been handled")
        self.file_obj.close()
        return True
```


```python
with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function('Hola!')
```

    init object
    enter operate object
    exit
    Exception has been handled


## 基于生成器的实现

用装饰器(decorators)和生成器(generators)来实现上下文管理器。  
Python有个```contextlib```模块专门用于这个目的。可以使用一个生成器函数来实现一个上下文管理器，而不是使用一个类

1. Python解释器遇到了```yield```关键字。因为这个缘故它创建了一个生成器而不是一个普通的函数。
2. 因为这个装饰器，```contextmanager```会被调用并传入函数名（```open_file```）作为参数。
3. ```contextmanager```函数返回一个以```GeneratorContextManager```对象封装过的生成器。
4. 这个```GeneratorContextManager```被赋值给```open_file```函数，实际上是在调用```GeneratorContextManager```对象。


```python
from contextlib import contextmanager 
@contextmanager 
def open_file(name): 
    f = open(name, 'w') 
    yield f 
    f.close()
```


```python
with open_file('some_file') as f:
    f.write('hola!')
```
