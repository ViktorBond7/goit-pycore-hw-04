
def get_cats_info(path: str) ->list[dict]:
    result = []
    try:
       with open(path, encoding="utf-8") as file:
           for line in file:
               line = line.strip()
               parts = line.split(',')
               result.append({
                   'id': parts[0],
                   'name': parts[1],
                   'age': parts[2]
               })

    except FileNotFoundError:
        print(f'Файл {path} не знайдено.')
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []
    return result

print(get_cats_info('task_2/data_cats.txt'))

