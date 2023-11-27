from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('fuck.kv')

class MyLayout(Widget):
	
	def slide_it(self, color, *args):
		current_color = self.ids.my_label.background_color
		r,g,b,a = current_color
		
		if color == 'red':
			r = args[1]/255
		elif color == 'green':
			g = args[1]/255
		else:
			b = args[1]/255
		
		self.ids.my_label.background_color = (r,g,b,a)
		self.ids.my_color.text = f'{int(r*255),int(g*255),int(b*255)}'

		

class AwesomeApp(App):
	def build(self):
		Window.clearcolor = (127/255, 124/255, 156/255)
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()

