import csv
from pystyle import Colors, Colorate

user_input = input(Colorate.Horizontal(Colors.yellow_to_green, "Введите имя для поиска: ")).strip().lower()

found = False
with open('boardakshop.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  
    for row in reader:
        
        for cell in row:
            if user_input in cell.strip().lower():
                found = True
                found_row = row
                break
        if found:
            break

if found:
    info = ', '.join(found_row)
    print(Colorate.Horizontal(Colors.green_to_cyan, f"Имя '{user_input}' найдено в базе! Информация: {info}"))
else:
    print(Colorate.Horizontal(Colors.red_to_yellow, f"Имя '{user_input}' не найдено в файле."))