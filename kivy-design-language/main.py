import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty


class NumericInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if substring.isdigit() or substring == "":
            return super().insert_text(substring, from_undo=from_undo)
        else:
            return False

class MainGridLayout(GridLayout):
    answer = StringProperty("")
    name = ObjectProperty(None)
    birth = ObjectProperty(None)

    def __init__(self, **kwargs):
        

        super(MainGridLayout, self).__init__(**kwargs)

    def press(self):
        
        
        if self.name.text == '' or self.birth.text == '':
            return
        else:
            if int(self.birth.text)> 1999:
                self.answer = f"Olá, {self.name.text}! Infelizmente, você é NUTELLA :("
            else:
                self.answer = f"Olá, {self.name.text}! Parabéns, você não é nutella!"
        

class MyApp(App):
    def build(self):
        return MainGridLayout()
    

if __name__ == '__main__':
    MyApp().run()