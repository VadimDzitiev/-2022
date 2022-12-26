import json,random,sys,time
from contextlib import contextmanager

path ='data.json'
with open(path, encoding='utf-8', errors='ignore') as f:
    data = json.load(f)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        for k, v in kwargs.items():
            setattr(self, k, v)
        if not hasattr(self, "ignore_case"):
            self.ignore_case=False

    def __next__(self):
        if self.ignore_case:
            li=[]
            for x in self.items: li.append(x.lower())
        else:
            li = self.items

        self.items = []
        for i in li:
            if i not in self.items:
                self.items.append(i)
        return self.items

    def __iter__(self):
        return self

def gen_random(num_count, begin, end):
    a = []
    for i in range(num_count): a.append(random.randint(begin, end))
    return a

class cm_timer_1:
    def __init__(self):
        self.start_time = time.time()
        pass

    def __enter__(self):
        return 0

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print(round(time.time() - self.start_time, 1))


def N2(data):
    res=[]
    for x in data:
        if x.startswith("программист"):
            res.append(x)
    return res

def N3(data, start=' с опытом Python'):
    return data+start

def N4(data):
    a=gen_random(len(data),100000,200000)
    l=[]
    for i in a:
        l.append("зарплата "+str(i))
    res=zip(data,l)
    return res

def field(items, *args):
    res=[]
    assert len(args) > 0
    for a in range(len(args)):
        for i in range(len(items)):
            try: res.append(items[i][args[a]])
            except: pass
    return res

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def f1(arg):
    return next(Unique(field(arg, "job-name"), ignore_case=True))

def f2(arg):
    return N2(arg)

def f3(arg):
    return list(map(N3, arg))

def f4(arg):
    return N4(arg)


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
