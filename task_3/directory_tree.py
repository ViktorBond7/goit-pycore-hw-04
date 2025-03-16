from colorama import Fore
from pathlib import Path
import sys

def print_directory_tree(root_dir: Path, indent='')-> None:
    root_dir = Path(root_dir)
    
    if not root_dir.is_dir():
        print(f"Помилка: '{root_dir}' не є директорією або не існує.")
        return
        
    for item in root_dir.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + f"📁 {item.name}/")
            print_directory_tree(item, indent + "   ")
        else:
            print(indent + Fore.GREEN + f"📄 {item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "❗ вкажіть шлях до директорії")
    else:
        print_directory_tree(Path(sys.argv[-1]))
         

# print_directory_tree('task_3')
















