from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from components.scrollabre_form_area import ScrollableFormArea
from components.text_input_area import TextInputArea
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.config import Config

Config.set('input', 'mouse', 'mouse,disable_multitouch,disable_on_activity')


Builder.load_file('style.kv')

class Root(BoxLayout):
    output_text = StringProperty('')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.input_text = ''
        self.find_and_change_params = []

        self.orientation = 'vertical'
        scrollable_form_area = ScrollableFormArea(size_hint=(1, 0.3), update_params=self.update_params)
        self.add_widget(scrollable_form_area)

        self.fixed_area = GridLayout(cols = 2)
        self.add_widget(self.fixed_area)

        text_input_area = TextInputArea(update_input_text=self.update_input_text)
        self.fixed_area.add_widget(text_input_area)

        self.text_output_area = TextInput(

        )
        self.fixed_area.add_widget(self.text_output_area)

    def update_input_text(self, new_text: str):
        self.input_text = new_text
        self.update_output_text()

    def update_params(self, index: int, key: str, value: str):
        if len(self.find_and_change_params) <= index:
            self.find_and_change_params.extend([{'key':'', 'value':''}] * (index + 1 - len(self.find_and_change_params)))

        self.find_and_change_params[index][key] = value

        self.update_output_text()

    def update_output_text(self):
        if len(self.find_and_change_params) == 0:
            self.output_text = self.input_text

        updated_text = self.input_text

        for param in self.find_and_change_params:
            key = param.get('key')
            value = param.get('value')
            updated_text = updated_text.replace(key, value)

        self.output_text = updated_text
        
        self.text_output_area.text = self.output_text

class MyApp(App):
    def build(self):
        return Root()

if __name__ == "__main__":
    MyApp().run()
