import sqlite3
from create_database_dict_function import create_dict_table_db

name_database = input("What will be the name of your database? \n"
                      "(Please don't use spaces) ")
db = sqlite3.connect(f'{name_database}.sqlite')

name_table, type_pk, other_values, dict_pass, primary_key, list_val_dict, length_keys = create_dict_table_db()

dict_keys = []
dict_values = []
for key, value in dict_pass.items():
    dict_keys.append(key)
    dict_values.append(value)

db.execute(f"CREATE TABLE IF NOT EXISTS {name_table}({primary_key} {type_pk}, {other_values})")

count = 0
new_other_values = ", ".join(other_values.split(sep=" ")[::2])
for items1 in dict_keys:
    values_2 = "'" + "', '".join(dict_values[count])
    db.execute(f"INSERT INTO {name_table} ({primary_key}, {new_other_values}) VALUES "
               f"('{dict_keys[count]}', {values_2}')")
    if count + 1 > len(dict_keys):
        break
    count += 1

db.commit()
db.close()