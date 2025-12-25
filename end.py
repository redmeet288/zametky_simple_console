import os
import json
print("Добро пожаловать в Заметки");
list_zam = {};

if os.path.exists("notes.json"): # выгрузка
    try:
        with open("notes.json", "r", encoding="utf-8") as f:
            list_zam = json.load(f)
        print("Заметки загружены")
    except:
        print("Ошибка загрузки")

def save_notes(): # save
    try:
        with open("notes.json", "w", encoding="utf-8") as f:
            json.dump(list_zam, f, ensure_ascii=False, indent=2)
    except:
        print("Ошибка сохранения")


def AddZam(list_zam): # добавление
    print("Введите заголовок");
    zag = input("--- ");
    print("Введите описание");
    op = input("--- ");
    list_zam[zag] = op;
    save_notes()


def CheckZam(list_zam, cca): # просмотр заметки
    print("=" * 20);
    print(list_zam[cca]);
    print("=" * 20);


def DeleteZam(list_zam, cca): # удаление
    del list_zam[cca];
    save_notes()


def EditZam(list_zam, cca): # редакт заметки
    if cca in list_zam:
        current_text = list_zam[cca];
        print(f"Текущая заметка: {current_text}");
        print("Отредактируйте текст");


        new_text = input(f"{current_text}| ");
        new_text = new_text.replace("|", "");

        if new_text.strip():
            list_zam[cca] = new_text.strip();
        else:
            print("Изменения не будет");
    else:
        print("Заметки нет");


while(True): # отсновной поток
    print("Выберите из списка");
    print("0.Добавить заметку");
    for i, index in enumerate(list_zam.keys()):
        print(f"{i + 1}. {index}");

    try:
        choice = input("Введите номер или 0: ").strip();

        if choice == "0":
            AddZam(list_zam);
            print("*" * 10 + " добавлено");
            continue;

        num = int(choice) - 1;
        keys_list = list(list_zam.keys());

        if 0 <= num < len(keys_list):
            cca = keys_list[num]
            CheckZam(list_zam, cca)

            print("\nЧто сделать?");
            print("1. Удалить");
            print("2. Редактировать");
            print("3. Вернуться назад");

            cha = input("Введите (1-3): ").strip();

            match cha:
                case "1":
                    DeleteZam(list_zam, cca);
                case "2":
                    EditZam(list_zam, cca);
                case "3":
                    continue;
                case _:
                    print("неверно - (1-3)");
        else:
            print("нет такой заметки");

    except (ValueError, KeyError):
        print("не число");

    print("-" * 20);
