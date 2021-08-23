import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import sqlite3
from random import randrange, choice
from datetime import timedelta, datetime

class DBListClass(QDialog):
	def __init__(self, parent):
		super(DBListClass, self).__init__(parent)
		dblist_ui = 'db_list.ui'
		uic.loadUi(dblist_ui, self)
		self.parent = parent
		self.tableWidget.setRowCount(\
			len(self.parent.query_res))	
		for i in range(len(self.parent.query_res)):
			for j in range(5):
				self.tableWidget.setItem(i,j,\
				QTableWidgetItem(\
				str(self.parent.query_res[i][j])))
				
		self.show()
				

class DateClass(QMainWindow):
	def __init__(self, parent):
		super(DateClass, self).__init__(parent)
		date_ui = 'date.ui'
		uic.loadUi(date_ui, self)
		self.parent = parent
		self.query_res = None
		self.EnddateEdit.setDate(QDate.currentDate())
		self.EnddateEdit.setMaximumDate(QDate.currentDate())
		self.show()
		
		self.SBButton.clicked.connect(self.SBButtonFunc)
		self.SLButton.clicked.connect(self.SLButtonFunc)
		self.CloseButton.clicked.connect(self.CloseButtonFunc)
		
	def SBButtonFunc(self):
		conn = sqlite3.connect("test.db", isolation_level=None)
		c = conn.cursor()
		query = []
		query2 = []
		query.append('SELECT menu, COUNT(menu) FROM log WHERE')
		query2.append('SELECT datetime, sex, age, category, menu FROM log WHERE')
		if self.parent.age:
			if len(self.parent.age) == 1:
				query.append("age=%d"% (self.parent.age[0]))
				query2.append("age=%d"% (self.parent.age[0]))
			else :
				query.append("age BETWEEN %d AND %d"\
				%(self.parent.age[0], self.parent.age[-1]))
				query2.append("age BETWEEN %d AND %d"\
				%(self.parent.age[0], self.parent.age[-1]))
				
		if self.parent.sex:
			if len(query) == 1:
				query.append("sex='%s'"%(self.parent.sex))
				query2.append("sex='%s'"%(self.parent.sex))
			else :
				query.append("AND sex='%s'"%(self.parent.sex))
				query2.append("AND sex='%s'"%(self.parent.sex))
			
		date1 = []
		date1.append(self.StartdateEdit.date().toString("yyyy-MM-dd"))
		if self.parent.starttime:
			date1.append(self.parent.starttime[0])
		date1 = ' '.join(date1)
		
		date2 = []
		date2.append(self.EnddateEdit.date().toString("yyyy-MM-dd"))
		
		if self.parent.endtime:
			date2.append(self.parent.endtime[0])
		date2 = ' '.join(date2)
		
		if len(query) == 1:
			query.append("datetime BETWEEN datetime('%s') and datetime('%s')"%(date1, date2))
			query2.append("datetime BETWEEN datetime('%s') and datetime('%s')"%(date1, date2))
		else :
			query.append("AND datetime BETWEEN datetime('%s') and datetime('%s')"%(date1, date2))
			query2.append("AND datetime BETWEEN datetime('%s') and datetime('%s')"%(date1, date2))
		
		query.append('GROUP BY menu HAVING COUNT(*)')
		query2.append('ORDER BY datetime')
		
		print(' '.join(query))
		print(' '.join(query2))
		
		c.execute(' '.join(query))
		
		res = list(c.fetchall())
		max_res = max(res, key=lambda x:x[1])
		self.textBrowser.append("Best menu is '%s'\n total selling : %d "%(\
			max_res[0], max_res[1]))
			
		c.execute(' '.join(query2))
		self.query_res = list(c)
		
	def SLButtonFunc(self):
		DBListClass(self)
		
		
		
	def CloseButtonFunc(self):
		self.close()

class SexClass(QDialog):
	def __init__(self, parent):
		super(SexClass, self).__init__(parent)
		sex_ui = 'sex.ui'
		uic.loadUi(sex_ui, self)
		self.parent = parent
		self.show()
		
		self.pushButton.clicked.connect(self.pushButtonFunc)
		
	def pushButtonFunc(self):
		if self.radioButton.isChecked():
			self.parent.sex = 'female'
		elif self.radioButton_2.isChecked():
			self.parent.sex = 'male'
		self.parent.textBrowser.append(self.parent.sex)
		self.close()

class AgeClass(QDialog):
	def __init__(self, parent):
		super(AgeClass, self).__init__(parent)
		age_ui = 'age.ui'
		uic.loadUi(age_ui, self)
		self.parent = parent
		self.show()
		
		self.pushButton.clicked.connect(self.pushButtonFunc)
		
	def pushButtonFunc(self):
		start_age = self.StartBox.value()
		end_age = self.EndBox.value()
		self.parent.age = [i for i in range(start_age,end_age+1)]
		text = [str(start_age),"~", str(end_age)]
		self.parent.textBrowser.append(' '.join(text))
		self.close()

class TimeZoneClass(QDialog):
	def __init__(self, parent):
		super(TimeZoneClass, self).__init__(parent)
		timezone_ui = 'timezone.ui'
		uic.loadUi(timezone_ui, self)
		self.parent = parent
		self.show()
		
		self.pushButton.clicked.connect(self.pushButtonFunc)
		
	def pushButtonFunc(self):
		self.parent.starttime.append(\
			self.StarttimeEdit.time().toString("hh:mm:ss"))
		self.parent.endtime.append(\
			self.EndtimeEdit.time().toString("hh:mm:ss"))
		text = [self.parent.starttime[0],\
			"~",self.parent.endtime[0]]
		self.parent.textBrowser.append(' '.join(text))
		self.close()

class StatisticsClass(QMainWindow):
	def __init__(self, parent):
		super(StatisticsClass, self).__init__(parent)
		statistics_ui = 'statistics.ui'
		uic.loadUi(statistics_ui, self)
		self.parent = parent
		self.show()
		
		self.starttime = []
		self.endtime = []
		
		self.sex = None
		self.age = None
		
		self.TimeZoneButton.clicked.connect(\
			self.TimeZoneButtonFunc)
		self.AgeButton.clicked.connect(\
			self.AgeButtonFunc)
		self.SexButton.clicked.connect(\
			self.SexButtonFunc)
		self.SelectButton.clicked.connect(\
			self.SelectButtonFunc)
			
	def SelectButtonFunc(self):
		DateClass(self)
			
	def SexButtonFunc(self):
		SexClass(self)
			
	def AgeButtonFunc(self):
		AgeClass(self)
			
	def TimeZoneButtonFunc(self):
		TimeZoneClass(self)

