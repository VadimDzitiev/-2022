from operator import itemgetter

class Mus:
    """Музыкант"""
    def __init__(self, id, fio, sal, orc_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.orc_id = orc_id

class Orc:
    """Оркестр"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class MusOrc:
    """
    'Музыканты' для реализации
    связи многие-ко-многим
    """
    def __init__(self,orc_id,mus_id):
        self.mus_id = mus_id
        self.orc_id = orc_id

# Оркестры
Orcs = [
    Orc(1, 'Исторический оркестр'),
    Orc(2, 'Симфонический оркестр'),
    Orc(3, 'Духовой оркестр'),
]

#  Музыканты
Muss = [
    Mus(1, 'Иванов', 45000, 1),
    Mus(2, 'Багаев', 35000, 1),
    Mus(3, 'Петров', 22000, 2),
    Mus(4, 'Свиридов', 25000, 2),
    Mus(5, 'Слепаков', 39000, 3),
    Mus(6, 'Рябцев', 30000, 3),
]


muss_orcs = [
    MusOrc(1, 1),
    MusOrc(2, 1),
    MusOrc(3, 2),
    MusOrc(4, 2),
    MusOrc(5, 3),
    MusOrc(6, 3),
]


"""Основная функция"""
# Соединение данных один-ко-многим
one_to_many = [(e.fio, e.sal, d.name)
              for d in Orcs
              for e in Muss
              if e.orc_id == d.id]
# Соединение данных многие-ко-многим
many_to_many_temp = [(d.name, ed.orc_id, ed.orc_id)
                    for d in Orcs
                    for ed in muss_orcs
                    if d.id == ed.orc_id]
many_to_many = [(e.fio, e.sal, orc_name)
                for orc_name, orc_id, mus_id in many_to_many_temp
                for e in Muss
                if e.id == mus_id ]

def N1():
    global one_to_many, many_to_many
    A1=[]
    print('Задание А1')
    for i in range(len(one_to_many)):
        if one_to_many[i][0][-2:] == "ов":
            A1.append((one_to_many[i][0], one_to_many[i][2]))
    return A1

def N2():
    global one_to_many, many_to_many
    A2=[]
    print('\nЗадание А2')
    arr = arr1 = []
    for x in Orcs:
        # Список музыкантов
        d_muss = list(filter(lambda i: i[2] == x.name, one_to_many))
        if len(d_muss) > 0:
            # Зарплаты музыкантов
            d_sals = [sal for _, sal, _ in d_muss]
            # Средняя зарплата
            d_sals_sum = sum(d_sals)
            arr.append((x.name, d_sals_sum/len(d_muss)))
            arr1=sorted(arr, key=itemgetter(1), reverse=True)

    for i in arr1:
        A2.append((i[0],i[1].__round__()))
    return A2

def N3():
    global one_to_many, many_to_many
    A3=[]
    print('\nЗадание А3')
    arr2 = []
    for d in Orcs:
        if 'И' in d.name:
            arr2.append(d.id)

    for x in range(int(len(arr2))):
        A3.append(many_to_many[x][2])
        for i in Muss:
            if i.orc_id == arr2[x]:
                A3.append(i.fio)

    return A3

if __name__ == '__main__':

    print(N1())
    print(N2())
    print(N3())