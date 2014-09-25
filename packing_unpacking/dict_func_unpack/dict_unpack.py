def function_default(arg1=2, arg2=1):
    print arg1, arg2

def function_nodefault(arg1, arg2=1):
    print arg1, arg2


d = {'arg1': 0, 'arg2': 10}

function_default(**d)

function_nodefault(**d)
