from operator import itemgetter
class Book:
 """Книга"""
 def __init__(self, id, title, price, lib_id):
  self.id = id
  self.title = title
  self.price = price
  self.lib_id = lib_id
class Lib:
 """Библиотека"""
 def __init__(self, id, name):
  self.id = id
  self.name = name
class BookLibRelation:
 """Книги в библиотеке"""
 def __init__(self, book_id, lib_id):
  self.book_id = book_id
  self.lib_id = lib_id
# Библиотеки
libs = [
 Lib(1, 'Книга и чернила'),
 Lib(2, 'Книжное место'),
 Lib(3, 'Перо'),
]
# Книги
books = [
 Book(1, 'Метель', 500, 1),
 Book(2, 'На реке', 200, 1),
 Book(3, 'Муму', 300, 2),
 Book(4, 'Мертвые души', 450, 2),
 Book(5, 'Цыган', 150, 2),
 Book(6, 'Обломов', 370, 3),
]
# Связи
books_libs = [
 BookLibRelation(1, 1),
 BookLibRelation(2, 1),
 BookLibRelation(3, 2),
 BookLibRelation(4, 2),
 BookLibRelation(5, 2),
 BookLibRelation(6, 3),
]
def main():
 """Основная функция"""
 # Соединение данных один ко многим
 one_to_many = [(b.title, b.price, l.name)
 for l in libs
 for b in books
 if b.lib_id == l.id
 ]
 # Соединение данных многие ко многим
 many_to_many_temp = [(l.name, bl.lib_id, bl.book_id)
 for l in libs
 for bl in books_libs
 if l.id == bl.lib_id
 ]
 many_to_many = [(b.title, b.price, lib_name)
 for lib_name, lib_id, book_id in many_to_many_temp
 for b in books
 if b.id == book_id
 ]
 # Вывод книг, начинающихся на "Ме" а так же их библиотеки
 print("Задание Д1")
 print(one_to_many)
 res_1 = [(b[0], b[2]) for b in list(filter(lambda x: x[0][:2] == "Ме",
one_to_many))]
 print(*res_1, sep="\n", end="\n\n")
 # Вывод названий библиотек и средних цен на книги
 print("Задание Д2")
 res2 = []
 for l in libs:
 # список книг в одной конкретной бибилиотеке
  books_in_lib = list(filter(lambda x: x[2] == l.name, one_to_many))
  if len(books_in_lib) > 0:
    sum_price = sum(int(b[1])
 for b in books_in_lib
 )
 avg = sum_price/len(books_in_lib)
 # добавляем название библиотеки и среднюю цену
 res2.append((books_in_lib[0][2], avg))
 res2.sort(key=itemgetter(1))
 print(*res2, sep="\n", end="\n\n")
 # Вывод библиотек начинающихся на "К", а так же список книг в них
 print("Задание Д3")
 res3 = {}
 print(many_to_many)
 for l in libs:
  if l.name[0] == "К":
   books_in_lib = list(filter(lambda x: x[2] == l.name, many_to_many))
   res3[l.name] = [b[0] for b in books_in_lib]
 print(res3)
if __name__ == '__main__':
 main()
