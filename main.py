import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid():
    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols =2
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline = False)
        self.adw

class MyApp(App):
    title = "Testing"
                
    def build(self):
        return Label(text="Hello")
                   
    


if __name__ == "__main__":
    MyApp().run()
