import sqlite3
import sqlite3 as sql

flag = True

connection = sql.connect("../product_base.db")
cursor = connection.cursor()

if flag:

    cursor.execute("""CREATE TABLE IF NOT EXISTS product(
       productTd INT PRIMARY KEY,
       name TEXT,
       proteins REAL,
       fats REAL,
       carbohydrates REAL,
       calories REAL)""")
    connection.commit()

last = 1


def add_item():

    import os
    global last
    names_of_files = os.listdir(r"database food e")[1:]

    for name in names_of_files:

        with open(os.path.join(r"database food e", name), "r") as out_file:

            data = out_file.readlines()
            data = list(map(lambda x: x.split("\t"), data))
            id_p = iter(range(last, len(data) + last))
            for i in range(len(data)):
                try:
                    cursor.execute(
                        """INSERT INTO product(productTd, name, proteins, fats, carbohydrates, calories) 
                        VALUES(?, ?, ?, ?, ?, ?)""", [next(id_p)] + data[i])
                    connection.commit()
                except sqlite3.ProgrammingError or sqlite3.IntegrityError:
                    print(name, i)

            last += len(data)

add_item()



