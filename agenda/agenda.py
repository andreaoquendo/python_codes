import sqlite3

agenda = sqlite3.connect('agenda.db')

cursor = agenda.cursor()

# cursor.execute("CREATE TABLE agenda (name text, phone integer, email text)")
# agenda.commit()


def add_register(name, phone, email):
    cursor.execute("INSERT INTO agenda VALUES('" +
                   name + "', "+phone+", '"+email+"')")
    agenda.commit()


print("Add a register:")
name = input("Name: ")
phone = input("Phone: ")
email = input("Email: ")
add_register(name, phone, email)
