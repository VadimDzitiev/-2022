
def f1(a):
    a+=":P:"

def add_to_beginning(s, start='to_'):
    return start + s

lst = ['South', 'North']

result = list(map(add_to_beginning, lst))
print(result)


data=["a","a","a","a"]
a=map(f1,data)
print(a)