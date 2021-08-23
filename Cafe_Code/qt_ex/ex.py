import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sqlite3
from random import randrange, choice
from datetime import timedelta, datetime
from statistics import *

form_class = uic.loadUiType("main.ui")[0]

#f = open('db_len.txt', 'rw')

menu = {'coffee':['Espresso', 'Americano', 'Cafe Mocha', 'Cappuccino'],\
	'latte':['Choco Latte', 'Green Latte', 'Cafe Latte', 'S.P. Latte'],\
	'tea':['Camomile','Earl Grey','Lemon Tea','Black Tea','Peppermint'],\
	'juice':['Watermelon','Kiwi','Tomato','Orange','Strawberry'],\
	'ade':['Grapefruit','Orange','Lemon']}

class AvailableTimeClass(QMainWindow):
	def __init__(self, parent):
		super(AvailableTimeClass, self).__init__(parent)
		availabletime_ui = 'availabletime.ui'
		uic.loadUi(availabletime_ui, self)
		self.parent = parent
		self.show()
		
		self.pushButton_2.clicked.connect(self.SelectFunc2)
		self.pushButton_3.clicked.connect(self.SelectFunc3)
		self.pushButton_4.clicked.connect(self.SelectFunc4)
		self.pushButton_5.clicked.connect(self.SelectFunc5)
		self.pushButton_8.clicked.connect(self.SelectFunc8)
		self.pushButton_9.clicked.connect(self.SelectFunc9)
		
	def SelectFunc2(self):
		self.priceBrowser.setPlainText('Select Succed!!')
		self.parent.textBrowser.append('10:00 selected')
		self.parent.parent.priceBrowser.append('10:00 selected')
		self.pushButton_2.setFlat(True)
		
	def SelectFunc3(self):
		self.priceBrowser.setPlainText('Select Succed!!')
		self.parent.textBrowser.append('11:00 selected')
		self.parent.parent.priceBrowser.append('11:00 selected')
		self.pushButton_3.setFlat(True)
		
	def SelectFunc4(self):
		self.priceBrowser.setPlainText('Select Succed!!')
		self.parent.textBrowser.append('12:00 selected')
		self.parent.parent.priceBrowser.append('12:00 selected')
		self.pushButton_4.setFlat(True)
		
	def SelectFunc5(self):
		self.priceBrowser.setPlainText('Select Succed!!')
		self.parent.textBrowser.append('13:00 selected')
		self.parent.parent.priceBrowser.append('13:00 selected')
		self.pushButton_5.setFlat(True)
		
	def SelectFunc8(self):
		self.priceBrowser.setPlainText('Select Succed!!')
		self.parent.textBrowser.append('16:00 selected')
		self.parent.parent.priceBrowser.append('16:00 selected')
		self.pushButton_8.setFlat(True)
		
	def SelectFunc9(self):
		self.priceBrowser.setPlainText('Select Succed!!')
		self.parent.textBrowser.append('17:00 selected')
		self.parent.parent.priceBrowser.append('17:00 selected')
		self.pushButton_9.setFlat(True)

class SeatClass(QMainWindow):
	def __init__(self, parent):
		super(SeatClass, self).__init__(parent)
		seat_ui = 'seat.ui'
		uic.loadUi(seat_ui, self)
		self.parent = parent.parent
		self.show()
		
		self.pushButton.clicked.connect(self.SeatFunc)
		self.pushButton_2.clicked.connect(self.SeatFunc2)
		self.pushButton_3.clicked.connect(self.SeatFunc3)
		self.pushButton_4.clicked.connect(self.SeatFunc4)
		self.pushButton_5.clicked.connect(self.SeatFunc5)
		self.pushButton_6.clicked.connect(self.SeatFunc6)
		self.pushButton_7.clicked.connect(self.SeatFunc7)
		self.pushButton_8.clicked.connect(self.SeatFunc8)
		self.BackButton.clicked.connect(self.BackButtonFunc)
		
	def SeatFunc(self):
		AvailableTimeClass(self)
		self.textBrowser.setPlainText('Seat 1 selected')
		self.parent.priceBrowser.append('Seat 1')
		
	def SeatFunc2(self):
		AvailableTimeClass(self)
		self.textBrowser.setPlainText('Seat 2 selected')
		self.parent.priceBrowser.append('Seat 2')
		
	def SeatFunc3(self):
		AvailableTimeClass(self)
		self.textBrowser.setPlainText('Seat 3 selected')
		self.parent.priceBrowser.append('Seat 3')
		
	def SeatFunc4(self):
		AvailableTimeClass(self)
		self.textBrowser.setPlainText('Seat 4 selected')
		self.parent.priceBrowser.append('Seat 4')
		
	def SeatFunc5(self):
		AvailableTimeClass(self)
		self.textBrowser.setPlainText('Seat 5 selected')
		self.parent.priceBrowser.append('Seat 5')
		
	def SeatFunc6(self):
		AvailableTimeClass(self)
		self.textBrowser.setPlainText('Seat 6 selected')
		self.parent.priceBrowser.append('Seat 6')
		
	def SeatFunc7(self):
		AvailableTimeClass(self)
		self.textBrowser.setPlainText('Seat 7 selected')
		self.parent.priceBrowser.append('Seat 7')
		
	def SeatFunc8(self):
		AvailableTimeClass(self)
		self.textBrowser.setPlainText('Seat 8 selected')
		self.parent.priceBrowser.append('Seat 8')
	
	def BackButtonFunc(self):
		self.close()
		self.parent.priceBrowser.append("Order Completed!\n Please complete your payment")

