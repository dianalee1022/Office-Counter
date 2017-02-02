'''
Author: Diana Lee
Title: Office Counter
'''
#__version__ = '1.0'

import kivy
kivy.require('1.0.6')
import time
import datetime

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import *
from kivy.graphics import Color, Rectangle, Point, GraphicException

now = datetime.datetime.now()
currentTime = str(now.day) + "/" + str(now.month) + "/" + str(now.year)

class Boxes(FloatLayout):
	main_container = ObjectProperty(None)
	
	def call_pressed(self):
		global currentTime
		result = "hello it's call!" + currentTime
		self.ids.call_count.text = result
	def inperson_pressed(self):
		self.ids.inperson_count.text = "hellow it's in person!"
	def call_released(self):
		self.ids.call_count.text = "number of calls!"
	def inperson_released(self):
		self.ids.inperson_count.text = "number of inperson counts!"


class CounterApp(App):
	def build(self):
		return Boxes()

if __name__ == '__main__':
    CounterApp().run()
