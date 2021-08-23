import sqlite3
from random import randrange, choice
from datetime import timedelta, datetime

conn = sqlite3.connect("test.db", isolation_level=None)

c = conn.cursor()

c.execute("SELECT menu FROM log WHERE age=22")

print(c.fetchone())

c.execute("SELECT menu, sex, COUNT(menu) FROM log WHERE age=22 AND datetime BETWEEN datetime('2020-11-29 09:00:00') and datetime('2020-11-29 18:00:00') AND SEX='female' GROUP BY menu HAVING COUNT(*)")

res = list(c.fetchall())
print(res)

print(max(res, key=lambda x: x[2]))
