import urllib
import webbrowser
from pycbrf.toolbox import ExchangeRates
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
from kivy.metrics import *
from kivy.uix.screenmanager import Screen
import time



KV =	'''

<ButtonNum@Button>:
	background_normal: ''
	background_color: [.2,.18,.76, 1]
	font_size: dp(20)
<ButtonOper@Button>:
	background_normal: ''
	background_color: [.27,0,.62, 1]
	font_size: dp(20)
<ButtonIs@Button>:
	background_normal: ''
	background_color: [.5,.20,1, 1]
	font_size: dp(20)
<ButtonC@Button>:
	background_normal: ''
	background_color: [.91,.09,.09, 1]
	font_size: dp(20)
<Button2@Button>:
	background_color: [.1,.1,.1, 1]
	background_normal: ''
	font_size: dp(20)
	
	
<About@Screen>:
	name: 'about'
	
	BoxLayout:
		orientation: 'vertical'
		
		AnchorLayout:
			size_hint: (1,.1)
			MDIconButton:
				icon: 'home'
				on_press: app.root.current = 'main'
		BoxLayout:
			size_hint: (1,.1)
			Image:
				source: 'mylogo.png'
				allow_stretch: True
		Label:
			size_hint: (1,.1)
			font_size: 60
			text: 'Создатель LEv145'
		Label:
			size_hint: (1,.1)
			font_size: 50
			text: 'Приложение сделано с любовью к коду:3'
		Label:
			size_hint: (1,.1)
			text: 'Версия Python: 3.8.2'
		Label:
			size_hint: (1,.1)
			text: 'Версия Kivy: 1.11.1'
		Label:
			size_hint: (1,.1)
			text: 'Версия Kivy MD: 0.104.0'
		Widget:
			size_hint: (1,.2)
				
		
		Label:
			size_hint: (1,.05)
			text: 'v. 2.5.1'
		Label:
			size_hint: (1,.05)
			text: 'Авторские права ©AmITego'
	
<Menu>:
	name: 'menu'
	
	BoxLayout:
		orientation: 'vertical'
		
		AnchorLayout:
			size_hint: (1,.1)
			MDIconButton:
				icon: 'home'
				on_press: app.root.current = 'main'
		BoxLayout:
			padding: [10]
			orientation: 'vertical'
			size_hint: (1,.9)
			
			MDRaisedButton:
				icon: 'linux'
				text: 'О программе'
				text_color: 0,0,0,1
				font_size: 15
				md_bg_color: .36, .09, 1, 1
				size_hint: (1,.1)
				on_press: app.root.current = 'about'
					
			MDRaisedButton:
				icon: 'web'
				text: 'Мой сайт'
				text_color: 0,0,0,1
				font_size: 15
				md_bg_color: .36, .09, 1, 1
				size_hint: (1,.1)
				on_press: root.html()
			Widget:
				size_hint: (1,.6)
				
<Converter>:
	
	lval: Lval
	textvl: Text_Val
	
	name: 'conver'
	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			size_hint: (1,.07)
			MDIconButton:
				size_hint: (.15,1)
				icon: 'home'
				on_press: app.root.current = 'main'
			Widget:
				size_hint: (.7,1)
			MDIconButton:
				size_hint: (.15,1)
				icon: 'settings'
				on_press: app.root.current = 'menu'
		BoxLayout:
			orientation: 'vertical'
			padding: [150,400]
			
				
			
			
			MDTextField:
				id: Text_Val
				size_hint: (1,.3)
	 		   hint_text: "Напишите наминал перевода"
			    mode: "rectangle"
	  		  color_mode: 'custom'
				line_color_focus: .57, 0, .86, 1
			Widget:
				size_hint: (1,.2)
			BoxLayout:
				size_hint: (1,.2)
				MDCheckbox:
					group: 'group1'
					size_hint: (.3,1)
					on_active: root.get_ruble1()
				MDCheckbox:
					group: 'group1'
					size_hint: (.3,1)
					on_active: root.get_euro1()
				MDCheckbox:
					group: 'group1'
					size_hint: (.3,1)
					on_active: root.get_dollar1()
			Widget:
				size_hint: (1,.1)
			BoxLayout:
				size_hint: (1,.2)
				Image:
					size_hint: (.3,1)
					source: 'rub.png'
				Image:
					size_hint: (.3,1)
					source: 'euro.png'
				Image:
					size_hint: (.3,1)
					source: 'dollar.png'
			Widget:
				size_hint: (1,.1)
			BoxLayout:
				size_hint: (1,.2)
				MDCheckbox:
					group: 'group2'
					size_hint: (.3,1)
					on_active: root.get_ruble2()
				MDCheckbox:
					group: 'group2'
					size_hint: (.3,1)
					on_active: root.get_euro2()
				MDCheckbox:
					group: 'group2'
					size_hint: (.3,1)
					on_active: root.get_dollar2()
			Widget:
				size_hint: (1,.1)
			Label:
				id: Lval
				size_hint: (1,.2)
				text: '0'
				font_size: dp(30)
			Widget:
				size_hint: (1,.2)
			MDRaisedButton:
				size_hint: (1,.3)
				text_color: 1,1,1,1
	            md_bg_color: .36, .09, 1, 1
	            font_size: dp(10)
	            text: 'Вычислить'
				on_press: root.get_value()
				
		
			
		
	


<Main>:

	ans: Ans_label
	glb: Great_label
	
	orientation: 'vertical'
	BoxLayout:
		size_hint: (1,.07)
		MDIconButton:
			size_hint: (.15,1)
			icon: 'cash-multiple'
			on_press: app.root.current = 'conver'
		Widget:
			size_hint: (.7,1)
		MDIconButton:
			size_hint: (.15,1)
			icon: 'settings'
			on_press: app.root.current = 'menu'

	Label:
		id: Ans_label
		text: '0'
		font_size: dp(20)
		halign: 'right'
		valign: 'center'
		text_size: self.size
		size_hint: (1, .13)
	Label:
		id: Great_label
		text: '0'
		font_size: dp(30)
		halign: 'right'
		valign: 'top'
		text_size: self.size
		size_hint: (1, .2)
	GridLayout:
		rows: 1
		size_hint: (1,.1)
		Button2:
			on_press: root.add_oper('(')
			text: '('
		Button2:
			on_press: root.add_oper(')')
			text: ')'
		Button2:
			on_press: root.add_oper('√')
			text: '√'
		Button2:
			on_press: root.add_oper('^')
			text: '^'
		ButtonC:
			on_press: root.C_oper()
			text: 'C'
	GridLayout:
		cols: 4
		size_hint: (1, .5)
		ButtonNum:
			on_press: root.add_num(7)
			text: '7'
		ButtonNum:
			on_press: root.add_num(8)
			text: '8'
		ButtonNum:
			on_press: root.add_num(9)
			text: '9'
		ButtonOper:
			on_press: root.add_oper('x')
			text: 'x'
		ButtonNum:
			on_press: root.add_num(4)
			text: '4'
		ButtonNum:
			on_press: root.add_num(5)
			text: '5'
		ButtonNum:
			on_press: root.add_num(6)
			text: '6'
		ButtonOper:
			on_press: root.add_oper('-')
			text: '-'
		ButtonNum:
			on_press: root.add_num(1)
			text: '1'
		ButtonNum:
			on_press: root.add_num(2)
			text: '2'
		ButtonNum:
			on_press: root.add_num(3)
			text: '3'
		ButtonOper:
			on_press: root.add_oper('+')
			text: '+'
		ButtonNum:
			on_press: root.add_num(0)
			text: '0'
		ButtonNum:
			on_press: root.add_num('.')
			text: '.'
		ButtonIs:
			on_press: root.oper_is()
			text: '='
		ButtonOper:
			on_press: root.add_oper('÷')
			text: '÷'
	
			
		
		
	



ScreenManager:
	Screen:
		name: 'main'
		Main:
    Menu:
    About:
    Converter:
'''
class Converter(Screen):
	
	def __init__(self, **kwargs):
		
		try:
	
			self.time = time.strftime('%Y-%m-%d')
			
			rates = ExchangeRates(self.time, locale_en=True)
			self.usd = rates['USD'].value
			rates = ExchangeRates(self.time, locale_en=True)
			self.eur = rates['EUR'].value
			
			self.rub = 1
			
		
		except IOError:
			
			self.usd = 64.21
			self.eur = 70.90
			self.rub = 1
			
			
			
		super().__init__(**kwargs)
	
	def get_dollar1(self):
		self.val1 = self.usd
		
		
	def get_euro1(self):
		self.val1 = self.eur
		
		
	def get_ruble1(self):
		self.val1 = self.rub
		
		
	def get_dollar2(self):
		self.val2 = self.usd
		
		
	def get_euro2(self):
		self.val2 = self.eur
		
		
	def get_ruble2(self):
		self.val2 =  self.rub
		
	def get_value(self):
		try:
			a = 1
			a = float(self.textvl.text)
			self.val = (float(self.val1)/float(self.val2)*a)
			self.lval.text = str(self.val)
		except ValueError:
			pass
		
		
		

