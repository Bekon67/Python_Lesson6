# тест файлового менеджера
# sys.path.append('D:/Neural_university/Python/Python_Lesson5/victory')
from .victory.functions_victory import get_date, month_convert


def test_get_date():
    assert get_date('29.02.2012') == 'двадцать девятое февраля 2012 года'
    return


def test_month_convert():
    assert month_convert('июНь') == 6
    assert month_convert('июНнь') == 0
    assert month_convert('1234') == 0
    assert month_convert('1a') == 0
