
import argparse
import sys


sys.argv = ['text', '7', '--verbose', '--repeat']


def main():

    # Создаем контейнер для спецификаций аргументов и опций
    parser = argparse.ArgumentParser(prog='Options and flags',
                                     description='Handing options and flags',
                                     epilog='Task4, HomeWork15')

    # Добавляем к парсеру отдельные опции, принимающие значения, флаги включения/выключения, параметры,
    # обязательные аргументы
    parser.add_argument('text', type=str, help='Строка для вывода')
    parser.add_argument('number', type=int, help='Число для вывода')

    # добавление опций
    parser.add_argument('--verbose',
                        action='store_true',
                        help='Вывод дополнительной информации о процессе')

    parser.add_argument('--repeat',
                        type=int,
                        default=1,
                        help='количество повторений строки в выводе')

    # Создаем объект args. Он будет содержать все принятые аргументы
    args = parser.parse_args()


    # Если опция --verbose установлена, то будет выведена дополнительная информация
    if args.verbose:
        print(f'Полученные аргументы: \nчисло - {args.number}, \nстрока - "{args.text}", \nповторения - {args.repeat}')

    print(f'Число - {args.number}, \nстрока - {args.text * args.repeat}')

if __name__ == '__main__':
    main()



