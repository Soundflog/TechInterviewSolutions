import re


def remove_sql_comments(sql_text):
    """
    Удаляет комментарии из SQL текста.

    Параметры:
    sql_text (str): Текст SQL, содержащий комментарии.

    Возвращает:
    str: SQL текст без комментариев.
    """
    # Удалить многострочные комментарии
    sql_text = re.sub(r'/\*.*?\*/', '', sql_text, flags=re.DOTALL)

    # Удалить однострочные комментарии, начинающиеся с --
    sql_text = re.sub(r'--.*?\n', '', sql_text)

    # Удалить однострочные комментарии, начинающиеся с #
    sql_text = re.sub(r'#.*?\n', '', sql_text)

    return sql_text.strip()


def process_sql_file(input_file, output_file):
    """
    Читает SQL из входного файла, удаляет комментарии и записывает результат в выходной файл.

    Параметры:
    input_file (str): Путь к входному файлу.
    output_file (str): Путь к выходному файлу.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        sql_text = file.read()

    clean_sql = remove_sql_comments(sql_text)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(clean_sql)


# Пример использования
input_file = 'input.sql'
output_file = 'output.sql'
process_sql_file(input_file, output_file)
