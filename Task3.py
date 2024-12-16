
from datetime import datetime, timedelta


def future_date(count_days):
    """Функция возвращающая дату, которая наступит через введенное количество дней"""

    # Текущая дата
    date_now = datetime.now()
    print(date_now)

    # Получение будущей даты с форматированием
    future_date = datetime.strftime(date_now + timedelta(days=count_days), "%Y-%m-%d")

    return future_date


if __name__ == '__main__':
    print(future_date(count_days=30))