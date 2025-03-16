
def total_salary(path: str)-> tuple[float, float]:
    try:
        total=0
        average=0
        count= 0
        with open(path, encoding="utf-8") as file:
            while True:
                line = file.readline().strip()
           
                if not line:
                    break
           
                parts = line.split(',')[-1]
                total+=float(parts)
                count +=1
    except FileNotFoundError:
        print(f'Файл {path} не знайдено.')
        
    except Exception as e:
        print(f"Сталася помилка: {e}")
    if count > 0: 
        average = round(total / count, 2)    
  
    return (total, average)


total, average = total_salary('task_1/data.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

assert isinstance(total_salary('task_1/data.txt'), tuple)
