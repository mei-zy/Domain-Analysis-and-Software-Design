import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class OrderClass(QMainWindow) :
	def __init__(self, parent):
		super(OrderClass, self).__init__(parent)
		order_ui = 'order.ui'
		uic.loadUi(order_ui, self)
		self.show()
		
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
		self.OrderButton.clicked.connect(self.OrderButtonFunc)
		self.ExitButton.clicked.connect(self.ExitButtonFunc)
	
	def EarAddButtonFunc(self):
		show = ["Earl Grey"]
		qty = self.EarSpin.value()
		show.append(str(qty))
		self.total_price += qty*5500
		show.append(str(qty*5500))

		self.priceBrowser.append('\t'.join(show))
	
	def CamAddButtonFunc(self):
		show = ["camomile"]
		qty = self.CamSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))

		self.priceBrowser.append('\t'.join(show))
	
	def SPAddButtonFunc(self):
		show = ["S.P. Latte"]
		qty = self.SPSpin.value()
		show.append(str(qty))
		self.total_price += qty*6000
		show.append(str(qty*6000))

		self.priceBrowser.append('\t'.join(show))
	
	def LatAddButtonFunc(self):
		show = ["Cafe Latte"]
		qty = self.LatSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))

		self.priceBrowser.append('\t'.join(show))
		
	def GreAddButtonFunc(self):
		show = ["Green Latte"]
		qty = self.GreSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))

		self.priceBrowser.append('\t'.join(show))
	
	def ChoAddButtonFunc(self):
		show = ["Choco Latte"]
		qty = self.ChoSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))

		self.priceBrowser.append('\t'.join(show))	
	
	def AmeAddButtonFunc(self):
		show = ["Americano"]
		qty = self.AmeSpin.value()
		show.append(str(qty))
		self.total_price += qty*5000
		show.append(str(qty*5000))

		self.priceBrowser.append('\t'.join(show))
		
	def CafAddButtonFunc(self):
		show = ["Cafe Mocha"]
		qty = self.CafSpin.value()
		show.append(str(qty))
		self.total_price += qty*4500
		show.append(str(qty*4500))

		self.priceBrowser.append('\t'.join(show))
		
	def CapAddButtonFunc(self):
		show = ["Cappuccino"]
		qty = self.CapSpin.value()
		show.append(str(qty))
		self.total_price += qty*4500
		show.append(str(qty*4500))

		self.priceBrowser.append('\t'.join(show))
		
	def EspAddButtonFunc(self):
		show = ["Espresso"]
		qty = self.EspSpin.value()
		show.append(str(qty))
		self.total_price += qty*4000
		show.append(str(qty*4000))

		self.priceBrowser.append('\t'.join(show))

	def OrderButtonFunc(self):
		total = ["Order Completed!!\n","Total is : "]
		total.append(str(self.total_price))
		
		self.priceBrowser.append(''.join(total))
		AskSeatClass(self)

	def ExitButtonFunc(self):
		self.close()
