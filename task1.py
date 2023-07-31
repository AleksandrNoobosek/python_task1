# 1 .Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - 
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

ZERO = 0 
a = 6   # 1
b = 5  # 2
c = 6  # 10

if a + b > c and b + c > a and c + a > b and a > ZERO and b > ZERO and c > ZERO:
    print(' треугольник существует')

    if a!=b and b!=c and c!=a:
        print ('Треугольник яв-ся разносторонним! ')
    elif a == b == c:
        print('Треугольник яв-ся  равносторонним! ')
    else:
        print('Треугольник яв-ся равнобедренным! ')
else:
    print('треугольника с такими сторонами не существует')   # [1,2,10]

# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

ZERO = 0
min_limit = 0
max_limit = 100000
numm = None
num_exception = 1
root_two = 0.5
first_num = 1

while True:
    print('Input restriction:', min_limit, 'and', max_limit)
    numm = int(input('input your value:'))

    if numm < min_limit or numm > max_limit:
        print('entered a wrong number')
    else:
        break

if numm <= num_exception:
    print('is not a natural number and consequently, is neither prime')
else:    
    for i in range(2, int(numm ** root_two) + first_num):
        if numm % i == ZERO:
            print('composite number')
            break
    else:
        print('simple number')

# Решить задачу про таблицу умножения: Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

count = 10
for i in range(1,count):
    for j in range(1,count):
        print(i, 'x', j, '=', i*j)
    print(' ')
    