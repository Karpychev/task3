import json
import sys

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def fill_report_structure(tests_structure, values_dict):
    if isinstance(tests_structure, dict):
        # Если это словарь, рекурсивно обрабатываем его
        for key, value in tests_structure.items():
            if key == "id" and value in values_dict:
                tests_structure["value"] = values_dict[value]
            elif isinstance(value, (dict, list)):
                fill_report_structure(value, values_dict)
    elif isinstance(tests_structure, list):
        # Если это список, обрабатываем каждый элемент
        for item in tests_structure:
            fill_report_structure(item, values_dict)

def main(values_file, tests_file, report_file):
    # Загрузка данных из файлов
    values = load_json(values_file)
    tests = load_json(tests_file)

    # Преобразуем список значений в словарь для быстрого доступа
    values_dict = {item['id']: item['value'] for item in values}

    # Заполняем структуру отчета
    fill_report_structure(tests, values_dict)

    # Сохраняем результат в report.json
    with open(report_file, 'w', encoding='utf-8') as file:
        json.dump(tests, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python KarpychevAlexandrPython.txt values.json tests.json report.json")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    main(values_file, tests_file, report_file)
