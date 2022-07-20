'''В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
Чем больше тестов на каждую функцию - тем лучше
'''

from math import pi, sqrt, pow, hypot


def test_math_pi():
    assert int(1 * pi * 100) == 314
    return


def test_math_sqrt():
    assert sqrt(4) == 2
    assert sqrt(1) == 1
    assert sqrt(6.25) == 2.5
    return


def test_math_pow():
    assert pow(3, 2) == 9
    assert pow(-3, 2) == 9
    assert pow(3, 3) == 27
    assert pow(-5, -3) == -0.008
    assert int(pow(1.5, -2) * 10000) == 4444
    return


def test_math_hypot():
    assert hypot(3, 4) == 5
    assert hypot(-3, -4) == 5
    assert hypot(3.3, -4.4) == 5.5
    return


def test_filter():
    test_list = ['first', 1, 1.0, True, False, None, 'second']
    assert list(filter(None, test_list)) == ['first', 1, 1.0, True, 'second']
    assert list(filter(lambda x: isinstance(x, str), test_list)) == ['first', 'second']
    assert list(filter(lambda x: isinstance(x, int), test_list)) == [1, True, False]
    return


def test_map():
    assert list(map(sqrt, [0, 4, 6.25, 11])) == [0, 2, 2.5, sqrt(11)]
    assert list(map(lambda x, y: x + y, [0, 4], [6.25, 11])) == [6.25, 15]
    return


def test_sorted():
    l1 = {'carrot': 'vegetable', 'red': 'color', 'soup': 'food'}
    assert sorted(l1, key=len) == ['red', 'soup', 'carrot']
    assert sorted(l1.values(), key=len) == ['food', 'color', 'vegetable']
    assert sorted(['blue', 'green', 'red', 'orange'], key=len) == ['red', 'blue', 'green', 'orange']
    assert sorted((1, -4, 5, -7, 9, 2.5), key=abs, reverse=True) == [9, -7, 5, -4, 2.5, 1]
    return
