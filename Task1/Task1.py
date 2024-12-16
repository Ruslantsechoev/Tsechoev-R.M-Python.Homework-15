
import logging


# Настройка логирования
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Преобразователь для сообщений
letter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


# Обработчик для Debug and Info
debug_info = logging.FileHandler('debug_info.log')
debug_info.setLevel(logging.DEBUG)
debug_info.setFormatter(letter)
logger.addHandler(debug_info)


# Обработчик для Warning, Error and Critical
warning_error = logging.FileHandler('warning_error.log')
warning_error.setLevel(logging.WARNING)
warning_error.setFormatter(letter)
logger.addHandler(warning_error)


# Логирование сообщений разных уровней
logger.debug('Level DEBUG')
logger.info('Level INFO')
logger.warning('Level WARNING')
logger.error('Level ERROR')
logger.critical('Level CRITICAL')
