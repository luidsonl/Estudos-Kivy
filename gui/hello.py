import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class NumericInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if substring.isdigit() or substring == "":
            return super().insert_text(substring, from_undo=from_undo)
        else:
            return False

class MainGridLayout(GridLayout):


    def __init__(self, **kwargs):

        self.cols = 1

        self.top_grid = GridLayout(
            row_force_default= True,
            row_default_height = 60
        )
        self.top_grid.cols = 2

        super(MainGridLayout, self).__init__(**kwargs)

        self.name_label = Label(text="Qual seu nome?")
        self.top_grid.add_widget(self.name_label)
        
        self.name_input = TextInput(multiline = False)
        self.top_grid.add_widget(self.name_input)

        self.birth_label = Label(text="Em qual ano você nasceu?")
        self.top_grid.add_widget(self.birth_label)

        self.birth_input = NumericInput(multiline = False)
        self.top_grid.add_widget(self.birth_input)

        self.add_widget(self.top_grid)

        self.submit_button = Button(
            text="Fazer cálculos", 
            font_size=32,
            size_hint_y = None,
            height= 50
        )
        self.submit_button.bind(on_press=self.press)
        self.add_widget(self.submit_button)

        self.text_message = Label()
        self.add_widget(self.text_message)

        


    def press(self, instance):
        name = self.name_input.text
        birth = self.birth_input.text

        if name == '' or birth == '':
            return
        else:
            if int(birth)> 1999:
                self.text_message.text = f"Olá, {name}! Infelizmente, você é NUTELLA :("
            else:
                self.text_message.text = f"Olá, {name}! Parabéns, você não é nutella!"
        

class MyApp(App):
    def build(self):
        return MainGridLayout()
    

if __name__ == '__main__':
    MyApp().run()