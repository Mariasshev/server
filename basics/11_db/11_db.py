# Робота з базами даних
# 1. Встановлення СУБД. Використовуємо MYSQL
# 2. Створюємо БД та користувача для неї (подаємо команди у Workbench)

# CREATE DATABASE server_221;
# CREATE USER user_knp_221@localhost IDENTIFIED BY 'pass_221';
# GRANT ALL PRIVILEGES ON server_221.* TO user_knp_221@localhost;

# 3. Додаємо драйвери підключення до БД

import mysql.connector
from tabulate import tabulate

db_ini = {
    'host': 'localhost',
    'port': 3306,
    'user': 'user_knp_221',
    'password': 'pass_221',
    'database': 'server_221',
    'charset': 'utf8mb4',
    'use_unicode': True,
    'collation': 'utf8mb4_unicode_ci'
}

db_connection = None

def connect_db() :
    global db_connection
    try:
        db_connection = mysql.connector.connect(**db_ini)
    except mysql.connector.Error as err:
        print(err)
    else :
        print("Connection OK")


def show_databases() :                          # Виконання SQL запитів
    global db_connection                        # 1. Контекст виконання команди (SqlCommand [ADO], Statement [JDBC])
    if db_connection is None : return           #    cursor [Python]
    try :                                       #    Контекст формує команду, передає її на виконання 
        cursor = db_connection.cursor()         #    та контролює передачу результату (ітерування)
        cursor.execute("SHOW DATABASES")        #    Рекомендується для різних команд утворювати свої контексти,
        # Результатом є генерування 
        print(cursor.column_names)              #    не виконуючи багатьої команд в одному контексті
    except mysql.connector.Error as err:        #
        print(err)                              # 2. Виконання запиту (з результатами) запускає генератор
    else :                                      #    з боку СУБД, передача даних з якого відбувається через
        print(cursor.column_names)              #    ітерування курсора
        print("-----------------")              # 3. Результат команди розділяється - окремо назви полів, 
        for row in cursor :                     #    окремо самі результати
            print(row)                          #
    finally :                                   # 4. Контекст команди має бути закритим для додаткового
        cursor.close()                          #    контролю того, що дані передані та ресурси звільнені


def generate_union(n) :
    global db_connection
    cursor = db_connection.cursor()
    rows = []
    for i in range(n) :
        cursor.execute("select uuid(), uuid()")
        row = cursor.fetchone()
        rows.append(row)
        
    print(tabulate(rows, headers=cursor.column_names, tablefmt="grid"))

def close_connection() :
    db_connection.close()

def main() :
    connect_db()
    #show_databases()
    generate_union(3)
    close_connection()

if __name__ == '__main__':
    main()