class Menu(Screen):
	
	def html(self):
		webbrowser.open('https://amitego.ru', new = 2)
		
class Main(BoxLayout):
	
	def __init__(self, **kwargs):
		self.math = ""
		self.realmath = ""
		super().__init__(**kwargs)

	def add_num(self, instance):
		self.math += str(instance)
		self.realmath += str(instance)
		self.update_label()
	def update_lab2(self):
		self.ans.text = self.realmath
	
	def update_lab(self):
		self.glb.text = self.realmath
	def update_label(self):
		self.glb.text = self.math
		
	def C_oper(self):
		if self.realmath != 0:
			self.realmath = self.realmath[:-1]
			self.math = self.math[:-1]
		else:
			self.realmath =""
		self.update_label()
		self.update_lab()
		
		

		
		self.update_label()
	
	def add_oper(self, instance):
		if instance == 'x':
			self.math += 'x'
			self.realmath += '*'
		elif instance == '÷':
			self.math += '÷'
			self.realmath += '/'
		elif instance == "√":
			self.math += '√'
			self.realmath += '** 0.5'
		elif instance == "^":
			self.math += '^'
			self.realmath += '**'
		else:
			self.math += str(instance)
			self.realmath += str(instance)
		self.update_label()
		
	def oper_is(self):
		try:
			self.realmath = str(eval(self.realmath))
			self.update_lab2()
			self.update_lab()
			self.realmath = ""
			self.math = ""
		except SyntaxError:
			self.glb.text = 'Ошибка: неправельное написание!'
			self.math = ""
			self.realmath = ""
		except ZeroDivisionError:
			self.glb.text = 'Ошибка: деление на 0!'
			self.math = ""
			self.realmath = ""
			


class App(MDApp):
		
	def __init__(self, **kwargs):
		self.theme_cls.theme_style = 'Dark'
		super().__init__(**kwargs)

	def build(self):

		
		return Builder.load_string(KV)

if __name__ == "__main__":
    App().run()