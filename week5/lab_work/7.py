def f(result):
    import re
    return ''.join(x.capitalize() or '_' for x in result.split('_'))    

print(f(str(raw_input())))