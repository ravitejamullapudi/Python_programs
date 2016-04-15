__author__ = 'Kalyan'

notes = '''
 Scopes and namespaces govern the accessibility rules and lifetime of python variables.

 Namespaces is a mapping of names to objects. Each python block creates a new namespace. The 3 python blocks are
 modules (files), functions and classes.

 An object can have many names in the same namespace
 An object can have names in different namespaces.

 Scope is a textual area in which a variable can be directly accessible by its name.

 Variable which are bound (created) in a block are called local variables in that block
 Variables which are scoped to the the whole file (module) are called global
 Variables which are scoped to outer functions (in case of nested functions) are called non-local or free.
'''


from placeholders import *

count = 10

#used to by pass any local shadow variables.
def get_global_count():
    return count

def test_scope_basic():
    value = count

    assert True == ('value' in locals())
    assert False == ('value' in globals())

    assert False == ('count' in locals())
    assert True == ('count' in globals())

    assert 10 == value


def test_scope_undefined_variable():
    try:
        my_name = name  #name variable is not in local or  global scope
    except NameError : # fill up the exception
        pass

    assert False == ('my_name' in locals())
    assert False == ('name' in locals())
    assert False == ('name' in globals())

def test_variable_shadow():
    count = 20

    assert True == ('count' in locals())
    assert True == ('count' in globals())

    assert 20 == count
    assert 10 == get_global_count()

def test_global_write():
    global count # declare that we want to use the read/write to global count
    count = 30

    try:
        assert False == ('count' in locals())
        assert True == ('count' in globals())

        assert 30 == count
        assert 30 == get_global_count()
    finally:
        count = 10 #reset to original value

def test_scope_is_bound_at_definition_time():
    assert False == ('count' in locals())
    assert True == ('count' in globals())

    try:
        value = count
        count = 30
    except NameError : # what happens when you read a variable before initializing it?
        #print it here..
        assert True
    finally:
        count = 20

    assert 20 == count
    assert 10 == get_global_count()


def test_scope_writing_globals():
    assert False == ('count' in locals())
    assert True == ('count' in globals())

    global count

    try:
        count = 40
        assert 40 == count
        assert 40 == get_global_count()
    finally:
        count = 10

    assert 10 == get_global_count()



three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = 15


