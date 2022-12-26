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


def main():
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

    print('Задание А1')
    for i in range(len(one_to_many)):
        if one_to_many[i][0][-2:]=="ов":
            print(one_to_many[i][0], one_to_many[i][2])

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
        print(i[0],i[1].__round__())

    print('\nЗадание А3')
    arr2 = []
    for d in Orcs:
        if 'И' in d.name:
            arr2.append(d.id)

    for x in range(int(len(arr2))):
        print(many_to_many[x][2])
        for i in Muss:
            if i.orc_id == arr2[x]:
                print(i.fio)


if __name__ == '__main__':
    main()
'''
  for l in Orcs:
        if l.name[0] == "Б":
            arr2.append([l.name,l.orc_id])
    print(arr2)
    for x in range(int(len(arr2))):
        for i in Muss:
            if i.orc_id==arr2[x][1]:
                print(i.fio)

arr2 = {}

    for i in range(len(many_to_many)):
         if many_to_many[i][0][0]=="Б":
             print(many_to_many[i][0][0])
    for x in Orcs:
        # Список музыкантов
        d_muss = list(filter(lambda i: i[2] == x.name, many_to_many))
        d_emps_names = [x for x, _, _ in d_muss]
        # Добавляем результат в словарь
        # ключ - отдел, значение - список фамилий
        arr2[x.name] = d_emps_names

    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все отделы
    for d in Orcs:
        # Список сотрудников отдела
        d_emps = list(filter(lambda i: i[2] == d.name, one_to_many))
        # Если отдел не пустой
        if len(d_emps) > 0:
            # Зарплаты сотрудников отдела
            d_sals = [sal for _, sal, _ in d_emps]
            # Суммарная зарплата сотрудников отдела
            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.name, d_sals_sum))

    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все отделы
    for d in Orcs:
        if 'отдел' in d.name:
            # Список сотрудников отдела
            d_emps = list(filter(lambda i: i[2] == d.name, many_to_many))
            # Только ФИО сотрудников
            d_emps_names = [x for x, _, _ in d_emps]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.name] = d_emps_names

    print(res_13)


if __name__ == '__main__':
    main()
'''