class AskSeatClass(QDialog):
	def __init__(self, parent):
		super(AskSeatClass, self).__init__(parent)
		askseat_ui = 'ask_seat.ui'
		uic.loadUi(askseat_ui, self)
		self.parent = parent
		self.show()
		
		self.YesButton.clicked.connect(self.YesButtonFunc)
		self.NoButton.clicked.connect(self.NoButtonFunc)
	
	def NoButtonFunc(self):
		self.close()
		self.parent.priceBrowser.append("Order Completed!\n Please complete your payment")
		
	def YesButtonFunc(self):
		self.close()
		SeatClass(self)

class OrderClass(QMainWindow) :
	def __init__(self, parent):
		super(OrderClass, self).__init__(parent)
		order_ui = 'order.ui'
		uic.loadUi(order_ui, self)
		self.show()
		self.menu = []
		self.total_price = 0
		
		self.AmeAdd.clicked.connect(self.AmeAddButtonFunc)
		self.CafAdd.clicked.connect(self.CafAddButtonFunc)
		self.CapAdd.clicked.connect(self.CapAddButtonFunc)
		self.EspAdd.clicked.connect(self.EspAddButtonFunc)
		self.ChoAdd.clicked.connect(self.ChoAddButtonFunc)
		self.GreAdd.clicked.connect(self.GreAddButtonFunc)
		self.LatAdd.clicked.connect(self.LatAddButtonFunc)
		self.SPAdd.clicked.connect(self.SPAddButtonFunc)
		self.CamAdd.clicked.connect(self.CamAddButtonFunc)
		self.EarAdd.clicked.connect(self.EarAddButtonFunc)
		self.LemAdd.clicked.connect(self.LemAddButtonFunc)
		self.BlaAdd.clicked.connect(self.BlaAddButtonFunc)
		self.PepAdd.clicked.connect(self.PepAddButtonFunc)
		self.WatAdd.clicked.connect(self.WatAddButtonFunc)
		self.KiwAdd.clicked.connect(self.KiwAddButtonFunc)
		self.TomAdd.clicked.connect(self.TomAddButtonFunc)
		self.OraAdd.clicked.connect(self.OraAddButtonFunc)
		self.StrAdd.clicked.connect(self.StrAddButtonFunc)
		self.GraAdd.clicked.connect(self.GraAddButtonFunc)
		self.OragAdd.clicked.connect(self.OragAddButtonFunc)
		self.LemoAdd.clicked.connect(self.LemoAddButtonFunc)
		self.OrderButton.clicked.connect(self.OrderButtonFunc)
		self.ExitButton.clicked.connect(self.ExitButtonFunc)
		self.PaymentButton.clicked.connect(self.PaymentButtonFunc)
	
	def LemoAddButtonFunc(self):
		show = ["Lemon"]
		qty = self.LemoSpin.value()
		show.append(str(qty))
		self.total_price += qty*5500
		show.append(str(qty*5500))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def OragAddButtonFunc(self):
		show = ["Orange"]
		qty = self.OragSpin.value()
		show.append(str(qty))
		self.total_price += qty*6000
		show.append(str(qty*6000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def GraAddButtonFunc(self):
		show = ["Grapefruit"]
		qty = self.GraSpin.value()
		show.append(str(qty))
		self.total_price += qty*5500
		show.append(str(qty*5500))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def StrAddButtonFunc(self):
		show = ["Strawberry"]
		qty = self.StrSpin.value()
		show.append(str(qty))
		self.total_price += qty*6000
		show.append(str(qty*6000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def OraAddButtonFunc(self):
		show = ["Orange"]
		qty = self.OraSpin.value()
		show.append(str(qty))
		self.total_price += qty*5500
		show.append(str(qty*5500))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def TomAddButtonFunc(self):
		show = ["Tomato"]
		qty = self.TomSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def KiwAddButtonFunc(self):
		show = ["Kiwi"]
		qty = self.KiwSpin.value()
		show.append(str(qty))
		self.total_price += qty*6000
		show.append(str(qty*6000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def WatAddButtonFunc(self):
		show = ["Watermelon"]
		qty = self.WatSpin.value()
		show.append(str(qty))
		self.total_price += qty*5500
		show.append(str(qty*5500))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def PepAddButtonFunc(self):
		show = ["Peppermint"]
		qty = self.PepSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def BlaAddButtonFunc(self):
		show = ["Black Tea"]
		qty = self.BlaSpin.value()
		show.append(str(qty))
		self.total_price += qty*4500
		show.append(str(qty*4500))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def LemAddButtonFunc(self):
		show = ["Lemon Tea"]
		qty = self.LemSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def EarAddButtonFunc(self):
		show = ["Earl Grey"]
		qty = self.EarSpin.value()
		show.append(str(qty))
		self.total_price += qty*5500
		show.append(str(qty*5500))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def CamAddButtonFunc(self):
		show = ["camomile"]
		qty = self.CamSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def SPAddButtonFunc(self):
		show = ["S.P. Latte"]
		qty = self.SPSpin.value()
		show.append(str(qty))
		self.total_price += qty*6000
		show.append(str(qty*6000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def LatAddButtonFunc(self):
		show = ["Cafe Latte"]
		qty = self.LatSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
		
	def GreAddButtonFunc(self):
		show = ["Green Latte"]
		qty = self.GreSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
	
	def ChoAddButtonFunc(self):
		show = ["Choco Latte"]
		qty = self.ChoSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))	
	
	def AmeAddButtonFunc(self):
		show = ["Americano"]
		qty = self.AmeSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
		
	def CafAddButtonFunc(self):
		show = ["Cafe Mocha"]
		qty = self.CafSpin.value()
		show.append(str(qty))
		self.total_price += qty*4500
		show.append(str(qty*4500))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
		
	def CapAddButtonFunc(self):
		show = ["Cappuccino"]
		qty = self.CapSpin.value()
		show.append(str(qty))
		self.total_price += qty*4500
		show.append(str(qty*4500))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))
		
	def EspAddButtonFunc(self):
		show = ["Espresso"]
		qty = self.EspSpin.value()
		show.append(str(qty))
		self.total_price += qty*4000
		show.append(str(qty*4000))
		
		for _ in range(qty):
			self.menu.append(show[0])

		self.priceBrowser.append('\t'.join(show))

	def OrderButtonFunc(self):
		total = ["Total is : "]
		total.append(str(self.total_price))
		
		self.priceBrowser.append(''.join(total))
		AskSeatClass(self)

	def ExitButtonFunc(self):
		self.close()
		
	def PaymentButtonFunc(self):
		
		conn = sqlite3.connect("test.db", isolation_level=None)
		c = conn.cursor()
		
		sex = choice(['male', 'female'])
		age = choice([i for i in range(20,30)])
		date_time = datetime.now().strftime('%d/%m/%Y %H:%M')
		print(date_time)
		category = [k for m in self.menu for k,v in menu.items() if m in v]
		for i in range(len(self.menu)):
			ca = category[i]
			me = self.menu[i]
			c.execute("INSERT INTO log(datetime, sex, age, category, menu) VALUES(?,?,?,?,?)", (date_time,sex,age,ca,me))
			
			
		self.priceBrowser.append('log successed!')
		

class UserClass(QMainWindow):
	def __init__(self, parent):
		super(UserClass, self).__init__(parent)
		user_ui = 'user.ui'
		uic.loadUi(user_ui,self)
		self.show()

		self.OrderButton.clicked.connect(self.OrderButtonFunc)

	def OrderButtonFunc(self):
		OrderClass(self)
		
class ManagerClass(QMainWindow):
	def __init__(self, parent):
		super(ManagerClass, self).__init__(parent)
		manager_ui = 'manager.ui'
		uic.loadUi(manager_ui, self)
		self.parent = parent
		self.show()
		
		self.StatisticsButton.clicked.connect(\
			self.StatisticsButtonFunc)		

	def StatisticsButtonFunc(self):
		StatisticsClass(self)

class LoginClass(QMainWindow):
	def __init__(self):
		super().__init__()
		login_ui = 'login.ui'
		uic.loadUi(login_ui, self)
		self.show()
		
		self.LoginButton.clicked.connect(self.LoginButtonFunc)
		
	def LoginButtonFunc(self):
		lvl = self.comboBox.currentIndex()
		if lvl == 0:
			UserClass(self)
			
		if lvl == 1:
			ManagerClass(self)
			
		
		

if __name__ == "__main__" :
	app = QApplication(sys.argv)

	myWindow = LoginClass()

	myWindow.show()

	app.exec_()
