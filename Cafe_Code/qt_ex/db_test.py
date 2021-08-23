import sqlite3
from random import randrange, choice
from datetime import timedelta, datetime

def random_date(start, end):
	delta = end - start
	int_delta = (delta.days*24*60*60)+delta.seconds
	random_second = randrange(int_delta)
	return start+timedelta(seconds=random_second)

date_list = []

d1 = datetime.strptime('29/11/2020 9:00', '%d/%m/%Y %H:%M')
d2 = datetime.strptime('29/11/2020 18:00', '%d/%m/%Y %H:%M')
for _ in range(1000):
	date_list.append(random_date(d1,d2))
	
d1 = datetime.strptime('30/11/2020 9:00', '%d/%m/%Y %H:%M')
d2 = datetime.strptime('30/11/2020 18:00', '%d/%m/%Y %H:%M')
for _ in range(1000):
	date_list.append(random_date(d1,d2))
	
d1 = datetime.strptime('1/12/2020 9:00', '%d/%m/%Y %H:%M')
d2 = datetime.strptime('1/12/2020 18:00', '%d/%m/%Y %H:%M')
for _ in range(1000):
	date_list.append(random_date(d1,d2))
	
d1 = datetime.strptime('2/12/2020 9:00', '%d/%m/%Y %H:%M')
d2 = datetime.strptime('2/12/2020 18:00', '%d/%m/%Y %H:%M')
for _ in range(1000):
	date_list.append(random_date(d1,d2))
	
d1 = datetime.strptime('3/12/2020 9:00', '%d/%m/%Y %H:%M')
d2 = datetime.strptime('3/12/2020 18:00', '%d/%m/%Y %H:%M')
for _ in range(1000):
	date_list.append(random_date(d1,d2))

d1 = datetime.strptime('4/12/2020 9:00', '%d/%m/%Y %H:%M')
d2 = datetime.strptime('4/12/2020 18:00', '%d/%m/%Y %H:%M')
for _ in range(1000):
	date_list.append(random_date(d1,d2))
	
d1 = datetime.strptime('5/12/2020 9:00', '%d/%m/%Y %H:%M')
d2 = datetime.strptime('5/12/2020 18:00', '%d/%m/%Y %H:%M')
for _ in range(1000):
	date_list.append(random_date(d1,d2))
	
d1 = datetime.strptime('6/12/2020 9:00', '%d/%m/%Y %H:%M')
d2 = datetime.strptime('6/12/2020 18:00', '%d/%m/%Y %H:%M')
for _ in range(1000):
	date_list.append(random_date(d1,d2))
	
test_list = []
sex = ['male', 'female']
age = [i for i in range(20,30)]
category = ['coffee', 'latte', 'tea', 'juice', 'ade']
menu = {'coffee':['Espresso', 'Americano', 'Cafe Mocha', 'Cappuccino'],\
	'latte':['Choco Latte', 'Green Latte', 'Cafe Latte', 'S.P. Latte'],\
	'tea':['Camomile','Earl Grey','Lemon Tea','Black Tea','Peppermint'],\
	'juice':['Watermelon','Kiwi','Tomato','Orange','Strawberry'],\
	'ade':['Grapefruit','Orange','Lemon']}

for i in range(len(date_list)):
	s = choice(sex)
	a = choice(age)
	c = choice(category)
	m = choice(menu[c])
	test_list.append([date_list[i],s,a,c,m])
	
tuple_test = tuple(test_list)

conn = sqlite3.connect("test.db", isolation_level=None)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS log \
	(id INTEGER PRIMARY KEY, datetime DATETIME, sex STRING, age INT, category STRING, menu STRING)")

for tt in tuple_test:
	c.execute("INSERT INTO log(datetime, sex, age, category, menu)\
	VALUES(?,?,?,?,?)",\
		tt)

