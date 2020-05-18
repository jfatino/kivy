# I don't know what I'm doing and it's fun :)
import os
from SqlTools import Test
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)
        # quick test to see if I can pre-fill the tb
        
        self.name.text="Hello"

class MyApp(App):
    title = "Testing"
    Config.set('graphics', 'resizable', False)            
    def build(self):
        return MyGrid()
                   
    


if __name__ == "__main__":
    MyApp().run()
