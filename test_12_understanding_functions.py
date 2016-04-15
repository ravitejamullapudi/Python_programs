__author__ = 'Kalyan'

from placeholders import *

notes = '''
Functions are the basic unit of modularization in python. You use functions to group
together a meaningful action or behavior and use it when you need it.

The feature set of functions in python is richer than every major programming
language and makes it easy to expose elegant and usable apis.

This is a big topic, we will revisit this topic again.
'''

def my_print(x):
    print x

def my_increment(x):
    return x + 1

def my_min_max(numbers):
    return min(numbers), max(numbers)

# functions are kinds of objects, they have a type too!
def test_function_type():
    assert 'function' == type(my_print).__name__
    assert 'function' == type(my_increment).__name__
    assert 'function' == type(test_function_type).__name__

# functions are objects which can be 'called'
def test_function_callable_type():
    assert False == callable(1)
    assert True == callable(my_increment)
    assert False == callable(my_increment(10))

# functions can be held by references just like any other object
def test_function_assignment():
    demo = my_increment
    result = demo(20)
    assert 21 == result

# every function returns an object, even when it does not!
def test_every_function_returns_something():
    result = my_print(10)
    assert None == result

    result = my_increment(10)
    assert 11 == result

    result = my_min_max([20,30,5])
    assert (5,30) == result

def demo1():
    """returns 10"""
    return 10

def demo2():
    return 20

#The documentation of every function, if the author wrote it, is available at runtime.
#This makes it easy to write access help from console or build specialized help commands like help.
def test_function_documentation():
    assert 'returns 10' == demo1.__doc__
    assert None == demo2.__doc__

def my_callfunc(func):
    return func()

# functions can be passed around.
def test_functions_can_be_passed_as_objects():
    assert 10 == my_callfunc(demo1)
    assert 20 == my_callfunc(demo2)

def my_greet(greeting, name="world"):
    return "{0} {1}".format(greeting, name)

def test_default_arguments():
    assert "Hello world" == my_greet("Hello")
    assert "Hello john" == my_greet("Hello", "john")

def my_add_to_list1(sequence, target=[]):
    """
    Uses a mutable default, usually leads to unexpected behavior
    """
    target.extend(sequence)
    return target

def my_add_to_list2(sequence, target=None):
    """
    Uses None as default and creates a target list on demand.
    """
    if target is None:
        target = []
    target.extend(sequence)

def test_function_defaults_are_evaluated_at_definition_time():
    assert ['h','i'] == my_add_to_list1("hi")
    assert ['h','i','b','y','e'] == my_add_to_list1("bye")

    assert ['h','i'] == my_add_to_list2("hi")
    assert ['b','y','e'] == my_add_to_list2("bye")

def demo(first, second = 2, third = 3):
    return [first, second, third]

# keyword arguments allows you to write one api without having a large number
# of overloads for various scenarios.
def test_function_call_with_keyword_arguments():
    assert [10,2, 3] == demo(10)
    assert [10,20,3] == demo(10, 20)
    assert [10,20,30] == demo(10, 20, 30)
    assert [20,2,3] == demo(20)
    assert [20,2,30] == demo(20, third = 30)
    assert [10,2,30] == demo(first = 10, third= 30)
    assert [10,2,30] == demo(10, third= 30)

def demo_variable_args(first, *args):
    return args

def my_merge(separator, *args):
    return separator.join(args)

def test_function_with_variable_args():
    result = demo_variable_args("hello", "world")
    assert 'tuple' == type(result).__name__ #this is the type of args
    assert ('world',) == result              #this is the value of args

    assert (1,2,3) == demo_variable_args("hello", 1, 2, 3)

    assert "one.two.three" == my_merge(".", "one", "two", "three")
    assert "one,two,three" == my_merge(",", "one", "two", "three")

def demo_with_keyword_args(name, *args, **kwargs):
    return kwargs

def test_function_with_keyword_args():
    result = demo_with_keyword_args("jack", age=10, height=100)
    assert 'dict' == type(result).__name__
    assert {'age':10,'height':100} == result
    assert {'age':10,'height':100} == demo_with_keyword_args("jack", "address", age=10, height=100)
    assert {'address':"address",'age':10,'height':100} == demo_with_keyword_args("jack", address="address", age=10, height=100)


def demo_parameter_passing1(x):
    x = x + 1

def demo_parameter_passing2(names):
    names = []

def demo_parameter_passing3(names):
    names.append("something")

# read up after you finish this to make sure you get this right: http://effbot.org/zone/call-by-object.htm
def test_function_params_passed_by_object_reference():
    x = 10
    demo_parameter_passing1(x)
    assert 10 == x

    names = ["one", "two"]
    demo_parameter_passing2(names)
    assert ['one','two'] == names

    demo_parameter_passing3(names)
    assert ['one','two', 'something'] == names


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___



