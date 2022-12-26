import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
        key=False
    except:
        print(prompt)
        key=True

    if key:
        flag=True
        while flag:
            try:
                coef = float(input())
                flag=False
            except:
                print("Введите коэфицент повторно")
                pass
    return coef


def get_roots(a, b, c):
    result = []

    if (b**2 - 4 * a * c)>0:
        if (-b+math.sqrt(b**2-4*a*c))/(2*a) > 0:
            result.append(-math.sqrt((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a))
            result.append(math.sqrt((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a))
        if (-b-math.sqrt(b**2-4*a*c))/(2*a) > 0:
            result.append(-math.sqrt((-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a))
            result.append(math.sqrt((-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a))
    return result

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print(f'Два корня: {roots[0]} и {roots[1]}')
    elif len_roots == 3:
        print(f'Три корня: {roots[0]} , {roots[1]} и {roots[2]}')
    elif len_roots == 4:
        print(f'Четыре корня: {roots[0]} , {roots[1]} , {roots[2]} , {roots[3]}')
if __name__ == "__main__":
    main()