import sys
sys.setrecursionlimit(10000)


def name_number(n: int):
    if n == 0:
        return ''
    elif n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'
    elif n == 20:
        return 'twenty'
    elif n == 30:
        return 'thirty'
    elif n == 40:
        return 'fourty'
    elif n == 50:
        return 'fifty'
    elif n == 60:
        return 'sixty'
    elif n == 70:
        return 'seventy'
    elif n == 80:
        return 'eighty'
    elif n == 90:
        return 'ninety'
    elif n == 1000:
        return 'onethousand'
    elif n >= 100:
        return name_number(n//100) + 'hundred' + 'and' + name_number(n%100)
    else:
        return name_number(n - n%10) + name_number(n%10)

if __name__ == '__main__':
    res = ''
    for i in range(1, 1001):
        res += name_number(i)
    print(len(res))