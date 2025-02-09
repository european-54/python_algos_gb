"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: примените хеши и множества
рара:
рар
ра
ар
ара
р
а
"""

x = 26

mod = 3001


# Функция для поиска необходимого количества

def CntSubstr(s, l):
    # Переменная в хеш

    hash = 0;

    # Нахождение хеша подстроки

    # (0, l-1) с использованием случайного числа x

    for i in range(l):
        hash = (hash * x + (ord(s[i]) - 97)) % mod;

        # Вычисление х ^ (л-1)

    pow_l = 1;

    for i in range(l - 1):
        pow_l = (pow_l * x) % mod;

        # Неупорядоченный набор для добавления значений хеша

    result = set();

    result.add(hash);

    # Генерация всех возможных значений хеша

    for i in range(l, len(s)):
        hash = ((hash - pow_l * (ord(s[i - l]) - 97)

                 + 2 * mod) * x + (ord(s[i]) - 97)) % mod;

        result.add(hash);

        # Распечатать результат

    print(len(result));


#  Код водителя

if __name__ == "__main__":
    s = "abcba";

    l = 2;

    CntSubstr(s, l);
