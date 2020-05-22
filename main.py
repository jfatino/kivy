# I don't know what I'm doing and it's fun :)
import os
from SqlTools import Test
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.clock import Clock
from datetime import datetime, timedelta

class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.now = datetime.now()
        Clock.schedule_interval(self.update_clock, 1)
        self.cols = 1
        self.my_label = Label(text= self.now.strftime('%H:%M:%S'))
        self.add_widget(self.my_label)
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)
        # quick test to see if I can pre-fill the tb
        
        self.name.text=Test.tstring(self,"How about this?")
        
    def update_clock(self, *args):
         # Called once a second using the kivy.clock module
         # Add one second to the current time and display it on the label
         self.now = self.now + timedelta(seconds = 1)
         #self.Label(text = self.now.strftime('%H:%M:%S'))
         self.my_label.text = self.now.strftime('%H:%M:%S')           
        # another test
        

class MyApp(App):
    title = "Testing"
    Config.set('graphics', 'resizable', False)            
    def build(self):
        return MyGrid()
    

if __name__ == "__main__":
    MyApp().run()





    # def build(self):
    #     self.now = datetime.now()

    #     # Schedule the self.update_clock function to be called once a second
    #     Clock.schedule_interval(self.update_clock, 1)
    #     self.my_label = Label(text= self.now.strftime('%H:%M:%S'))
    #     return self.my_label  # The label is the only widget in the interface

    # def update_clock(self, *args):
    #     # Called once a second using the kivy.clock module
    #     # Add one second to the current time and display it on the label
    #     self.now = self.now + timedelta(seconds = 1)
    #     self.my_label.text = self.now.strftime('%H:%M:%S')           
    