
import os
import logging
import argparse
from collections import namedtuple


# Создание именованного кортежа для хранения информации о файлах и каталогах
file_info = namedtuple(typename='FileInfo',
                       field_names=['name', 'extension', 'is_directory', 'parent_directory'])


# Настройка логирования
logging.basicConfig(filename='total_directory.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')



def collecting_info(dir_path):
    """Функция по сбору информации о содержимом директории дальнейшее ее сохранение в лог"""

    if not os.path.isdir(dir_path):
        raise ValueError(f'Данный путь {dir_path} не является директорией')

    # Родительский каталог
    dir_parent = os.path.basename(os.path.abspath(dir_path))

    # Проходимся по директории
    for name_dir in os.listdir(dir_path):
        name_path = os.path.join(dir_path, name_dir)

        # Проверяем является ли полученный элемент директорией
        if os.path.isdir(name_path):
            file_info_log = file_info(name=name_dir,
                                      extension=None,
                                      is_directory=True,
                                      parent_directory=dir_parent)
        else:
            name_new, extension_new = os.path.splitext(name_dir)
            file_info_log = file_info(name=name_new,
                                      extension=extension_new.lstrip('.'),
                                      is_directory=False,
                                      parent_directory=dir_parent)

        # Запись в лог
        logging.info(f'{file_info_log.name} | {file_info_log.extension if file_info_log.extension else "None"} | '
                     f'{"Директория" if file_info_log.is_directory else "Файл"} | {file_info_log.parent_directory}')


def main():
    """Основная функция для обработки командной строки и сбора информации"""

    parser = argparse.ArgumentParser(prog='Starting from command line',
                                     description='Command line processing and information gathering',
                                     epilog='Task5 , HomeWork15')

    parser.add_argument('directory',
                        type=str,
                        help='Путь до директории для проверки')

    args = parser.parse_args()

    dir_path_check = args.directory

    try:
        collecting_info(dir_path=dir_path_check)
        print(f'Информация по директории - "{dir_path_check}" успешно записана в файл "total_directory.log". ')
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()