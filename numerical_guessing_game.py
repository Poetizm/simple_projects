import random
num = random.randrange(100)
print(num)
print('Добро пожаловать в числовую угадайку')

def is_valid(n):
    if n.isdigit():
        return True
    else:
        return False

n = input('Введите число от 0 до 100  ')
while True:
    if is_valid(n):
        n = int(n)
        break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        n = input()

while n != num:
    if n < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        n = int(input())
    elif n > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        n = int(input())
print('Вы угадали, поздравляем!')
