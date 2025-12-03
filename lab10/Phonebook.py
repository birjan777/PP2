import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        database="LAB10",
        user="postgres",
        password="5432"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Таблица phonebook создана.")

def insert_user(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Добавлено: {name} — {phone}")

def insert_from_csv(file_path):
    conn = connect()
    cur = conn.cursor()
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 2:
                print(f"Пропущена строка (не 2 элемента): {row}")
                continue
            name, phone = row
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name.strip(), phone.strip()))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Данные из CSV добавлены: {file_path}")

def update_user(old_name, new_name=None, new_phone=None):
    conn = connect()
    cur = conn.cursor()
    if new_name and new_phone:
        cur.execute("UPDATE phonebook SET name = %s, phone = %s WHERE name = %s", (new_name, new_phone, old_name))
    elif new_name:
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))
    elif new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, old_name))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Обновлено: {old_name} -> {new_name or '[не изменено]'} / {new_phone or '[не изменена]'}")

def search_user(name=None, phone=None):
    conn = connect()
    cur = conn.cursor()
    if name:
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
    elif phone:
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"%{phone}%",))
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_user(name=None, phone=None):
    conn = connect()
    cur = conn.cursor()
    if name:
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    elif phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Удален пользователь с {'именем' if name else 'телефоном'}: {name or phone}")

# Меню
def menu():
    create_table()
    while True:
        print("\nВыберите действие:")
        print("1 - Добавить пользователя вручную")
        print("2 - Добавить пользователей из CSV")
        print("3 - Обновить данные пользователя")
        print("4 - Найти пользователя")
        print("5 - Удалить пользователя")
        print("6 - Показать всех")
        print("0 - Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            insert_user(name, phone)

        elif choice == "2":
            path = input("Введите путь к CSV-файлу (например, users.csv): ")
            insert_from_csv(path)

        elif choice == "3":
            old_name = input("Введите текущее имя пользователя: ")
            new_name = input("Введите новое имя (или оставьте пустым): ")
            new_phone = input("Введите новый номер (или оставьте пустым): ")
            update_user(old_name, new_name if new_name else None, new_phone if new_phone else None)

        elif choice == "4":
            search_by = input("Искать по имени (n) или телефону (p)? ")
            if search_by.lower() == "n":
                name = input("Введите имя: ")
                search_user(name=name)
            elif search_by.lower() == "p":
                phone = input("Введите номер: ")
                search_user(phone=phone)

        elif choice == "5":
            delete_by = input("Удалить по имени (n) или телефону (p)? ")
            if delete_by.lower() == "n":
                name = input("Введите имя: ")
                delete_user(name=name)
            elif delete_by.lower() == "p":
                phone = input("Введите номер: ")
                delete_user(phone=phone)

        elif choice == "6":
            search_user()

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()