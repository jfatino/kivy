# I don't know what I'm doing and it's fun :)
import os
from SqlTools import Test
from kivy.app import App
from kivy.uix.label import Label
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.clock import Clock
from datetime import datetime, timedelta
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

#class MyGrid(GridLayout):
#    def __init__(self,**kwargs):
#        super(MyGrid, self).__init__(**kwargs)
#        self.now = datetime.now()
#        Clock.schedule_interval(self.update_clock, 1)
#        self.cols = 1
#        self.my_label = Label(text= self.now.strftime('%H:%M:%S'))
#        self.add_widget(self.my_label)
#        self.name = TextInput(multiline = False)
#        self.add_widget(self.name)
#        # quick test to see if I can pre-fill the tb
#        
#        self.name.text=Test.tstring(self,"How about this?")
#        
#    def update_clock(self, *args):
#        #  Called once a second using the kivy.clock module
#        #  Add one second to the current time and display it on the label
#         self.now = self.now + timedelta(seconds = 1)
#        #  self.Label(text = self.now.strftime('%H:%M:%S'))
#         self.my_label.text = self.now.strftime('%H:%M:%S')           
#        # another test
        
class MyBox(BoxLayout):
    def __init__(self,**kwargs):
        super(MyBox).__init__(**kwargs)
        pass
        
    def update_clock(self, *args):
         # Called once a second using the kivy.clock module
         # Add one second to the current time and display it on the label
         self.now = self.now + timedelta(seconds = 1)
         #self.Label(text = self.now.strftime('%H:%M:%S'))
         self.my_label.text = self.now.strftime('%H:%M:%S')  




class MyApp(App):
    title = "Testing"
    Config.set('graphics', 'resizable', False)            
    def build(self):
        superBox        = BoxLayout(orientation='vertical')

   

        horizontalBox   = BoxLayout(orientation='horizontal')

        button1         = Button(text="One")

        button2         = Button(text="Two")

 

        horizontalBox.add_widget(button1)

        horizontalBox.add_widget(button2)

   

        verticalBox     = BoxLayout(orientation='vertical')

        button3         = Button(text="Three")

        button4         = Button(text="Four")

 

        verticalBox.add_widget(button3)

        verticalBox.add_widget(button4)

   

        superBox.add_widget(horizontalBox)

        superBox.add_widget(verticalBox)

        return superBox
        
        
        
        
        
        
        
        
        #return MyBox()
        #return MyGrid()
    

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
    